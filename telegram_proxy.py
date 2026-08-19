# Telegram MTProto proxy integration for Spider Panel.
# Uses the maintained async MTProto proxy implementation from the
# `mtprotoproxy` package instead of the previous incomplete relay.

from __future__ import annotations

import asyncio
import hashlib
import logging
import os
import re
import signal
from typing import Dict, Optional

logger = logging.getLogger("Spider-TelegramProxy")

SECRET_RE = re.compile(r"^[0-9a-fA-F]{32}$")


def derive_secret_from_uuid(config_uuid: str, salt: str = "spider-tg-proxy") -> str:
    """Return a 32-hex-character secret accepted by mtprotoproxy 1.0.6.

    The Python mtprotoproxy package expects the secret itself as 32 hex
    characters on the command line. Keep the user-facing link identical to
    the value passed to the proxy process.
    """
    return hashlib.sha256(f"{salt}:{config_uuid}".encode("utf-8")).hexdigest()[:32]


def validate_secret(secret: str) -> str:
    secret = str(secret or "").strip().lower()
    if not SECRET_RE.fullmatch(secret):
        raise ValueError("MTProxy secret must be exactly 32 hexadecimal characters")
    return secret


def is_docker_available() -> bool:
    # Kept only for compatibility with older main.py code. The MTProxy process
    # runs directly through the installed Python package, so Docker is not used.
    return False


def run_docker_telegram_proxy(*args, **kwargs):
    return None


def stop_docker_telegram_proxy(*args, **kwargs):
    return None


class MTProtoProxyServer:
    """Process wrapper around the maintained `mtprotoproxy` package.

    One instance is used per inbound. The official-style proxy process accepts
    a comma-separated secret list, so every Telegram user on the same inbound
    gets its own credential while sharing the same listener port.
    """

    def __init__(self, inbound_id: str, port: int, sni: str = "",
                 destination: str = "", server_name: str = ""):
        self.inbound_id = inbound_id
        self.port = int(port)
        self.sni = ""
        self.destination = ""
        self.server_name = ""
        self._secrets_map: Dict[str, dict] = {}
        self._process: Optional[asyncio.subprocess.Process] = None
        self._running = False
        self.on_traffic = None
        self.on_connection = None

    def update_secrets(self, secrets_map: dict):
        cleaned = {}
        for secret, info in (secrets_map or {}).items():
            try:
                cleaned[validate_secret(secret)] = dict(info or {})
            except Exception:
                logger.warning("Skipping invalid MTProxy secret for inbound %s", self.inbound_id)
        self._secrets_map = cleaned
        logger.info("[TG Proxy %s] Secrets updated: %d users", self.inbound_id, len(cleaned))

    def get_traffic(self) -> dict:
        # The maintained proxy process does not expose per-user byte counts
        # through this wrapper. Return an empty mapping rather than fabricating
        # values. The panel's user traffic accounting remains separate.
        return {}

    async def start(self):
        if self._running:
            return
        if not self._secrets_map:
            raise RuntimeError("No Telegram users/secrets are configured for this inbound")

        try:
            # CLI syntax supported by mtprotoproxy: <port> <secret1,secret2,...>
            secret_list = ",".join(self._secrets_map.keys())
            cmd = ["mtprotoproxy", str(self.port), secret_list]
            logger.info("[TG Proxy %s] starting: mtprotoproxy on internal port %s", self.inbound_id, self.port)
            self._process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.STDOUT,
            )
            self._running = True
            asyncio.create_task(self._watch_output())
            await asyncio.sleep(0.35)
            if self._process.returncode is not None:
                rc = self._process.returncode
                self._process = None
                self._running = False
                raise RuntimeError(f"mtprotoproxy exited immediately with code {rc}")
            logger.info("[TG Proxy %s] listening on internal port %s", self.inbound_id, self.port)
        except FileNotFoundError as exc:
            raise RuntimeError("mtprotoproxy is not installed; add it to requirements.txt") from exc

    async def _watch_output(self):
        proc = self._process
        if not proc or not proc.stdout:
            return
        try:
            while True:
                line = await proc.stdout.readline()
                if not line:
                    break
                logger.info("[TG Proxy %s] %s", self.inbound_id, line.decode(errors="replace").rstrip())
        except asyncio.CancelledError:
            pass
        except Exception as exc:
            logger.debug("Telegram proxy log watcher stopped: %s", exc)

    async def stop(self):
        self._running = False
        proc = self._process
        self._process = None
        if not proc:
            return
        if proc.returncode is None:
            try:
                proc.send_signal(signal.SIGTERM)
                await asyncio.wait_for(proc.wait(), timeout=3)
            except Exception:
                try:
                    proc.kill()
                except Exception:
                    pass
                try:
                    await proc.wait()
                except Exception:
                    pass
        logger.info("[TG Proxy %s] stopped", self.inbound_id)

    async def restart(self):
        await self.stop()
        await self.start()


# Backwards-compatible alias used by panel code.
