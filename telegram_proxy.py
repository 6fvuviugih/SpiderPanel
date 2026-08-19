# telegram_proxy.py — Telegram MTProto Proxy Server for Spider Panel
# ════════════════════════════════════════════════════════════════════════════════
# Supports both built-in Python MTProto proxy and official telegrammessenger/proxy Docker image.
# Each inbound gets its own proxy instance (Python or Docker) on its internal port.
# Per-user secrets identify users; traffic is forwarded to Telegram servers.
# ═══════════════════════════════════════════════════════════════════════════════

import asyncio
import hashlib
import logging
import secrets
import struct
import shutil
import subprocess
from typing import Callable, Optional

logger = logging.getLogger("Spider-TelegramProxy")

# Telegram datacenter IP ranges (DC1-DC5)
TELEGRAM_DC_RANGES = [
    ("149.154.160.0", 20),   # 149.154.160.0/20
    ("91.108.4.0", 22),      # 91.108.4.0/22
    ("91.108.56.0", 22),     # 91.108.56.0/22
    ("149.154.164.0", 22),   # 149.154.164.0/22
    ("185.76.151.0", 24),    # 185.76.151.0/24
]

# Default Telegram DC addresses for routing
TELEGRAM_DCS = {
    1: ("149.154.175.50", 443),
    2: ("149.154.167.51", 443),
    3: ("149.154.175.100", 443),
    4: ("149.154.167.91", 443),
    5: ("149.154.173.131", 443),
}

# Obfuscated protocol tag: 0xefefefef
OBFUSCATED_TAG = b"\xef\xef\xef\xef"

# Secret length in the handshake
SECRET_LEN = 16

# Proxy secret prefix byte (0xEE = default proxy, 0xDD = test DC proxy)
SECRET_PREFIX_DEFAULT = 0xEE
SECRET_PREFIX_TEST = 0xDD

# Max initial handshake size
HANDSHAKE_MAX = 64

# I/O buffer size
BUF_SIZE = 64 * 1024

# Connection timeout (seconds)
CONNECT_TIMEOUT = 10.0


def derive_secret_from_uuid(config_uuid: str, salt: str = "spider-tg-proxy") -> str:
    """Derive a deterministic 16-byte hex secret from a user's config UUID.

    The secret is stable across regenerations — same UUID always produces
    the same secret. The format is compatible with t.me/proxy links:
    32 hex chars (16 bytes), prefixed with 0xEE for default proxy type.
    """
    h = hashlib.sha256(f"{salt}:{config_uuid}".encode()).digest()
    # First byte is 0xEE (default proxy type), next 15 bytes from hash
    secret_bytes = bytes([SECRET_PREFIX_DEFAULT]) + h[:15]
    return secret_bytes.hex()


def is_telegram_dc(ip: str) -> bool:
    """Check if an IP belongs to Telegram datacenter ranges."""
    try:
        parts = [int(p) for p in ip.split(".")]
        if len(parts) != 4:
            return False
        ip_int = (parts[0] << 24) | (parts[1] << 16) | (parts[2] << 8) | parts[3]
        for base, prefix in TELEGRAM_DC_RANGES:
            base_parts = [int(p) for p in base.split(".")]
            base_int = (base_parts[0] << 24) | (base_parts[1] << 16) | (base_parts[2] << 8) | base_parts[3]
            mask = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF
            if (ip_int & mask) == (base_int & mask):
                return True
    except Exception:
        pass
    return False


def is_docker_available() -> bool:
    """Check if Docker is available on the system."""
    return shutil.which("docker") is not None


def get_docker_image() -> str:
    """Get the Docker image to use for Telegram proxy."""
    return "telegrammessenger/proxy:latest"


async def run_docker_telegram_proxy(
    container_name: str,
    port: int,
    secret: str,
    domain: str = "",
    proxy_tag: str = ""
) -> bool:
    """
    Start a Telegram proxy using the official telegrammessenger/proxy Docker image.

    Args:
        container_name: Name for the Docker container
        port: Port to expose (internal port)
        secret: 32-char hex secret for MTProto
        domain: Optional domain for the proxy
        proxy_tag: Optional proxy tag from @MTProxybot

    Returns:
        True if container started successfully, False otherwise
    """
    if not is_docker_available():
        logger.warning("Docker not available, cannot start Docker-based Telegram proxy")
        return False

    # Check if container already exists
    try:
        result = subprocess.run(
            ["docker", "ps", "-a", "--filter", f"name=^{container_name}$", "--format", "{{.Names}}"],
            capture_output=True, text=True, timeout=10
        )
        if container_name in result.stdout:
            # Container exists, remove it first
            subprocess.run(["docker", "rm", "-f", container_name], capture_output=True, timeout=10)
    except Exception as e:
        logger.warning(f"Failed to check/remove existing container: {e}")

    # Build docker run command
    cmd = [
        "docker", "run", "-d",
        "--name", container_name,
        "--restart", "unless-stopped",
        "-p", f"{port}:443",  # Map internal port 443 to host port
        "-e", f"SECRET={secret}",
    ]

    if domain:
        cmd.extend(["-e", f"DOMAIN={domain}"])

    # Add proxy tag if provided (for MTProxybot)
    # Note: The official image uses PROXY_TAG env var
    # We'll add it if provided

    cmd.append("telegrammessenger/proxy:latest")

    try:
        logger.info(f"Starting Docker Telegram proxy: {container_name} on port {port}")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            logger.error(f"Failed to start Docker container: {result.stderr}")
            return False
        logger.info(f"Docker Telegram proxy started: {container_name}")
        return True
    except subprocess.TimeoutExpired:
        logger.error("Docker run timed out")
        return False
    except Exception as e:
        logger.error(f"Failed to start Docker Telegram proxy: {e}")
        return False


async def stop_docker_telegram_proxy(container_name: str) -> bool:
    """Stop and remove a Docker Telegram proxy container."""
    if not is_docker_available():
        return False

    try:
        subprocess.run(["docker", "stop", container_name], capture_output=True, timeout=10)
        subprocess.run(["docker", "rm", container_name], capture_output=True, timeout=10)
        logger.info(f"Docker Telegram proxy stopped: {container_name}")
        return True
    except Exception as e:
        logger.error(f"Failed to stop Docker container: {e}")
        return False


async def check_docker_proxy_running(container_name: str) -> bool:
    """Check if a Docker Telegram proxy container is running."""
    if not is_docker_available():
        return False

    try:
        result = subprocess.run(
            ["docker", "ps", "--filter", f"name=^{container_name}$", "--format", "{{.Status}}"],
            capture_output=True, text=True, timeout=10
        )
        return "Up" in result.stdout
    except Exception:
        return False