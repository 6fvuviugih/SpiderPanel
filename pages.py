# pages.py — Spider Panel Enterprise Theme
# Exports: LOGIN_HTML, DASHBOARD_HTML, get_public_page_html()

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ورود · Spider Panel</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
:root {
  --spider-blue: #2B7FFF;
  --spider-purple: #7B61FF;
  --spider-red: #FF2352;
  --spider-success: #16A34A;
  --spider-warning: #F59E0B;
  --spider-danger: #DC2626;
  --text-primary: #0F172A;
  --text-secondary: #475569;
  --bg: #F8FAFC;
  --surface: #FFFFFF;
  --border: #E2E8F0;
  --shadow-sm: 0 1px 3px rgba(0,0,0,.06), 0 1px 2px rgba(0,0,0,.04);
  --shadow-md: 0 4px 12px rgba(0,0,0,.08), 0 2px 4px rgba(0,0,0,.04);
  --shadow-lg: 0 12px 40px rgba(0,0,0,.12), 0 4px 12px rgba(0,0,0,.06);
  --shadow-glow: 0 0 60px rgba(43,127,255,.15), 0 0 120px rgba(123,97,255,.08);
  --radius-sm: 12px;
  --radius: 18px;
  --radius-lg: 24px;
  --radius-xl: 28px;
}
[data-theme="dark"] {
  --text-primary: #F1F5F9;
  --text-secondary: #94A3B8;
  --bg: #0B1121;
  --surface: rgba(15,23,42,.8);
  --border: rgba(226,232,240,.08);
  --shadow-sm: 0 1px 3px rgba(0,0,0,.3);
  --shadow-md: 0 4px 16px rgba(0,0,0,.4);
  --shadow-lg: 0 16px 48px rgba(0,0,0,.5);
  --shadow-glow: 0 0 80px rgba(43,127,255,.2), 0 0 160px rgba(123,97,255,.12);
}
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%;overflow:hidden}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);display:flex;align-items:center;justify-content:center;padding:20px;transition:background .4s ease}
/* Background */
.bg-layer{position:fixed;inset:0;z-index:0;overflow:hidden}
.bg-orbs{position:absolute;inset:0}
.orb{position:absolute;border-radius:50%;filter:blur(120px);opacity:.5;animation:float 12s ease-in-out infinite}
.orb-1{width:500px;height:500px;background:var(--spider-blue);top:-200px;left:-100px;opacity:.18}
.orb-2{width:400px;height:400px;background:var(--spider-purple);bottom:-150px;right:-120px;opacity:.14;animation-delay:-6s}
.orb-3{width:350px;height:350px;background:var(--spider-red);top:40%;right:30%;opacity:.08;animation-delay:-3s}
@keyframes float{0%,100%{transform:translateY(0) scale(1)}33%{transform:translateY(-30px) scale(1.05)}66%{transform:translateY(20px) scale(.95)}}
/* Grid */
.grid-bg{position:fixed;inset:0;background-image:linear-gradient(rgba(43,127,255,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(43,127,255,.04) 1px,transparent 1px);background-size:50px 50px;z-index:0;opacity:.6}
/* Particles */
.particles{position:fixed;inset:0;z-index:1;pointer-events:none}
.particle{position:absolute;border-radius:50%;animation:drift linear infinite;opacity:0}
.particle:nth-child(1){width:3px;height:3px;background:var(--spider-blue);top:20%;left:15%;animation-duration:14s;opacity:.5}
.particle:nth-child(2){width:2px;height:2px;background:var(--spider-purple);top:60%;left:25%;animation-duration:18s;animation-delay:-5s;opacity:.4}
.particle:nth-child(3){width:4px;height:4px;background:var(--spider-red);top:30%;left:70%;animation-duration:16s;animation-delay:-8s;opacity:.35}
.particle:nth-child(4){width:2px;height:2px;background:var(--spider-blue);top:75%;left:55%;animation-duration:20s;animation-delay:-2s;opacity:.45}
.particle:nth-child(5){width:3px;height:3px;background:var(--spider-purple);top:10%;left:45%;animation-duration:15s;animation-delay:-11s;opacity:.3}
.particle:nth-child(6){width:2px;height:2px;background:var(--spider-red);top:85%;left:80%;animation-duration:22s;animation-delay:-7s;opacity:.4}
.particle:nth-child(7){width:3px;height:3px;background:var(--spider-blue);top:45%;left:35%;animation-duration:17s;animation-delay:-4s;opacity:.35}
.particle:nth-child(8){width:2px;height:2px;background:var(--spider-purple);top:55%;left:65%;animation-duration:19s;animation-delay:-9s;opacity:.3}
@keyframes drift{0%{transform:translate(0,0) scale(1);opacity:0}10%{opacity:1}90%{opacity:1}100%{transform:translate(60px,-80px) scale(.3);opacity:0}}
/* Login Card */
.login-wrap{position:relative;z-index:10;width:100%;max-width:440px}
.login-card{background:rgba(255,255,255,.8);backdrop-filter:blur(24px) saturate(180%);-webkit-backdrop-filter:blur(24px) saturate(180%);border:1px solid rgba(255,255,255,.3);border-radius:var(--radius-xl);padding:44px 36px 38px;box-shadow:var(--shadow-lg),var(--shadow-glow);position:relative;overflow:hidden;transition:all .3s ease}
[data-theme="dark"] .login-card{background:rgba(15,23,42,.75);border-color:rgba(255,255,255,.06)}
.login-card::before{content:'';position:absolute;top:0;right:0;width:200px;height:200px;background:radial-gradient(circle,rgba(43,127,255,.08),transparent 70%);pointer-events:none}
.login-card::after{content:'';position:absolute;bottom:0;left:0;width:180px;height:180px;background:radial-gradient(circle,rgba(123,97,255,.08),transparent 70%);pointer-events:none}
/* Spider Logo */
.spider-logo{display:flex;align-items:center;justify-content:center;margin-bottom:28px;position:relative;z-index:1}
.spider-svg{width:80px;height:80px;filter:drop-shadow(0 4px 12px rgba(43,127,255,.3))}
.spider-body{fill:url(#spider-body-grad)}
.spider-leg{fill:none;stroke:url(#spider-leg-grad);stroke-width:3;stroke-linecap:round;animation:legPulse 2s ease-in-out infinite}
.spider-leg:nth-child(even){animation-delay:-1s}
@keyframes legPulse{0%,100%{stroke-width:3}50%{stroke-width:4.5}}
.login-title{text-align:center;font-size:28px;font-weight:800;margin-bottom:6px;letter-spacing:-.02em;position:relative;z-index:1}
.login-title .gradient-text{background:linear-gradient(90deg,var(--spider-blue),var(--spider-purple),var(--spider-red));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.login-sub{text-align:center;font-size:13px;color:var(--text-secondary);margin-bottom:28px;position:relative;z-index:1;line-height:1.6}
/* Password field */
.field-group{position:relative;z-index:1;margin-bottom:20px}
.field-label{font-size:11px;font-weight:700;color:var(--text-secondary);margin-bottom:8px;text-transform:uppercase;letter-spacing:.06em;display:flex;align-items:center;gap:6px}
.field-label i{font-size:13px;color:var(--spider-purple)}
.input-wrap{position:relative}
.input-wrap input{width:100%;padding:14px 48px 14px 48px;border-radius:var(--radius);border:1.5px solid var(--border);background:rgba(255,255,255,.6);backdrop-filter:blur(8px);color:var(--text-primary);font-family:'Vazirmatn',sans-serif;font-size:14px;outline:none;transition:all .3s ease}
[data-theme="dark"] .input-wrap input{background:rgba(15,23,42,.6);color:var(--text-primary)}
.input-wrap input:focus{border-color:var(--spider-blue);background:rgba(255,255,255,.9);box-shadow:0 0 0 4px rgba(43,127,255,.1)}
[data-theme="dark"] .input-wrap input:focus{background:rgba(15,23,42,.8);box-shadow:0 0 0 4px rgba(43,127,255,.15)}
.input-icon{position:absolute;right:16px;top:50%;transform:translateY(-50%);color:var(--text-secondary);font-size:18px;pointer-events:none;transition:color .3s}
input:focus ~ .input-icon{color:var(--spider-blue)}
.eye-toggle{position:absolute;left:10px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--text-secondary);cursor:pointer;font-size:17px;padding:6px;display:flex;align-items:center;transition:color .3s;border-radius:8px}
.eye-toggle:hover{color:var(--spider-purple);background:rgba(123,97,255,.08)}
/* Error */
.error-msg{display:none;align-items:center;gap:8px;background:rgba(255,35,82,.08);border:1px solid rgba(255,35,82,.2);border-radius:var(--radius-sm);padding:11px 14px;margin-bottom:18px;color:var(--spider-danger);font-size:12px;position:relative;z-index:1}
.error-msg.show{display:flex}
.error-msg i{font-size:16px;flex-shrink:0}
/* Hint */
.login-hint{display:flex;align-items:center;justify-content:space-between;gap:10px;background:rgba(43,127,255,.06);border:1px solid rgba(43,127,255,.15);border-radius:var(--radius-sm);padding:11px 16px;margin-bottom:20px;position:relative;z-index:1}
.hint-label{font-size:11px;color:var(--text-secondary);font-weight:500}
.hint-value{font-family:'Inter',monospace;font-size:14px;font-weight:700;color:var(--spider-blue);background:rgba(43,127,255,.1);border:1px solid rgba(43,127,255,.2);padding:4px 14px;border-radius:10px;cursor:pointer;transition:all .2s ease;letter-spacing:.06em}
.hint-value:hover{background:rgba(43,127,255,.18);transform:translateY(-1px)}
/* Submit button */
.login-btn{width:100%;height:60px;border:none;border-radius:var(--radius);cursor:pointer;position:relative;z-index:1;font-family:'Vazirmatn',sans-serif;font-size:15px;font-weight:700;color:#fff;overflow:hidden;transition:all .3s ease;display:flex;align-items:center;justify-content:center;gap:8px}
.login-btn::before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,var(--spider-blue),var(--spider-purple),var(--spider-red));transition:opacity .3s}
.login-btn::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,var(--spider-red),var(--spider-purple),var(--spider-blue));opacity:0;transition:opacity .3s}
.login-btn:hover::after{opacity:1}
.login-btn:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(43,127,255,.3),0 4px 12px rgba(123,97,255,.2)}
.login-btn:active{transform:translateY(0) scale(.98)}
.login-btn:disabled{opacity:.5;cursor:not-allowed;transform:none}
.login-btn span{position:relative;z-index:1;display:flex;align-items:center;gap:8px}
/* Loading spinner */
.spinner{width:18px;height:18px;border:2px solid rgba(255,255,255,.3);border-top-color:#fff;border-radius:50%;animation:spin .7s linear infinite;display:none}
.btn-loading .spinner{display:inline-block}
.btn-loading .btn-text{display:none}
@keyframes spin{to{transform:rotate(360deg)}}
/* Footer */
.login-footer{text-align:center;margin-top:24px;position:relative;z-index:1;font-size:11px;color:var(--text-secondary)}
.login-footer .dot{width:5px;height:5px;border-radius:50%;background:var(--spider-purple);display:inline-block;margin:0 6px}
/* Responsive */
@media(max-width:480px){
  .login-card{padding:32px 24px 30px}
  .login-title{font-size:24px}
  .spider-svg{width:64px;height:64px}
}
</style>
</head>
<body data-theme="light">
<div class="bg-layer">
  <div class="bg-orbs"><div class="orb orb-1"></div><div class="orb orb-2"></div><div class="orb orb-3"></div></div>
</div>
<div class="grid-bg"></div>
<div class="particles">
  <div class="particle"></div><div class="particle"></div><div class="particle"></div>
  <div class="particle"></div><div class="particle"></div><div class="particle"></div>
  <div class="particle"></div><div class="particle"></div>
</div>
<div class="login-wrap">
  <div class="login-card">
    <div class="spider-logo">
      <svg class="spider-svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="spider-body-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#2B7FFF"/>
            <stop offset="50%" style="stop-color:#7B61FF"/>
            <stop offset="100%" style="stop-color:#FF2352"/>
          </linearGradient>
          <linearGradient id="spider-leg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#2B7FFF"/>
            <stop offset="100%" style="stop-color:#7B61FF"/>
          </linearGradient>
        </defs>
        <!-- Legs -->
        <path class="spider-leg" d="M50,50 L10,15"/>
        <path class="spider-leg" d="M50,50 L15,50"/>
        <path class="spider-leg" d="M50,50 L10,85"/>
        <path class="spider-leg" d="M50,50 L90,15"/>
        <path class="spider-leg" d="M50,50 L85,50"/>
        <path class="spider-leg" d="M50,50 L90,85"/>
        <path class="spider-leg" d="M50,50 L30,5"/>
        <path class="spider-leg" d="M50,50 L70,5"/>
        <!-- Body -->
        <ellipse class="spider-body" cx="50" cy="46" rx="18" ry="22"/>
        <!-- Head -->
        <ellipse class="spider-body" cx="50" cy="23" rx="12" ry="10"/>
        <!-- Eyes -->
        <circle cx="44" cy="20" r="3" fill="#fff"/>
        <circle cx="56" cy="20" r="3" fill="#fff"/>
        <circle cx="44.5" cy="19.5" r="1.2" fill="#1a1a2e"/>
        <circle cx="56.5" cy="19.5" r="1.2" fill="#1a1a2e"/>
      </svg>
    </div>
    <div class="login-title">
      <span class="gradient-text">SPIDER PANEL</span>
    </div>
    <div class="login-sub">به پنل مدیریت خوش آمدید<br>برای ادامه رمز عبور را وارد کنید</div>
    <div class="error-msg" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <div class="login-hint">
      <span class="hint-label"><i class="ti ti-key"></i> رمز پیش‌فرض</span>
      <span class="hint-value" onclick="document.getElementById('pw').value='123456';document.getElementById('pw').focus()">123456</span>
    </div>
    <form id="form">
      <div class="field-group">
        <div class="field-label"><i class="ti ti-lock"></i> رمز عبور</div>
        <div class="input-wrap">
          <input type="password" id="pw" placeholder="••••••••" autofocus required>
          <i class="ti ti-lock input-icon"></i>
          <button type="button" class="eye-toggle" id="eye-btn" title="نمایش رمز">
            <i class="ti ti-eye"></i>
          </button>
        </div>
      </div>
      <button type="submit" class="login-btn" id="btn">
        <span class="spinner"></span>
        <span class="btn-text"><i class="ti ti-login-2"></i> ورود به داشبورد</span>
      </button>
    </form>
    <div class="login-footer">
      <span class="dot"></span>
      Spider Gateway · Spider Panel
      <span class="dot"></span>
    </div>
  </div>
</div>
<script>
(function(){
  var d=document.documentElement;
  var saved=localStorage.getItem('spider-theme')||'light';
  d.setAttribute('data-theme',saved);
  // Eye toggle
  var pw=document.getElementById('pw'),eye=document.getElementById('eye-btn'),eyeIcon=eye.querySelector('i');
  eye.onclick=function(){
    var show=pw.type==='password';
    pw.type=show?'text':'password';
    eyeIcon.className='ti '+(show?'ti-eye-off':'ti-eye');
  };
  // Login form
  document.getElementById('form').addEventListener('submit',async function(e){
    e.preventDefault();
    var btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('err-text');
    err.classList.remove('show');btn.disabled=true;btn.classList.add('btn-loading');
    try{
      var r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:pw.value})});
      if(!r.ok){var d=await r.json().catch(function(){return{}});throw new Error(d.detail||'خطا در ورود');}
      location.href='/dashboard';
    }catch(ex){
      et.textContent=ex.message;err.classList.add('show');
      btn.disabled=false;btn.classList.remove('btn-loading');
    }
  });
})();
</script>
</body></html>"""

DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Spider Panel · داشبورد</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
/* ============================================================
   CSS VARIABLES — ۴ تم مختلف
   ============================================================ */
:root {
  /* تم اصلی (نئون/سایبر) */
  --spider-blue: #2B7FFF;
  --spider-purple: #7B61FF;
  --spider-red: #FF2352;
  --spider-cyan: #00F5FF;
  --spider-gold: #FFD700;
  --spider-pink: #FF2D95;
  --spider-green: #00FF88;

  --text-primary: #0F172A;
  --text-secondary: #475569;
  --bg: #F8FAFC;
  --surface: rgba(255, 255, 255, 0.75);
  --surface-glass: rgba(255, 255, 255, 0.6);
  --surface-solid: #FFFFFF;
  --border: rgba(226, 232, 240, 0.6);
  --border-solid: #E2E8F0;

  --gradient-main: linear-gradient(135deg, #2B7FFF, #7B61FF, #FF2352);
  --gradient-blue: linear-gradient(135deg, #2B7FFF, #00F5FF);
  --gradient-purple: linear-gradient(135deg, #7B61FF, #FF2D95);
  --gradient-gold: linear-gradient(135deg, #FFD700, #FF6B00);
  --gradient-green: linear-gradient(135deg, #00FF88, #00B4D8);
  --gradient-red: linear-gradient(135deg, #FF2352, #FF6B35);
  --gradient-cyan: linear-gradient(135deg, #00F5FF, #2B7FFF);

  --shadow-sm: 0 1px 3px rgba(0,0,0,0.04);
  --shadow-md: 0 4px 16px rgba(0,0,0,0.06);
  --shadow-lg: 0 12px 40px rgba(0,0,0,0.08);
  --shadow-xl: 0 20px 60px rgba(0,0,0,0.1);
  --shadow-glow: 0 0 40px rgba(43,127,255,0.15), 0 0 80px rgba(123,97,255,0.08);

  --radius-sm: 10px;
  --radius: 16px;
  --radius-lg: 22px;
  --radius-xl: 28px;
  --radius-full: 9999px;

  --sidebar-w: 72px;
  --sidebar-w-expanded: 240px;
  --topbar-h: 70px;
  --transition: 0.35s cubic-bezier(0.4, 0, 0.2, 1);

  --font: 'Vazirmatn', sans-serif;
  --font-mono: 'Inter', monospace;
}

/* تم تاریک — نسخه ارتقا یافته */
[data-theme="dark"] {
  --text-primary: #F1F5F9;
  --text-secondary: #94A3B8;
  --bg: #0A0A1A;
  --surface: rgba(15, 23, 42, 0.7);
  --surface-glass: rgba(15, 23, 42, 0.5);
  --surface-solid: #1A1A2E;
  --border: rgba(226, 232, 240, 0.06);
  --border-solid: rgba(226, 232, 240, 0.08);
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.3);
  --shadow-md: 0 4px 16px rgba(0,0,0,0.4);
  --shadow-lg: 0 12px 40px rgba(0,0,0,0.5);
  --shadow-xl: 0 20px 60px rgba(0,0,0,0.6);
  --shadow-glow: 0 0 60px rgba(43,127,255,0.15), 0 0 120px rgba(123,97,255,0.08);
}

/* تم طلایی/لوکس */
[data-theme="gold"] {
  --spider-blue: #C9A96E;
  --spider-purple: #D4AF37;
  --spider-red: #B8860B;
  --spider-cyan: #D4AF37;
  --spider-gold: #FFD700;
  --spider-pink: #D4AF37;
  --spider-green: #C9A96E;

  --text-primary: #1A1208;
  --text-secondary: #6B5B3A;
  --bg: #FDF8F0;
  --surface: rgba(255, 248, 240, 0.8);
  --surface-glass: rgba(255, 248, 240, 0.6);
  --surface-solid: #FFF8F0;
  --border: rgba(212, 175, 55, 0.25);
  --border-solid: #E8D5B0;

  --gradient-main: linear-gradient(135deg, #C9A96E, #D4AF37, #B8860B);
  --gradient-blue: linear-gradient(135deg, #C9A96E, #D4AF37);
  --gradient-purple: linear-gradient(135deg, #D4AF37, #B8860B);
  --gradient-gold: linear-gradient(135deg, #FFD700, #C9A96E);
}

/* تم پاستیل/شیرین */
[data-theme="pastel"] {
  --spider-blue: #A8D8EA;
  --spider-purple: #D4A5D4;
  --spider-red: #FFB3B3;
  --spider-cyan: #A8D8EA;
  --spider-gold: #F7DC6F;
  --spider-pink: #FFB3C6;
  --spider-green: #A8E6CF;

  --text-primary: #3D2C3D;
  --text-secondary: #7A6A7A;
  --bg: #FFF5F7;
  --surface: rgba(255, 245, 247, 0.85);
  --surface-glass: rgba(255, 245, 247, 0.7);
  --surface-solid: #FFF5F7;
  --border: rgba(200, 180, 200, 0.25);

  --gradient-main: linear-gradient(135deg, #A8D8EA, #D4A5D4, #FFB3B3);
  --gradient-blue: linear-gradient(135deg, #A8D8EA, #B5EAD7);
  --gradient-purple: linear-gradient(135deg, #D4A5D4, #FFB3C6);
  --gradient-gold: linear-gradient(135deg, #F7DC6F, #FFD3B4);
}

/* تم نئون/سایبر — پیش‌فرض */
[data-theme="neon"] {
  --spider-blue: #00F5FF;
  --spider-purple: #FF2D95;
  --spider-red: #FF0055;
  --spider-cyan: #00F5FF;
  --spider-gold: #FFD700;
  --spider-pink: #FF2D95;
  --spider-green: #00FF88;

  --text-primary: #FFFFFF;
  --text-secondary: #94A3B8;
  --bg: #0A0A1A;
  --surface: rgba(0, 0, 0, 0.6);
  --surface-glass: rgba(0, 0, 0, 0.4);
  --surface-solid: #1A1A2E;
  --border: rgba(0, 245, 255, 0.15);
  --border-solid: rgba(0, 245, 255, 0.1);

  --gradient-main: linear-gradient(135deg, #00F5FF, #FF2D95, #FF0055);
  --gradient-blue: linear-gradient(135deg, #00F5FF, #00FF88);
  --gradient-purple: linear-gradient(135deg, #FF2D95, #FF0055);
  --gradient-gold: linear-gradient(135deg, #FFD700, #FF6B00);
  --shadow-glow: 0 0 60px rgba(0, 245, 255, 0.2), 0 0 120px rgba(255, 45, 149, 0.1);
}

/* ============================================================
   RESET & BASE
   ============================================================ */
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { height: 100%; }
body {
  font-family: var(--font);
  background: var(--bg);
  color: var(--text-primary);
  min-height: 100vh;
  display: flex;
  transition: background var(--transition), color var(--transition);
  overflow-x: hidden;
  font-size: 14px;
  line-height: 1.6;
}
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(43,127,255,0.2); border-radius: 2px; }
::-webkit-scrollbar-thumb:hover { background: rgba(43,127,255,0.4); }
a { color: inherit; text-decoration: none; }
button { font-family: inherit; cursor: pointer; }

/* ============================================================
   BACKGROUND PARTICLES (تعاملی با ماوس)
   ============================================================ */
.bg-particles {
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  overflow: hidden;
}
.particle-bg {
  position: absolute;
  border-radius: 50%;
  background: var(--spider-blue);
  opacity: 0.03;
  transition: transform 0.1s ease-out;
}
.particle-bg:nth-child(1) { width: 300px; height: 300px; top: -100px; left: -100px; background: var(--spider-blue); }
.particle-bg:nth-child(2) { width: 250px; height: 250px; bottom: -80px; right: -80px; background: var(--spider-purple); opacity: 0.02; }
.particle-bg:nth-child(3) { width: 200px; height: 200px; top: 50%; right: 20%; background: var(--spider-red); opacity: 0.015; }

/* ============================================================
   SIDEBAR — جمع‌شونده
   ============================================================ */
.sidebar {
  width: var(--sidebar-w);
  min-height: 100vh;
  background: var(--surface-glass);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border-left: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  position: fixed;
  right: 0;
  top: 0;
  bottom: 0;
  z-index: 200;
  transition: width var(--transition), background var(--transition), border-color var(--transition);
  box-shadow: var(--shadow-sm);
  overflow: hidden;
}
.sidebar:hover { width: var(--sidebar-w-expanded); }
.sidebar:hover .nav-label { opacity: 1; width: auto; }
.sidebar:hover .sidebar-logo-text { opacity: 1; }
.sidebar:hover .sidebar-user-name { opacity: 1; }
.sidebar:hover .sidebar-user-role { opacity: 1; }
.sidebar:hover .sidebar-footer .theme-btn span { opacity: 1; width: auto; }
.sidebar:hover .sidebar-footer .logout-btn span { opacity: 1; width: auto; }

.sidebar-logo {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 18px 14px 16px;
  border-bottom: 1px solid var(--border);
  flex-shrink: 0;
  min-height: 70px;
}
.sidebar-logo svg { width: 36px; height: 36px; flex-shrink: 0; filter: drop-shadow(0 2px 12px rgba(43,127,255,0.3)); }
.sidebar-logo-text {
  font-size: 15px; font-weight: 800; color: var(--text-primary);
  opacity: 0; width: 0; white-space: nowrap; overflow: hidden;
  transition: opacity 0.3s ease 0.1s, width 0.3s ease;
}
.sidebar-logo-sub {
  font-size: 8px; color: var(--text-secondary); opacity: 0.6;
  display: block; margin-top: 1px;
}

.sidebar-nav {
  flex: 1;
  overflow-y: auto;
  padding: 6px 6px;
}
.nav-section {
  padding: 14px 14px 6px;
  font-size: 8px;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--text-secondary);
  opacity: 0.4;
  white-space: nowrap;
}
.nav-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  color: var(--text-secondary);
  font-size: 12px;
  font-weight: 500;
  cursor: pointer;
  border-right: 2px solid transparent;
  transition: all 0.2s;
  margin: 1px 4px;
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
  position: relative;
  white-space: nowrap;
}
.nav-item i { font-size: 17px; width: 22px; text-align: center; flex-shrink: 0; }
.nav-label { opacity: 0; width: 0; overflow: hidden; transition: opacity 0.3s ease 0.1s, width 0.3s ease; }
.sidebar:hover .nav-label { opacity: 1; width: auto; }
.nav-item:hover { background: rgba(43,127,255,0.06); color: var(--text-primary); }
.nav-item.active {
  background: linear-gradient(135deg, rgba(123,97,255,0.12), rgba(43,127,255,0.08));
  color: var(--spider-purple);
  border-right-color: var(--spider-purple);
  font-weight: 700;
}
.nav-item.active i { color: var(--spider-purple); }
.nav-badge {
  margin-right: auto;
  background: rgba(43,127,255,0.12);
  color: var(--spider-blue);
  font-size: 8px;
  padding: 2px 7px;
  border-radius: 20px;
  font-weight: 700;
  flex-shrink: 0;
}
.nav-tooltip {
  display: none;
  position: absolute;
  right: 60px;
  top: 50%;
  transform: translateY(-50%);
  background: var(--surface-solid);
  color: var(--text-primary);
  padding: 4px 12px;
  border-radius: var(--radius-sm);
  font-size: 11px;
  font-weight: 600;
  box-shadow: var(--shadow-md);
  border: 1px solid var(--border);
  white-space: nowrap;
  pointer-events: none;
  z-index: 300;
}
.sidebar:not(:hover) .nav-item:hover .nav-tooltip { display: block; }

.sidebar-footer {
  padding: 12px 12px;
  border-top: 1px solid var(--border);
  flex-shrink: 0;
}
.sidebar-user {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
  padding: 0 4px;
}
.sidebar-avatar {
  width: 36px; height: 36px;
  border-radius: var(--radius-sm);
  background: var(--gradient-main);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 15px;
  flex-shrink: 0;
  box-shadow: 0 4px 12px rgba(123,97,255,0.25);
}
.sidebar-user-name {
  font-size: 12px; font-weight: 700; color: var(--text-primary);
  opacity: 0; width: 0; overflow: hidden; white-space: nowrap;
  transition: opacity 0.3s ease 0.1s, width 0.3s ease;
}
.sidebar-user-role {
  font-size: 8px; color: var(--text-secondary);
  opacity: 0; width: 0; overflow: hidden; white-space: nowrap;
  transition: opacity 0.3s ease 0.15s, width 0.3s ease;
}
.sidebar-footer .theme-btn,
.sidebar-footer .logout-btn {
  display: flex;
  align-items: center;
  gap: 7px;
  width: 100%;
  padding: 8px 10px;
  border: none;
  border-radius: var(--radius-sm);
  font-family: var(--font);
  font-size: 11px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  background: rgba(43,127,255,0.04);
  color: var(--text-secondary);
  border: 1px solid var(--border);
  overflow: hidden;
}
.sidebar-footer .theme-btn:hover { background: rgba(43,127,255,0.1); color: var(--text-primary); }
.sidebar-footer .theme-btn i { font-size: 14px; flex-shrink: 0; }
.sidebar-footer .theme-btn span { opacity: 0; width: 0; overflow: hidden; white-space: nowrap; transition: opacity 0.3s ease 0.1s, width 0.3s ease; }
.sidebar:hover .sidebar-footer .theme-btn span { opacity: 1; width: auto; }

.logout-btn {
  background: rgba(255,35,82,0.04) !important;
  color: var(--spider-red) !important;
  margin-top: 4px;
}
.logout-btn:hover { background: rgba(255,35,82,0.1) !important; }
.logout-btn span { opacity: 0; width: 0; overflow: hidden; white-space: nowrap; transition: opacity 0.3s ease 0.1s, width 0.3s ease; }
.sidebar:hover .logout-btn span { opacity: 1; width: auto; }

/* ============================================================
   MOBILE TOP BAR
   ============================================================ */
.mobile-top {
  display: none;
  position: fixed;
  top: 0; right: 0; left: 0;
  height: 60px;
  background: var(--surface-glass);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  z-index: 150;
  align-items: center;
  justify-content: space-between;
  padding: 0 14px;
}
.mobile-brand { display: flex; align-items: center; gap: 9px; }
.mobile-brand svg { width: 28px; height: 28px; }
.mobile-brand span { font-size: 13px; font-weight: 700; color: var(--text-primary); }
.mobile-actions { display: flex; gap: 6px; }
.mob-btn {
  background: rgba(43,127,255,0.04);
  border: 1px solid var(--border);
  color: var(--text-secondary);
  width: 36px; height: 36px;
  border-radius: 10px;
  font-size: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
.overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.5);
  z-index: 190;
  backdrop-filter: blur(4px);
}
.overlay.show { display: block; }

/* ============================================================
   MAIN CONTENT
   ============================================================ */
.main {
  margin-right: var(--sidebar-w);
  flex: 1;
  padding: 20px 28px 40px;
  min-width: 0;
  transition: margin var(--transition);
  position: relative;
  z-index: 1;
}
.page { display: none; animation: fadeIn 0.35s ease; }
.page.active { display: block; }
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(12px); }
  to { opacity: 1; transform: translateY(0); }
}

/* ============================================================
   TOPBAR
   ============================================================ */
.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
  flex-wrap: wrap;
  gap: 12px;
}
.topbar-left {
  display: flex;
  align-items: center;
  gap: 14px;
}
.topbar-title {
  font-size: 22px;
  font-weight: 900;
  color: var(--text-primary);
  display: flex;
  align-items: center;
  gap: 8px;
  letter-spacing: -0.02em;
}
.topbar-title i { color: var(--spider-blue); font-size: 22px; }
.topbar-sub {
  font-size: 11px;
  color: var(--text-secondary);
  margin-top: 2px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.topbar-sub .dot-online {
  width: 6px; height: 6px;
  border-radius: 50%;
  background: var(--spider-green);
  display: inline-block;
  animation: pulse-dot 1.5s ease-in-out infinite;
}
@keyframes pulse-dot { 0%,100% { opacity: 1; } 50% { opacity: 0.3; } }

.topbar-right {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}
.theme-selector {
  display: flex;
  gap: 4px;
  background: var(--surface-glass);
  border: 1px solid var(--border);
  border-radius: var(--radius-full);
  padding: 4px;
}
.theme-dot {
  width: 28px; height: 28px;
  border-radius: 50%;
  border: 2px solid transparent;
  cursor: pointer;
  transition: all 0.2s;
}
.theme-dot:hover { transform: scale(1.15); }
.theme-dot.active { border-color: var(--text-primary); box-shadow: 0 0 20px rgba(43,127,255,0.2); }
.theme-dot.dark { background: #0A0A1A; }
.theme-dot.light { background: #F8FAFC; }
.theme-dot.gold { background: #C9A96E; }
.theme-dot.pastel { background: #FFB3C6; }
.theme-dot.neon { background: #00F5FF; }

.bell-btn {
  width: 38px; height: 38px;
  border-radius: var(--radius-sm);
  background: rgba(43,127,255,0.04);
  border: 1px solid var(--border);
  color: var(--text-secondary);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 17px;
  transition: all 0.2s;
  position: relative;
}
.bell-btn:hover { background: rgba(43,127,255,0.08); color: var(--spider-blue); }
.bell-btn::after {
  content: '';
  position: absolute;
  top: 8px; left: 8px;
  width: 7px; height: 7px;
  border-radius: 50%;
  background: var(--spider-red);
  border: 2px solid var(--surface-solid);
}

.btn {
  font-family: var(--font);
  font-size: 12px;
  font-weight: 700;
  border-radius: var(--radius);
  padding: 10px 20px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  border: none;
  transition: all 0.25s;
  white-space: nowrap;
}
.btn i { font-size: 14px; }
.btn-primary {
  background: var(--gradient-main);
  color: #fff;
  box-shadow: 0 4px 20px rgba(43,127,255,0.2);
}
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 30px rgba(43,127,255,0.3); }
.btn-primary:active { transform: translateY(0); }
.btn-ghost {
  background: rgba(43,127,255,0.04);
  color: var(--spider-blue);
  border: 1px solid rgba(43,127,255,0.12);
}
.btn-ghost:hover { background: rgba(43,127,255,0.08); }
.btn-danger {
  background: rgba(255,35,82,0.04);
  color: var(--spider-red);
  border: 1px solid rgba(255,35,82,0.12);
}
.btn-danger:hover { background: rgba(255,35,82,0.08); }
.btn-sm { padding: 6px 12px; font-size: 10.5px; border-radius: var(--radius-sm); }
.btn-icon { width: 32px; height: 32px; padding: 0; justify-content: center; border-radius: var(--radius-sm); }
.btn-success {
  background: rgba(0, 255, 136, 0.08);
  color: var(--spider-green);
  border: 1px solid rgba(0, 255, 136, 0.15);
}
.btn-success:hover { background: rgba(0, 255, 136, 0.15); }

/* ============================================================
   BADGES
   ============================================================ */
.badge {
  font-size: 9px;
  padding: 3px 10px;
  border-radius: 20px;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  white-space: nowrap;
}
.badge-blue { background: rgba(43,127,255,0.08); color: var(--spider-blue); }
.badge-green { background: rgba(0,255,136,0.08); color: var(--spider-green); }
.badge-red { background: rgba(255,35,82,0.08); color: var(--spider-red); }
.badge-purple { background: rgba(123,97,255,0.08); color: var(--spider-purple); }
.badge-gold { background: rgba(255,215,0,0.08); color: var(--spider-gold); }
.dot {
  width: 6px; height: 6px;
  border-radius: 50%;
  flex-shrink: 0;
  display: inline-block;
}
.dot-green { background: var(--spider-green); }
.dot-red { background: var(--spider-red); }
.dot-blue { background: var(--spider-blue); }
.dot-gold { background: var(--spider-gold); }
.pulse { animation: pulse-dot 1.5s ease-in-out infinite; }

/* ============================================================
   STATS CARDS — با گرادیان و آیکون بزرگ
   ============================================================ */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  margin-bottom: 20px;
}
.stat-card {
  background: var(--surface-glass);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 20px 18px 18px;
  transition: all var(--transition);
  position: relative;
  overflow: hidden;
  cursor: default;
}
.stat-card::before {
  content: '';
  position: absolute;
  top: 0; right: 0;
  width: 100%; height: 4px;
  background: var(--gradient-main);
  opacity: 0.6;
  transition: height 0.3s;
}
.stat-card:hover { transform: translateY(-4px); border-color: rgba(43,127,255,0.2); box-shadow: var(--shadow-hover); }
.stat-card:hover::before { height: 6px; }

.stat-card .stat-icon {
  width: 48px; height: 48px;
  border-radius: var(--radius);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  margin-bottom: 10px;
}
.stat-icon.blue { background: rgba(43,127,255,0.1); color: var(--spider-blue); }
.stat-icon.purple { background: rgba(123,97,255,0.1); color: var(--spider-purple); }
.stat-icon.green { background: rgba(0,255,136,0.1); color: var(--spider-green); }
.stat-icon.red { background: rgba(255,35,82,0.1); color: var(--spider-red); }
.stat-icon.gold { background: rgba(255,215,0,0.1); color: var(--spider-gold); }
.stat-icon.cyan { background: rgba(0,245,255,0.1); color: var(--spider-cyan); }

.stat-label {
  font-size: 10px;
  font-weight: 700;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: 4px;
}
.stat-value {
  font-size: 28px;
  font-weight: 900;
  color: var(--text-primary);
  line-height: 1.1;
  letter-spacing: -0.02em;
}
.stat-sub {
  font-size: 10px;
  color: var(--text-secondary);
  margin-top: 6px;
  display: flex;
  align-items: center;
  gap: 4px;
}
.stat-sub.up { color: var(--spider-green); }
.stat-sub.down { color: var(--spider-red); }

/* شمارنده انیمیشنی */
.counter-value {
  display: inline-block;
  transition: all 0.3s;
}

/* ============================================================
   QUICK ACTIONS — با آیکون‌های بزرگ و برچسب
   ============================================================ */
.quick-actions {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin-bottom: 20px;
}
.qa-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 16px 12px;
  border-radius: var(--radius);
  border: 1px solid var(--border);
  background: var(--surface-glass);
  backdrop-filter: blur(12px);
  color: var(--text-primary);
  font-family: var(--font);
  font-size: 11px;
  font-weight: 600;
  cursor: pointer;
  transition: all var(--transition);
  text-align: center;
}
.qa-btn i {
  font-size: 26px;
  transition: transform 0.3s;
}
.qa-btn:hover {
  background: var(--gradient-main);
  color: #fff;
  border-color: transparent;
  box-shadow: 0 8px 30px rgba(43,127,255,0.2);
  transform: translateY(-3px);
}
.qa-btn:hover i { transform: scale(1.15) rotate(-5deg); }

/* ============================================================
   SERVER INFO — دایره‌ای
   ============================================================ */
.server-panel {
  background: var(--surface-glass);
  backdrop-filter: blur(16px);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 22px 24px 20px;
  margin-bottom: 20px;
}
.server-title {
  font-size: 14px;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.server-title i { color: var(--spider-blue); font-size: 17px; }

.server-circular {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}
.srv-circle {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
}
.srv-circle canvas {
  width: 80px;
  height: 80px;
}
.srv-circle-label {
  font-size: 10px;
  font-weight: 700;
  color: var(--text-secondary);
}
.srv-circle-value {
  font-size: 13px;
  font-weight: 800;
  color: var(--text-primary);
}

/* ============================================================
   TABLE
   ============================================================ */
.table-wrap {
  background: var(--surface-glass);
  backdrop-filter: blur(16px);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
}
.table-wrap table {
  width: 100%;
  border-collapse: collapse;
}
.table-wrap th {
  background: rgba(43,127,255,0.03);
  font-size: 9.5px;
  font-weight: 800;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  padding: 12px 14px;
  text-align: right;
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 1;
}
.table-wrap td {
  padding: 11px 14px;
  font-size: 12px;
  color: var(--text-primary);
  border-bottom: 1px solid var(--border);
  transition: background 0.15s;
}
.table-wrap tr:hover td { background: rgba(43,127,255,0.02); }
.table-wrap tr:last-child td { border-bottom: none; }

.proto-badge {
  font-size: 8.5px;
  padding: 3px 8px;
  border-radius: 6px;
  font-weight: 700;
}
.pb-vless { background: rgba(43,127,255,0.1); color: var(--spider-blue); }
.pb-vmess { background: rgba(123,97,255,0.1); color: var(--spider-purple); }
.pb-trojan { background: rgba(255,35,82,0.1); color: var(--spider-red); }
.pb-ss { background: rgba(0,255,136,0.1); color: var(--spider-green); }
.pb-wg { background: rgba(255,215,0,0.1); color: var(--spider-gold); }

.usage-bar-wrap { width: 100%; min-width: 100px; }
.usage-bar {
  height: 5px;
  border-radius: 3px;
  background: rgba(43,127,255,0.06);
  overflow: hidden;
  margin-bottom: 3px;
}
.usage-fill {
  height: 100%;
  border-radius: 3px;
  background: var(--gradient-blue);
  transition: width 0.5s ease;
}
.usage-text {
  font-size: 9px;
  color: var(--text-secondary);
  display: flex;
  justify-content: space-between;
}
.status-dot {
  display: flex;
  align-items: center;
  gap: 5px;
  font-weight: 600;
  font-size: 11px;
}
.status-dot.active { color: var(--spider-green); }
.status-dot.expired { color: var(--spider-red); }

.exp-chip {
  font-size: 9px;
  padding: 2px 8px;
  border-radius: 6px;
  font-weight: 700;
}
.exp-ok { background: rgba(0,255,136,0.08); color: var(--spider-green); }
.exp-warn { background: rgba(255,215,0,0.08); color: var(--spider-gold); }
.exp-bad { background: rgba(255,35,82,0.08); color: var(--spider-red); }
.action-btns { display: flex; gap: 4px; }

/* ============================================================
   TABLE FILTERS
   ============================================================ */
.table-filters {
  display: flex;
  gap: 10px;
  padding: 12px 14px;
  border-bottom: 1px solid var(--border);
  flex-wrap: wrap;
  align-items: center;
}
.table-filters input,
.table-filters select {
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border);
  background: rgba(255,255,255,0.3);
  color: var(--text-primary);
  font-family: var(--font);
  font-size: 11px;
  outline: none;
  transition: all 0.2s;
}
[data-theme="dark"] .table-filters input,
[data-theme="dark"] .table-filters select {
  background: rgba(0,0,0,0.2);
}
.table-filters input:focus,
.table-filters select:focus {
  border-color: var(--spider-blue);
  box-shadow: 0 0 0 3px rgba(43,127,255,0.05);
}
.table-filters .filter-label {
  font-size: 10px;
  font-weight: 700;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* ============================================================
   PAGINATION
   ============================================================ */
.pagination {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 14px 0;
}
.pagination button {
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border);
  background: transparent;
  color: var(--text-secondary);
  font-family: var(--font);
  font-size: 11px;
  cursor: pointer;
  transition: all 0.2s;
}
.pagination button:hover { background: rgba(43,127,255,0.06); border-color: var(--spider-blue); }
.pagination button.active {
  background: var(--gradient-main);
  color: #fff;
  border-color: transparent;
}

/* ============================================================
   MODALS
   ============================================================ */
.modal-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.5);
  z-index: 500;
  align-items: center;
  justify-content: center;
  backdrop-filter: blur(8px);
  padding: 20px;
}
.modal-overlay.open { display: flex; }
.modal-card {
  background: var(--surface-glass);
  backdrop-filter: blur(32px) saturate(180%);
  -webkit-backdrop-filter: blur(32px) saturate(180%);
  border: 1px solid var(--border);
  border-radius: var(--radius-xl);
  padding: 0;
  max-width: 540px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: var(--shadow-xl);
  animation: modalIn 0.3s ease;
}
@keyframes modalIn {
  from { opacity: 0; transform: scale(0.95) translateY(12px); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}
.modal-head {
  padding: 20px 24px 16px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
}
.modal-title {
  font-size: 16px;
  font-weight: 800;
  color: var(--text-primary);
  display: flex;
  align-items: center;
  gap: 8px;
}
.modal-title i { color: var(--spider-purple); font-size: 18px; }
.modal-close {
  width: 32px; height: 32px;
  border-radius: var(--radius-sm);
  background: rgba(43,127,255,0.04);
  border: 1px solid var(--border);
  color: var(--text-secondary);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.2s;
}
.modal-close:hover { background: rgba(255,35,82,0.08); color: var(--spider-red); }
.modal-body { padding: 18px 24px; }
.modal-footer {
  padding: 14px 24px 20px;
  border-top: 1px solid var(--border);
  display: flex;
  gap: 10px;
  justify-content: flex-end;
}

/* Form fields */
.form-field { margin-bottom: 14px; }
.form-field label {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 10px;
  font-weight: 800;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 5px;
}
.form-field label i { color: var(--spider-purple); font-size: 13px; }
.form-input {
  width: 100%;
  padding: 10px 14px;
  border-radius: var(--radius);
  border: 1.5px solid var(--border);
  background: rgba(255,255,255,0.3);
  backdrop-filter: blur(8px);
  color: var(--text-primary);
  font-family: var(--font);
  font-size: 12.5px;
  outline: none;
  transition: all 0.2s;
}
[data-theme="dark"] .form-input { background: rgba(0,0,0,0.2); }
.form-input:focus {
  border-color: var(--spider-blue);
  box-shadow: 0 0 0 4px rgba(43,127,255,0.05);
}
.form-row { display: flex; gap: 10px; flex-wrap: wrap; }
.form-row .form-field { flex: 1; min-width: 120px; }
.form-select {
  width: 100%;
  padding: 10px 14px;
  border-radius: var(--radius);
  border: 1.5px solid var(--border);
  background: rgba(255,255,255,0.3);
  backdrop-filter: blur(8px);
  color: var(--text-primary);
  font-family: var(--font);
  font-size: 12.5px;
  outline: none;
  cursor: pointer;
}
[data-theme="dark"] .form-select { background: rgba(0,0,0,0.2); }
.form-textarea {
  width: 100%;
  padding: 10px 14px;
  border-radius: var(--radius);
  border: 1.5px solid var(--border);
  background: rgba(255,255,255,0.3);
  backdrop-filter: blur(8px);
  color: var(--text-primary);
  font-family: var(--font);
  font-size: 12.5px;
  outline: none;
  resize: vertical;
  min-height: 70px;
}
[data-theme="dark"] .form-textarea { background: rgba(0,0,0,0.2); }

/* Toggle switch */
.toggle-wrap {
  display: flex;
  align-items: center;
  gap: 10px;
}
.toggle-switch {
  width: 44px; height: 24px;
  border-radius: 12px;
  background: rgba(100,116,139,0.2);
  position: relative;
  cursor: pointer;
  transition: all 0.3s;
  border: none;
  flex-shrink: 0;
}
.toggle-switch::after {
  content: '';
  position: absolute;
  width: 18px; height: 18px;
  border-radius: 50%;
  background: #fff;
  right: 3px; top: 3px;
  transition: all 0.3s;
  box-shadow: 0 1px 3px rgba(0,0,0,0.15);
}
.toggle-switch.on { background: var(--spider-green); }
.toggle-switch.on::after { right: 23px; }
.toggle-label { font-size: 11.5px; color: var(--text-secondary); font-weight: 600; }

/* ============================================================
   TOAST
   ============================================================ */
.toast {
  position: fixed;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%) translateY(40px);
  background: var(--surface-glass);
  backdrop-filter: blur(20px);
  border: 1px solid var(--border);
  color: var(--text-primary);
  border-radius: var(--radius);
  padding: 12px 24px;
  font-size: 12.5px;
  opacity: 0;
  transition: all 0.3s;
  z-index: 999;
  pointer-events: none;
  display: flex;
  align-items: center;
  gap: 8px;
  box-shadow: var(--shadow-lg);
  white-space: nowrap;
}
.toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }
.toast.ok { border-color: rgba(0,255,136,0.2); color: var(--spider-green); }
.toast.err { border-color: rgba(255,35,82,0.2); color: var(--spider-red); }

/* ============================================================
   EMPTY STATE
   ============================================================ */
.empty-state {
  text-align: center;
  padding: 50px 20px;
  color: var(--text-secondary);
}
.empty-state i { font-size: 40px; opacity: 0.2; display: block; margin-bottom: 12px; }
.empty-state p { font-size: 13px; }

/* ============================================================
   CONFIG CARDS
   ============================================================ */
.cfg-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 14px;
}
.cfg-card-item {
  background: var(--surface-glass);
  backdrop-filter: blur(16px);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 0;
  overflow: hidden;
  transition: all var(--transition);
}
.cfg-card-item:hover {
  border-color: rgba(43,127,255,0.2);
  transform: translateY(-3px);
  box-shadow: var(--shadow-lg);
}
.cfg-card-top { padding: 16px 18px 12px; display: flex; align-items: flex-start; justify-content: space-between; gap: 10px; }
.cfg-card-label { font-size: 14px; font-weight: 700; color: var(--text-primary); }
.cfg-card-body { padding: 0 18px 14px; }
.cfg-code {
  background: rgba(0,0,0,0.03);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 10px 12px;
  font-family: var(--font-mono);
  font-size: 9.5px;
  color: var(--spider-blue);
  word-break: break-all;
  line-height: 1.7;
  max-height: 80px;
  overflow-y: auto;
  margin-bottom: 10px;
}
[data-theme="dark"] .cfg-code { background: rgba(0,0,0,0.15); color: #60A5FA; }
.cfg-card-actions { display: flex; gap: 6px; flex-wrap: wrap; padding: 0 18px 14px; }

/* ============================================================
   LOGS
   ============================================================ */
.log-list { display: flex; flex-direction: column; }
.log-row {
  display: flex;
  gap: 12px;
  padding: 11px 0;
  border-bottom: 1px solid var(--border);
}
.log-row:last-child { border-bottom: none; }
.log-icon-s {
  width: 34px; height: 34px;
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 15px;
  flex-shrink: 0;
}
.log-icon-s.info { background: rgba(43,127,255,0.08); color: var(--spider-blue); }
.log-icon-s.ok { background: rgba(0,255,136,0.08); color: var(--spider-green); }
.log-icon-s.warn { background: rgba(255,215,0,0.08); color: var(--spider-gold); }
.log-icon-s.err { background: rgba(255,35,82,0.08); color: var(--spider-red); }
.log-content { flex: 1; min-width: 0; }
.log-msg { font-size: 12.5px; color: var(--text-primary); line-height: 1.6; }
.log-time { font-size: 9.5px; color: var(--text-secondary); margin-top: 2px; display: flex; align-items: center; gap: 4px; }

/* ============================================================
   TRAFFIC CHART
   ============================================================ */
.chart-card {
  background: var(--surface-glass);
  backdrop-filter: blur(16px);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 20px 22px;
  margin-bottom: 20px;
}
.chart-title {
  font-size: 13px;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 14px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.chart-title i { color: var(--spider-blue); }
.chart-canvas-wrap { position: relative; height: 280px; }

/* ============================================================
   RESPONSIVE
   ============================================================ */
@media (max-width: 1100px) {
  .stats-grid { grid-template-columns: repeat(2, 1fr); }
  .server-circular { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 860px) {
  .sidebar {
    transform: translateX(100%);
    width: var(--sidebar-w-expanded);
  }
  .sidebar:hover { width: var(--sidebar-w-expanded); }
  .sidebar.open {
    transform: translateX(0);
    box-shadow: -10px 0 40px rgba(0,0,0,0.3);
  }
  .sidebar .nav-label { opacity: 1; width: auto; }
  .sidebar .sidebar-logo-text { opacity: 1; }
  .sidebar .sidebar-user-name { opacity: 1; }
  .sidebar .sidebar-user-role { opacity: 1; }
  .sidebar .sidebar-footer .theme-btn span { opacity: 1; width: auto; }
  .sidebar .sidebar-footer .logout-btn span { opacity: 1; width: auto; }

  .main { margin-right: 0; padding-top: 76px; }
  .mobile-top { display: flex; }
  .quick-actions { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 600px) {
  .stats-grid { grid-template-columns: 1fr 1fr; }
  .quick-actions { grid-template-columns: 1fr 1fr; }
  .main { padding: 72px 12px 40px; }
  .server-circular { grid-template-columns: repeat(2, 1fr); }
  .cfg-grid { grid-template-columns: 1fr; }
  .form-row { flex-direction: column; }
  .topbar-title { font-size: 18px; }
  .topbar-right .btn span { display: none; }
  .topbar-right .btn i { margin: 0; }
}
@media (max-width: 420px) {
  .stats-grid { grid-template-columns: 1fr; }
  .quick-actions { grid-template-columns: 1fr; }
}
</style>
</head>
<body data-theme="dark">

<!-- ============================================================
   BACKGROUND PARTICLES
   ============================================================ -->
<div class="bg-particles" id="bgParticles">
  <div class="particle-bg"></div>
  <div class="particle-bg"></div>
  <div class="particle-bg"></div>
</div>

<!-- ============================================================
   TOAST
   ============================================================ -->
<div class="toast" id="toast"></div>

<!-- ============================================================
   OVERLAY (موبایل)
   ============================================================ -->
<div class="overlay" id="overlay"></div>

<!-- ============================================================
   MODALS
   ============================================================ -->
<!-- مودال ایجاد کاربر -->
<div class="modal-overlay" id="modal-create-user">
  <div class="modal-card">
    <div class="modal-head">
      <div class="modal-title"><i class="ti ti-user-plus"></i> ایجاد کاربر جدید</div>
      <button class="modal-close" onclick="closeModal('modal-create-user')"><i class="ti ti-x"></i></button>
    </div>
    <div class="modal-body">
      <form id="create-user-form">
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-user"></i> نام کاربری</label><input class="form-input" id="cu-username" placeholder="username" required></div>
          <div class="form-field"><label><i class="ti ti-lock"></i> رمز عبور</label><input class="form-input" id="cu-password" type="password" placeholder="••••" required></div>
        </div>
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-plug-connected"></i> پروتکل</label><select class="form-select" id="cu-protocol"><option value="vless">VLESS</option><option value="vmess">VMess</option><option value="trojan">Trojan</option><option value="shadowsocks">Shadowsocks</option><option value="wireguard">WireGuard</option></select></div>
          <div class="form-field"><label><i class="ti ti-server"></i> سرور</label><select class="form-select" id="cu-server"><option value="">انتخاب سرور...</option></select></div>
        </div>
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-gauge"></i> محدودیت ترافیک</label><input class="form-input" id="cu-traffic" type="number" min="0" step="0.1" placeholder="مقدار"></div>
          <div class="form-field"><label>واحد</label><select class="form-select" id="cu-traffic-unit"><option value="GB">GB</option><option value="MB">MB</option><option value="TB">TB</option><option value="unlimited">نامحدود</option></select></div>
        </div>
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-calendar"></i> روزهای انقضا</label><input class="form-input" id="cu-expire" type="number" min="0" placeholder="0 = نامحدود"></div>
          <div class="form-field"><label><i class="ti ti-users"></i> اتصال همزمان</label><input class="form-input" id="cu-concurrent" type="number" min="1" value="1"></div>
        </div>
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-route"></i> اینباند</label><select class="form-select" id="cu-inbound"><option value="">انتخاب اینباند...</option></select></div>
          <div class="form-field" id="cu-worker-country-wrap" style="display:none"><label><i class="ti ti-map-pin"></i> کشور ورکر</label><select class="form-select" id="cu-worker-country"><option value="">انتخاب کشور...</option></select></div>
        </div>
        <div class="form-field"><label><i class="ti ti-notes"></i> یادداشت</label><textarea class="form-textarea" id="cu-notes" placeholder="یادداشت اختیاری..."></textarea></div>
        <div class="toggle-wrap">
          <button type="button" class="toggle-switch on" id="cu-active-toggle" onclick="this.classList.toggle('on')"></button>
          <span class="toggle-label">فعال</span>
        </div>
      </form>
    </div>
    <div class="modal-footer">
      <button class="btn btn-ghost" onclick="closeModal('modal-create-user')">انصراف</button>
      <button class="btn btn-primary" onclick="createUser()"><i class="ti ti-user-plus"></i> ایجاد کاربر</button>
    </div>
  </div>
</div>

<!-- مودال کانفیگ -->
<div class="modal-overlay" id="modal-config">
  <div class="modal-card" style="max-width:460px">
    <div class="modal-head">
      <div class="modal-title"><i class="ti ti-link"></i> کانفیگ</div>
      <button class="modal-close" onclick="closeModal('modal-config')"><i class="ti ti-x"></i></button>
    </div>
    <div class="modal-body">
      <div class="cfg-code" style="max-height:none;font-size:11px" id="config-text"></div>
      <div style="margin-top:14px;display:flex;gap:8px">
        <button class="btn btn-primary" onclick="copyConfigText()"><i class="ti ti-copy"></i> کپی</button>
        <button class="btn btn-ghost" onclick="showQRCode()"><i class="ti ti-qrcode"></i> QR Code</button>
      </div>
      <div id="config-qr" style="margin-top:14px;text-align:center;display:none">
        <img id="config-qr-img" src="" alt="QR" style="max-width:200px;border-radius:12px;background:#fff;padding:8px">
      </div>
    </div>
  </div>
</div>

<!-- ============================================================
   MOBILE TOP BAR
   ============================================================ -->
<div class="mobile-top">
  <div class="mobile-brand">
    <svg width="28" height="28" viewBox="0 0 100 100"><defs><linearGradient id="mg1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#2B7FFF"/><stop offset="100%" style="stop-color:#7B61FF"/></linearGradient></defs><ellipse cx="50" cy="48" rx="16" ry="18" fill="url(#mg1)"/><ellipse cx="50" cy="28" rx="10" ry="9" fill="url(#mg1)"/><circle cx="46" cy="25" r="2.5" fill="#fff"/><circle cx="54" cy="25" r="2.5" fill="#fff"/></svg>
    <span>Spider Panel</span>
  </div>
  <div class="mobile-actions">
    <button class="mob-btn" id="menu-toggle" onclick="toggleSidebar()"><i class="ti ti-menu-2"></i></button>
  </div>
</div>

<!-- ============================================================
   SIDEBAR
   ============================================================ -->
<aside class="sidebar" id="sidebar">
  <div class="sidebar-logo">
    <svg width="36" height="36" viewBox="0 0 100 100"><defs><linearGradient id="sg1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#2B7FFF"/><stop offset="50%" style="stop-color:#7B61FF"/><stop offset="100%" style="stop-color:#FF2352"/></linearGradient></defs><path d="M50,50 L10,15 M50,50 L15,50 M50,50 L10,85 M50,50 L90,15 M50,50 L85,50 M50,50 L90,85 M50,50 L30,5 M50,50 L70,5" stroke="url(#sg1)" stroke-width="2.5" fill="none" stroke-linecap="round"/><ellipse cx="50" cy="46" rx="18" ry="22" fill="url(#sg1)"/><ellipse cx="50" cy="23" rx="12" ry="10" fill="url(#sg1)"/><circle cx="44.5" cy="20" r="3" fill="#fff"/><circle cx="55.5" cy="20" r="3" fill="#fff"/><circle cx="45" cy="19.5" r="1.2" fill="#1a1a2e"/><circle cx="56" cy="19.5" r="1.2" fill="#1a1a2e"/></svg>
    <div class="sidebar-logo-text">Spider Panel<span class="sidebar-logo-sub">Spider Gateway</span></div>
  </div>
  <div class="sidebar-nav">
    <div class="nav-section">منوی اصلی</div>
    <div class="nav-item active" data-page="dash"><i class="ti ti-layout-dashboard"></i><span class="nav-label">داشبورد</span><span class="nav-tooltip">داشبورد</span></div>
    <div class="nav-item" data-page="users"><i class="ti ti-users"></i><span class="nav-label">کاربران</span><span class="nav-badge" id="users-count">0</span><span class="nav-tooltip">کاربران</span></div>
    <div class="nav-item" data-page="configs"><i class="ti ti-link-plus"></i><span class="nav-label">کانفیگ‌ها</span><span class="nav-badge" id="configs-count">0</span><span class="nav-tooltip">کانفیگ‌ها</span></div>
    <div class="nav-item" data-page="servers"><i class="ti ti-server-2"></i><span class="nav-label">سرورها</span><span class="nav-tooltip">سرورها</span></div>
    <div class="nav-item" data-page="plans"><i class="ti ti-receipt-2"></i><span class="nav-label">پلن‌ها</span><span class="nav-tooltip">پلن‌ها</span></div>
    <div class="nav-item" data-page="groups"><i class="ti ti-folders"></i><span class="nav-label">گروه‌ها</span><span class="nav-tooltip">گروه‌ها</span></div>
    <div class="nav-item" data-page="traffic"><i class="ti ti-chart-area"></i><span class="nav-label">ترافیک</span><span class="nav-tooltip">ترافیک</span></div>
    <div class="nav-item" data-page="logs"><i class="ti ti-history"></i><span class="nav-label">لاگ‌ها</span><span class="nav-tooltip">لاگ‌ها</span></div>
    <div class="nav-section">سیستم</div>
    <div class="nav-item" data-page="worker"><i class="ti ti-cloud"></i><span class="nav-label">Worker</span><span class="nav-tooltip">Worker</span></div>
    <div class="nav-item" data-page="api"><i class="ti ti-api"></i><span class="nav-label">API</span><span class="nav-tooltip">API</span></div>
    <div class="nav-item" data-page="tools"><i class="ti ti-tools"></i><span class="nav-label">ابزارها</span><span class="nav-tooltip">ابزارها</span></div>
    <div class="nav-item" data-page="settings"><i class="ti ti-settings"></i><span class="nav-label">تنظیمات</span><span class="nav-tooltip">تنظیمات</span></div>
    <div class="nav-item" data-page="logout" style="color:var(--spider-red)"><i class="ti ti-logout"></i><span class="nav-label">خروج</span><span class="nav-tooltip">خروج</span></div>
  </div>
  <div class="sidebar-footer">
    <div class="sidebar-user">
      <div class="sidebar-avatar"><i class="ti ti-user"></i></div>
      <div><div class="sidebar-user-name">ادمین</div><div class="sidebar-user-role">مدیر سیستم</div></div>
    </div>
    <button class="theme-btn" id="themeToggleBtn" onclick="cycleTheme()"><i class="ti ti-moon"></i><span id="theme-label">تاریک</span></button>
    <button class="logout-btn" onclick="doLogout()"><i class="ti ti-logout"></i><span>خروج از حساب</span></button>
  </div>
</aside>

<!-- ============================================================
   MAIN CONTENT
   ============================================================ -->
<main class="main">

  <!-- ===== DASHBOARD ===== -->
  <section class="page active" id="page-dash">
    <div class="topbar">
      <div class="topbar-left">
        <div>
          <div class="topbar-title"><i class="ti ti-layout-dashboard"></i> داشبورد</div>
          <div class="topbar-sub"><span class="dot-online"></span> سیستم آنلاین · <span id="last-updated">در حال بارگذاری...</span></div>
        </div>
      </div>
      <div class="topbar-right">
        <div class="theme-selector" id="themeSelector">
          <button class="theme-dot dark" data-theme="dark" onclick="setTheme('dark')" title="تاریک"></button>
          <button class="theme-dot light" data-theme="light" onclick="setTheme('light')" title="روشن"></button>
          <button class="theme-dot gold" data-theme="gold" onclick="setTheme('gold')" title="طلایی"></button>
          <button class="theme-dot pastel" data-theme="pastel" onclick="setTheme('pastel')" title="پاستیل"></button>
          <button class="theme-dot neon active" data-theme="neon" onclick="setTheme('neon')" title="نئون"></button>
        </div>
        <button class="bell-btn" title="اعلان‌ها"><i class="ti ti-bell"></i></button>
        <button class="btn btn-primary" onclick="openModal('modal-create-user')"><i class="ti ti-user-plus"></i> <span>کاربر جدید</span></button>
      </div>
    </div>

    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon blue"><i class="ti ti-users"></i></div>
        <div class="stat-label">کاربران فعال</div>
        <div class="stat-value"><span class="counter-value" id="s-active-users">—</span></div>
        <div class="stat-sub up" id="s-users-trend"><i class="ti ti-trending-up"></i> در حال رشد</div>
      </div>
      <div class="stat-card">
        <div class="stat-icon green"><i class="ti ti-link"></i></div>
        <div class="stat-label">کانفیگ‌های فعال</div>
        <div class="stat-value"><span class="counter-value" id="s-active-configs">—</span></div>
        <div class="stat-sub"><span class="dot dot-green pulse"></span> فعال</div>
      </div>
      <div class="stat-card">
        <div class="stat-icon purple"><i class="ti ti-transfer"></i></div>
        <div class="stat-label">مصرف ترافیک</div>
        <div class="stat-value"><span class="counter-value" id="s-traffic">—</span></div>
        <div class="stat-sub">کل مصرف</div>
      </div>
      <div class="stat-card">
        <div class="stat-icon red"><i class="ti ti-server-2"></i></div>
        <div class="stat-label">سرورهای آنلاین</div>
        <div class="stat-value"><span class="counter-value" id="s-online-servers">—</span></div>
        <div class="stat-sub"><span class="dot dot-green pulse"></span> آنلاین</div>
      </div>
    </div>

    <div class="quick-actions">
      <button class="qa-btn" onclick="openModal('modal-create-user')"><i class="ti ti-user-plus"></i> افزودن کاربر</button>
      <button class="qa-btn" onclick="switchPage('configs')"><i class="ti ti-link-plus"></i> ساخت کانفیگ</button>
      <button class="qa-btn" onclick="switchPage('traffic')"><i class="ti ti-chart-bar"></i> گزارش ترافیک</button>
      <button class="qa-btn" onclick="refreshAll()"><i class="ti ti-refresh"></i> بروزرسانی</button>
    </div>

    <div class="server-panel">
      <div class="server-title"><i class="ti ti-activity"></i> وضعیت سرور</div>
      <div class="server-circular">
        <div class="srv-circle">
          <canvas id="cpuCanvas" width="160" height="160"></canvas>
          <span class="srv-circle-label">CPU</span>
          <span class="srv-circle-value" id="srv-cpu-label">—%</span>
        </div>
        <div class="srv-circle">
          <canvas id="ramCanvas" width="160" height="160"></canvas>
          <span class="srv-circle-label">RAM</span>
          <span class="srv-circle-value" id="srv-ram-label">—%</span>
        </div>
        <div class="srv-circle">
          <canvas id="diskCanvas" width="160" height="160"></canvas>
          <span class="srv-circle-label">Disk</span>
          <span class="srv-circle-value" id="srv-disk-label">—%</span>
        </div>
        <div class="srv-circle">
          <canvas id="netCanvas" width="160" height="160"></canvas>
          <span class="srv-circle-label">Network</span>
          <span class="srv-circle-value" id="srv-net-label">— MB/s</span>
        </div>
      </div>
    </div>

    <div class="table-wrap">
      <div class="table-filters">
        <span class="filter-label"><i class="ti ti-filter"></i> فیلتر:</span>
        <input type="text" id="dash-search" placeholder="جستجوی کاربر..." oninput="filterDashTable()">
        <select id="dash-filter-proto" onchange="filterDashTable()">
          <option value="all">همه پروتکل‌ها</option>
          <option value="vless">VLESS</option>
          <option value="vmess">VMess</option>
          <option value="trojan">Trojan</option>
          <option value="shadowsocks">Shadowsocks</option>
          <option value="wireguard">WireGuard</option>
        </select>
        <select id="dash-filter-status" onchange="filterDashTable()">
          <option value="all">همه وضعیت‌ها</option>
          <option value="active">فعال</option>
          <option value="expired">غیرفعال</option>
        </select>
      </div>
      <table>
        <thead><tr><th onclick="sortDashTable('label')" style="cursor:pointer">نام کاربری</th><th onclick="sortDashTable('protocol')" style="cursor:pointer">پروتکل</th><th>مصرف</th><th>انقضا</th><th>وضعیت</th><th>عملیات</th></tr></thead>
        <tbody id="dash-users-table"><tr><td colspan="6" style="text-align:center;padding:30px;color:var(--text-secondary)">در حال بارگذاری...</td></tr></tbody>
      </table>
      <div class="pagination" id="dash-pagination"></div>
    </div>
  </section>

  <!-- ===== USERS ===== -->
  <section class="page" id="page-users">
    <div class="topbar">
      <div class="topbar-left">
        <div>
          <div class="topbar-title"><i class="ti ti-users"></i> کاربران</div>
          <div class="topbar-sub">مدیریت کاربران و کانفیگ‌ها</div>
        </div>
      </div>
      <div class="topbar-right">
        <button class="btn btn-primary" onclick="openModal('modal-create-user')"><i class="ti ti-user-plus"></i> <span>کاربر جدید</span></button>
      </div>
    </div>
    <div class="table-wrap">
      <div class="table-filters">
        <span class="filter-label"><i class="ti ti-filter"></i> فیلتر:</span>
        <input type="text" id="users-search" placeholder="جستجوی کاربر..." oninput="filterUsersTable()">
        <select id="users-filter-proto" onchange="filterUsersTable()">
          <option value="all">همه پروتکل‌ها</option>
          <option value="vless">VLESS</option>
          <option value="vmess">VMess</option>
          <option value="trojan">Trojan</option>
          <option value="shadowsocks">Shadowsocks</option>
          <option value="wireguard">WireGuard</option>
        </select>
        <select id="users-filter-status" onchange="filterUsersTable()">
          <option value="all">همه وضعیت‌ها</option>
          <option value="active">فعال</option>
          <option value="expired">غیرفعال</option>
        </select>
      </div>
      <table>
        <thead><tr><th onclick="sortUsersTable('label')" style="cursor:pointer">نام کاربری</th><th onclick="sortUsersTable('protocol')" style="cursor:pointer">پروتکل</th><th>مصرف</th><th>انقضا</th><th>وضعیت</th><th>عملیات</th></tr></thead>
        <tbody id="users-table"><tr><td colspan="6" style="text-align:center;padding:30px;color:var(--text-secondary)">در حال بارگذاری...</td></tr></tbody>
      </table>
      <div class="pagination" id="users-pagination"></div>
    </div>
  </section>

  <!-- ===== CONFIGS ===== -->
  <section class="page" id="page-configs">
    <div class="topbar">
      <div class="topbar-left">
        <div>
          <div class="topbar-title"><i class="ti ti-link-plus"></i> کانفیگ‌ها</div>
          <div class="topbar-sub">مدیریت کانفیگ‌های کاربران</div>
        </div>
      </div>
      <div class="topbar-right"><span class="badge badge-blue" id="cfg-total">۰ کانفیگ</span></div>
    </div>
    <div class="cfg-grid" id="configs-grid"></div>
    <div class="empty-state" id="configs-empty" style="display:none"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>
  </section>

  <!-- ===== TRAFFIC ===== -->
  <section class="page" id="page-traffic">
    <div class="topbar">
      <div class="topbar-left">
        <div>
          <div class="topbar-title"><i class="ti ti-chart-area"></i> ترافیک</div>
          <div class="topbar-sub">آمار مصرف پهنای باند</div>
        </div>
      </div>
      <div class="topbar-right"><button class="btn btn-ghost" onclick="refreshAll()"><i class="ti ti-refresh"></i> <span>بروزرسانی</span></button></div>
    </div>
    <div class="chart-card">
      <div class="chart-title"><i class="ti ti-activity"></i> روند مصرف ترافیک (MB)</div>
      <div class="chart-canvas-wrap"><canvas id="traffic-chart"></canvas></div>
    </div>
    <div class="stats-grid" style="grid-template-columns:repeat(3,1fr)">
      <div class="stat-card"><div class="stat-icon blue"><i class="ti ti-arrow-up-right"></i></div><div class="stat-label">میانگین ساعتی</div><div class="stat-value" id="t-avg" style="font-size:20px">—</div></div>
      <div class="stat-card"><div class="stat-icon purple"><i class="ti ti-chart-bar"></i></div><div class="stat-label">پیک مصرف</div><div class="stat-value" id="t-peak" style="font-size:20px">—</div></div>
      <div class="stat-card"><div class="stat-icon green"><i class="ti ti-database"></i></div><div class="stat-label">کل مصرف</div><div class="stat-value" id="t-total" style="font-size:20px">—</div></div>
    </div>
  </section>

  <!-- ===== LOGS ===== -->
  <section class="page" id="page-logs">
    <div class="topbar">
      <div class="topbar-left">
        <div>
          <div class="topbar-title"><i class="ti ti-history"></i> لاگ‌ها</div>
          <div class="topbar-sub">تاریخچه فعالیت‌های سیستم</div>
        </div>
      </div>
      <div class="topbar-right"><button class="btn btn-ghost" onclick="loadLogs()"><i class="ti ti-refresh"></i> <span>بروزرسانی</span></button></div>
    </div>
    <div class="table-wrap">
      <div class="log-list" id="logs-list"><div class="empty-state"><i class="ti ti-history-toggle"></i><p>در حال بارگذاری...</p></div></div>
    </div>
  </section>

  <!-- ===== SERVERS ===== -->
  <section class="page" id="page-servers">
    <div class="topbar"><div class="topbar-left"><div><div class="topbar-title"><i class="ti ti-server-2"></i> سرورها</div></div></div></div>
    <div class="empty-state"><i class="ti ti-server-off"></i><p>بخش مدیریت سرورها</p></div>
  </section>

  <!-- ===== PLANS ===== -->
  <section class="page" id="page-plans">
    <div class="topbar"><div class="topbar-left"><div><div class="topbar-title"><i class="ti ti-receipt-2"></i> پلن‌ها</div></div></div></div>
    <div class="empty-state"><i class="ti ti-package-off"></i><p>بخش مدیریت پلن‌ها</p></div>
  </section>

  <!-- ===== GROUPS ===== -->
  <section class="page" id="page-groups">
    <div class="topbar"><div class="topbar-left"><div><div class="topbar-title"><i class="ti ti-folders"></i> گروه‌ها</div></div></div></div>
    <div class="empty-state"><i class="ti ti-folders-off"></i><p>بخش مدیریت گروه‌ها</p></div>
  </section>

  <!-- ===== SETTINGS ===== -->
  <section class="page" id="page-settings">
    <div class="topbar">
      <div class="topbar-left"><div><div class="topbar-title"><i class="ti ti-settings"></i> تنظیمات</div><div class="topbar-sub">تنظیمات عمومی پنل</div></div></div>
      <div class="topbar-right"><button class="btn btn-primary" onclick="saveSettings()"><i class="ti ti-device-floppy"></i> <span>ذخیره تغییرات</span></button></div>
    </div>
    <div class="table-wrap" style="margin-bottom:18px">
      <div style="padding:16px 22px;border-bottom:1px solid var(--border)"><div class="server-title" style="margin-bottom:0"><i class="ti ti-world"></i> دامنه و شبکه</div></div>
      <div style="padding:16px 22px">
        <div class="form-field"><label><i class="ti ti-world-www"></i> دامنه اصلی</label><input class="form-input" id="set-domain" placeholder="example.com" dir="ltr"></div>
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-route"></i> نوع انتقال پیش‌فرض</label><select class="form-select" id="set-transport"><option value="ws">WebSocket (WS)</option><option value="xhttp">XHTTP</option><option value="tcp">TCP</option></select></div>
          <div class="form-field"><label><i class="ti ti-plug-connected"></i> مد اتصال پیش‌فرض</label><select class="form-select" id="set-conn-mode"><option value="ws">WebSocket</option><option value="xhttp">XHTTP</option><option value="tcp">TCP</option></select></div>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== WORKER ===== -->
  <section class="page" id="page-worker">
    <div class="topbar">
      <div class="topbar-left"><div><div class="topbar-title"><i class="ti ti-cloud"></i> Cloudflare Worker</div><div class="topbar-sub">تنظیم و مدیریت Worker برای پروکسی‌های توزیع‌شده</div></div></div>
      <div class="topbar-right"><button class="btn btn-primary" id="worker-sync-btn" onclick="syncWorkerProxies()"><i class="ti ti-refresh-cw"></i> <span>همگام‌سازی</span></button></div>
    </div>
    <div class="empty-state"><i class="ti ti-cloud"></i><p>بخش مدیریت Worker</p></div>
  </section>

</main>

<script>
// ============================================================
// GLOBALS
// ============================================================
var isDark = localStorage.getItem('spider-theme') === 'dark' || true;
var currentTheme = localStorage.getItem('spider-theme') || 'neon';
var currentPage = 'dash';
var currentConfigText = '';
var currentConfigUserId = '';
var allLinks = [];
var allUsers = [];
var filteredLinks = [];
var trafficChart = null;
var sortDashKey = 'label';
var sortDashAsc = true;
var sortUsersKey = 'label';
var sortUsersAsc = true;
var dashPage = 0;
var usersPage = 0;
var pageSize = 5;

// ============================================================
// THEME SYSTEM
// ============================================================
function setTheme(theme) {
  currentTheme = theme;
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('spider-theme', theme);
  document.querySelectorAll('.theme-dot').forEach(function(el) {
    el.classList.toggle('active', el.dataset.theme === theme);
  });
  // Update sidebar theme button
  var btn = document.getElementById('themeToggleBtn');
  var label = document.getElementById('theme-label');
  if (btn) {
    var icons = { dark: 'ti-moon', light: 'ti-sun', gold: 'ti-star', pastel: 'ti-flower', neon: 'ti-bolt' };
    var labels = { dark: 'تاریک', light: 'روشن', gold: 'طلایی', pastel: 'پاستیل', neon: 'نئون' };
    btn.querySelector('i').className = 'ti ' + (icons[theme] || 'ti-moon');
    label.textContent = labels[theme] || 'تاریک';
  }
}

function cycleTheme() {
  var themes = ['neon', 'dark', 'light', 'gold', 'pastel'];
  var idx = themes.indexOf(currentTheme);
  var next = themes[(idx + 1) % themes.length];
  setTheme(next);
}

// ============================================================
// TOAST
// ============================================================
function toast(msg, type) {
  var t = document.getElementById('toast');
  t.textContent = msg;
  t.className = 'toast show' + (type ? ' ' + type : '');
  clearTimeout(t._timer);
  t._timer = setTimeout(function() { t.classList.remove('show'); }, 2500);
}

// ============================================================
// UTILITY
// ============================================================
function esc(s) { return String(s || '').replace(/[&<>"']/g, function(c) {
  return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c] || c;
}); }
function fmtB(b) {
  if (!b || b === 0) return '0 B';
  if (b < 1024) return b + ' B';
  if (b < 1024**2) return (b/1024).toFixed(1) + ' KB';
  if (b < 1024**3) return (b/1024**2).toFixed(2) + ' MB';
  return (b/1024**3).toFixed(2) + ' GB';
}
function toFa(n) { return String(n).replace(/\d/g, function(d) { return '۰۱۲۳۴۵۶۷۸۹'[d]; }); }

// ============================================================
// AUTH
// ============================================================
async function authFetch(url, opts) {
  var r = await fetch(url, opts);
  if (r.status === 401) { location.href = '/login'; throw new Error('unauthorized'); }
  return r;
}
async function checkAuth() {
  try { var r = await fetch('/api/me'); var d = await r.json(); if (!d.authenticated) location.href = '/login'; } catch(e) {}
}
async function doLogout() {
  try { await fetch('/api/logout', { method: 'POST' }); } catch(e) {}
  location.href = '/login';
}

// ============================================================
// SIDEBAR
// ============================================================
function toggleSidebar() {
  var sb = document.getElementById('sidebar'), ov = document.getElementById('overlay');
  sb.classList.toggle('open'); ov.classList.toggle('show');
}
document.getElementById('menu-toggle').onclick = toggleSidebar;
document.getElementById('overlay').onclick = toggleSidebar;

function switchPage(name) {
  if (name === 'logout') { doLogout(); return; }
  currentPage = name;
  document.querySelectorAll('.nav-item').forEach(function(el) {
    el.classList.toggle('active', el.dataset.page === name);
  });
  document.querySelectorAll('.page').forEach(function(el) {
    el.classList.toggle('active', el.id === 'page-' + name);
  });
  toggleSidebar();
  window.scrollTo({ top: 0, behavior: 'smooth' });
  var loaders = { users: loadUsers, configs: loadConfigs, traffic: loadTraffic, logs: loadLogs, dash: loadDashboard, settings: loadSettings, worker: loadWorker };
  if (loaders[name]) loaders[name]();
}
document.querySelectorAll('.nav-item').forEach(function(el) {
  el.onclick = function() { switchPage(el.dataset.page); };
});

// ============================================================
// MODALS
// ============================================================
function openModal(id) {
  document.getElementById(id).classList.add('open');
  if (id === 'modal-create-user') loadInbounds();
}
function closeModal(id) { document.getElementById(id).classList.remove('open'); }
document.querySelectorAll('.modal-overlay').forEach(function(m) {
  m.addEventListener('click', function(e) { if (e.target === m) m.classList.remove('open'); });
});

// ============================================================
// LOAD INBOUNDS
// ============================================================
async function loadInbounds() {
  try {
    var r = await authFetch('/api/inbounds'), d = await r.json();
    var inbounds = d.inbounds || [];
    var inboundSelect = document.getElementById('cu-inbound');
    if (!inboundSelect) return;
    inboundSelect.innerHTML = '<option value="">انتخاب اینباند...</option>' +
      inbounds.map(function(ib) {
        return '<option value="' + esc(ib.inbound_id) + '">' + esc(ib.name) + ' (' + esc(ib.protocol) + ' ' + esc(ib.network) + ')</option>';
      }).join('');
    inboundSelect.onchange = function() {
      var selectedId = this.value;
      var selectedInbound = inbounds.find(function(ib) { return ib.inbound_id === selectedId; });
      var wrap = document.getElementById('cu-worker-country-wrap');
      if (selectedInbound && selectedInbound.protocol === 'worker') {
        loadWorkerCountries(selectedId);
        wrap.style.display = 'block';
      } else {
        wrap.style.display = 'none';
      }
    };
  } catch(e) { console.error(e); }
}

async function loadWorkerCountries(inboundId) {
  try {
    var r = await authFetch('/api/worker/inbounds'), d = await r.json();
    var workerInbounds = d.inbounds || [];
    var select = document.getElementById('cu-worker-country');
    if (!select) return;
    var selectedInbound = workerInbounds.find(function(ib) { return ib.inbound_id === inboundId; });
    if (selectedInbound && selectedInbound.countries && selectedInbound.countries.length > 0) {
      select.innerHTML = '<option value="">انتخاب کشور...</option>' +
        selectedInbound.countries.map(function(c) {
          return '<option value="' + esc(c.code) + '">' + esc(c.country) + ' (' + esc(c.code) + ')</option>';
        }).join('');
    } else {
      select.innerHTML = '<option value="">انتخاب کشور...</option>';
    }
  } catch(e) { console.error(e); }
}

// ============================================================
// CREATE USER
// ============================================================
async function createUser() {
  var traffic = document.getElementById('cu-traffic').value;
  var unit = document.getElementById('cu-traffic-unit').value;
  var active = document.getElementById('cu-active-toggle').classList.contains('on');
  var inboundId = document.getElementById('cu-inbound').value;
  var body = {
    label: document.getElementById('cu-username').value.trim(),
    password: document.getElementById('cu-password').value,
    protocol: document.getElementById('cu-protocol').value,
    limit_value: traffic || '0',
    limit_unit: unit === 'unlimited' ? 'GB' : unit,
    expires_days: document.getElementById('cu-expire').value || '0',
    concurrent: document.getElementById('cu-concurrent').value || '1',
    server_id: document.getElementById('cu-server').value || null,
    note: document.getElementById('cu-notes').value.trim(),
    active: active,
    inbound_id: inboundId || null
  };
  var wrap = document.getElementById('cu-worker-country-wrap');
  if (wrap && wrap.style.display !== 'none') {
    var proxyCountry = document.getElementById('cu-worker-country').value;
    if (proxyCountry) body.proxy_countries = [proxyCountry.toLowerCase()];
  }
  if (!body.label) { toast('نام کاربری الزامی است', 'err'); return; }
  try {
    var r = await authFetch('/api/users', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
    if (!r.ok) { var d = await r.json().catch(function(){return{};}); throw new Error(d.detail || 'خطا'); }
    toast('کاربر با موفقیت ایجاد شد ✓', 'ok');
    closeModal('modal-create-user');
    ['cu-username','cu-password','cu-traffic','cu-expire','cu-concurrent','cu-notes'].forEach(function(id) { document.getElementById(id).value = ''; });
    loadUsers(); loadConfigs(); loadDashboard();
  } catch(e) { toast(e.message, 'err'); }
}

// ============================================================
// LOAD USERS
// ============================================================
async function loadUsers() {
  try {
    var r = await authFetch('/api/links'), d = await r.json();
    allLinks = d.links || [];
    document.getElementById('users-count').textContent = allLinks.length;
    filteredLinks = [...allLinks];
    renderUsersTable(filteredLinks, 'users-table');
    renderUsersTable(filteredLinks, 'dash-users-table');
  } catch(e) { console.error(e); }
}

function renderUsersTable(links, tableId) {
  var tbody = document.getElementById(tableId);
  if (!links || !links.length) {
    tbody.innerHTML = '<tr><td colspan="6"><div class="empty-state"><i class="ti ti-users-off"></i><p>کاربری وجود ندارد</p></div></td></tr>';
    return;
  }
  // Pagination
  var isDash = tableId === 'dash-users-table';
  var page = isDash ? dashPage : usersPage;
  var start = page * pageSize;
  var end = Math.min(start + pageSize, links.length);
  var pageLinks = links.slice(start, end);

  tbody.innerHTML = pageLinks.map(function(l) {
    var pct = l.limit_bytes === 0 ? 0 : Math.min(100, l.used_bytes / l.limit_bytes * 100);
    var bc = pct > 90 ? 'var(--spider-red)' : pct > 70 ? 'var(--spider-gold)' : 'var(--spider-blue)';
    var lim = l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes);
    var protoClass = l.protocol === 'vless' || l.protocol === 'vless-ws' ? 'pb-vless' :
                     l.protocol === 'vmess' ? 'pb-vmess' :
                     l.protocol === 'trojan' ? 'pb-trojan' :
                     l.protocol === 'shadowsocks' ? 'pb-ss' : 'pb-wg';
    var protoFa = l.protocol === 'vless-ws' ? 'VLESS' : l.protocol === 'vmess' ? 'VMess' : l.protocol === 'trojan' ? 'Trojan' : l.protocol === 'shadowsocks' ? 'Shadowsocks' : l.protocol === 'wireguard' ? 'WireGuard' : l.protocol || 'VLESS';
    var isActive = l.active && !l.expired;
    var expText = l.expired ? 'منقضی' : l.expires_at ? new Date(l.expires_at).toLocaleDateString('fa-IR') : 'نامحدود';
    var expCls = l.expired ? 'exp-bad' : l.expires_at ? 'exp-ok' : 'exp-ok';
    return '<tr><td style="font-weight:600">' + esc(l.label) + '</td>' +
      '<td><span class="proto-badge ' + protoClass + '">' + protoFa + '</span></td>' +
      '<td><div class="usage-bar-wrap"><div class="usage-bar"><div class="usage-fill" style="width:' + pct + '%;background:' + bc + '"></div></div><div class="usage-text"><span>' + fmtB(l.used_bytes) + '</span><span>' + lim + '</span></div></div></td>' +
      '<td><span class="exp-chip ' + expCls + '">' + expText + '</span></td>' +
      '<td><div class="status-dot ' + (isActive ? 'active' : 'expired') + '"><span class="dot ' + (isActive ? 'dot-green' : 'dot-red') + ' ' + (isActive ? 'pulse' : '') + '"></span>' + (isActive ? 'فعال' : 'غیرفعال') + '</div></td>' +
      '<td><div class="action-btns">' +
        '<button class="btn btn-sm btn-ghost btn-icon" onclick="viewConfig(\'' + l.uuid + '\')" title="مشاهده"><i class="ti ti-eye"></i></button>' +
        '<button class="btn btn-sm btn-ghost btn-icon" onclick="copyLink(\'' + l.uuid + '\')" title="کپی"><i class="ti ti-copy"></i></button>' +
        '<button class="btn btn-sm btn-ghost btn-icon" onclick="toggleUser(\'' + l.uuid + '\')" title="فعال/غیرفعال"><i class="ti ti-toggle-' + (isActive ? 'right' : 'left') + '"></i></button>' +
        '<button class="btn btn-sm btn-danger btn-icon" onclick="deleteUser(\'' + l.uuid + '\')" title="حذف"><i class="ti ti-trash"></i></button>' +
      '</div></td></tr>';
  }).join('');

  // Pagination controls
  var totalPages = Math.ceil(links.length / pageSize);
  var pagEl = document.getElementById(isDash ? 'dash-pagination' : 'users-pagination');
  if (pagEl && totalPages > 1) {
    var html = '<button onclick="changePage(\'' + tableId + '\', -1)" ' + (page === 0 ? 'disabled' : '') + '>‹</button>';
    for (var i = 0; i < totalPages; i++) {
      html += '<button class="' + (i === page ? 'active' : '') + '" onclick="changePage(\'' + tableId + '\', ' + (i - page) + ')">' + (i + 1) + '</button>';
    }
    html += '<button onclick="changePage(\'' + tableId + '\', 1)" ' + (page >= totalPages - 1 ? 'disabled' : '') + '>›</button>';
    pagEl.innerHTML = html;
  } else if (pagEl) {
    pagEl.innerHTML = '';
  }
}

function changePage(tableId, delta) {
  var isDash = tableId === 'dash-users-table';
  var page = isDash ? dashPage : usersPage;
  var links = isDash ? filteredLinks : filteredLinks;
  var total = Math.ceil(links.length / pageSize);
  var newPage = Math.max(0, Math.min(total - 1, page + delta));
  if (isDash) dashPage = newPage; else usersPage = newPage;
  renderUsersTable(filteredLinks, tableId);
}

// ============================================================
// FILTERS & SORT
// ============================================================
function filterDashTable() { filterTable('dash'); }
function filterUsersTable() { filterTable('users'); }

function filterTable(prefix) {
  var search = document.getElementById(prefix + '-search').value.toLowerCase();
  var proto = document.getElementById(prefix + '-filter-proto').value;
  var status = document.getElementById(prefix + '-filter-status').value;
  filteredLinks = allLinks.filter(function(l) {
    var matchSearch = l.label.toLowerCase().includes(search);
    var matchProto = proto === 'all' || l.protocol === proto || (proto === 'vless' && l.protocol === 'vless-ws');
    var matchStatus = status === 'all' || (status === 'active' && l.active && !l.expired) || (status === 'expired' && (!l.active || l.expired));
    return matchSearch && matchProto && matchStatus;
  });
  if (prefix === 'dash') { dashPage = 0; renderUsersTable(filteredLinks, 'dash-users-table'); }
  else { usersPage = 0; renderUsersTable(filteredLinks, 'users-table'); }
}

function sortDashTable(key) { sortTable('dash', key); }
function sortUsersTable(key) { sortTable('users', key); }

function sortTable(prefix, key) {
  var isDash = prefix === 'dash';
  var sortKey = isDash ? 'sortDashKey' : 'sortUsersKey';
  var sortAsc = isDash ? 'sortDashAsc' : 'sortUsersAsc';
  if (window[sortKey] === key) window[sortAsc] = !window[sortAsc];
  else { window[sortKey] = key; window[sortAsc] = true; }
  filteredLinks.sort(function(a, b) {
    var va = a[key] || '', vb = b[key] || '';
    if (typeof va === 'string') va = va.toLowerCase();
    if (typeof vb === 'string') vb = vb.toLowerCase();
    if (va < vb) return window[sortAsc] ? -1 : 1;
    if (va > vb) return window[sortAsc] ? 1 : -1;
    return 0;
  });
  if (isDash) { dashPage = 0; renderUsersTable(filteredLinks, 'dash-users-table'); }
  else { usersPage = 0; renderUsersTable(filteredLinks, 'users-table'); }
}

// ============================================================
// USER ACTIONS
// ============================================================
async function viewConfig(uuid) {
  var link = allLinks.find(function(l) { return l.uuid === uuid; });
  if (!link) { toast('کانفیگ یافت نشد', 'err'); return; }
  currentConfigText = link.vless_link || '';
  currentConfigUserId = link.user_id || link.uuid || '';
  document.getElementById('config-text').textContent = currentConfigText;
  document.getElementById('config-qr').style.display = 'none';
  openModal('modal-config');
}
function copyConfigText() {
  if (!currentConfigText) return;
  navigator.clipboard.writeText(currentConfigText).then(function() { toast('کانفیگ کپی شد ✓', 'ok'); });
}
function showQRCode() {
  if (!currentConfigUserId) return;
  document.getElementById('config-qr-img').src = '/api/users/' + encodeURIComponent(currentConfigUserId) + '/qr?t=' + Date.now();
  document.getElementById('config-qr').style.display = 'block';
}
function copyLink(uuid) {
  var link = allLinks.find(function(l) { return l.uuid === uuid; });
  if (!link || !link.vless_link) return;
  navigator.clipboard.writeText(link.vless_link).then(function() { toast('لینک کپی شد ✓', 'ok'); });
}
async function toggleUser(uuid) {
  var link = allLinks.find(function(l) { return l.uuid === uuid; });
  if (!link) return;
  try {
    var r = await authFetch('/api/links/' + uuid, { method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ active: !link.active }) });
    if (!r.ok) throw new Error();
    toast('وضعیت تغییر کرد ✓', 'ok');
    loadUsers(); loadDashboard();
  } catch(e) { toast('خطا در تغییر وضعیت', 'err'); }
}
async function deleteUser(uuid) {
  if (!confirm('آیا از حذف این کاربر اطمینان دارید؟')) return;
  try {
    var r = await authFetch('/api/links/' + uuid, { method: 'DELETE' });
    if (!r.ok) throw new Error();
    toast('کاربر حذف شد ✓', 'ok');
    loadUsers(); loadDashboard(); loadConfigs();
  } catch(e) { toast('خطا در حذف', 'err'); }
}

// ============================================================
// CONFIGS
// ============================================================
async function loadConfigs() {
  try {
    var r = await authFetch('/api/links'), d = await r.json();
    allLinks = d.links || [];
    document.getElementById('configs-count').textContent = allLinks.length;
    document.getElementById('cfg-total').textContent = toFa(allLinks.length) + ' کانفیگ';
    var grid = document.getElementById('configs-grid'), empty = document.getElementById('configs-empty');
    if (!allLinks.length) { grid.innerHTML = ''; empty.style.display = 'block'; return; }
    empty.style.display = 'none';
    grid.innerHTML = allLinks.map(function(l) {
      var protoFa = l.protocol === 'vless-ws' ? 'VLESS' : l.protocol === 'vmess' ? 'VMess' : l.protocol === 'trojan' ? 'Trojan' : l.protocol || 'VLESS';
      var protoClass = l.protocol === 'vless-ws' ? 'pb-vless' : l.protocol === 'vmess' ? 'pb-vmess' : l.protocol === 'trojan' ? 'pb-trojan' : 'pb-vless';
      var isActive = l.active && !l.expired;
      var pct = l.limit_bytes === 0 ? 0 : Math.min(100, l.used_bytes / l.limit_bytes * 100);
      return '<div class="cfg-card-item">' +
        '<div class="cfg-card-top"><span class="cfg-card-label">' + esc(l.label) + '</span><span class="badge ' + (isActive ? 'badge-green' : 'badge-red') + '"><span class="dot ' + (isActive ? 'dot-green' : 'dot-red') + ' ' + (isActive ? 'pulse' : '') + '"></span> ' + (isActive ? 'فعال' : 'غیرفعال') + '</span></div>' +
        '<div class="cfg-card-body"><span class="proto-badge ' + protoClass + '" style="margin-bottom:8px;display:inline-block">' + protoFa + '</span>' +
        '<div class="usage-bar-wrap" style="margin-bottom:8px"><div class="usage-bar"><div class="usage-fill" style="width:' + pct + '%"></div></div><div class="usage-text"><span>' + fmtB(l.used_bytes) + '</span><span>' + (l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes)) + '</span></div></div></div>' +
        '<div class="cfg-card-actions">' +
        '<button class="btn btn-sm btn-ghost" onclick="viewConfig(\'' + l.uuid + '\')"><i class="ti ti-eye"></i> مشاهده</button>' +
        '<button class="btn btn-sm btn-ghost" onclick="copyLink(\'' + l.uuid + '\')"><i class="ti ti-copy"></i> کپی</button>' +
        '<button class="btn btn-sm btn-ghost btn-icon" onclick="showQRForLink(\'' + l.uuid + '\')"><i class="ti ti-qrcode"></i></button>' +
        '</div></div>';
    }).join('');
  } catch(e) { console.error(e); }
}
function showQRForLink(uuid) {
  var link = allLinks.find(function(l) { return l.uuid === uuid; });
  if (!link || !link.vless_link) return;
  currentConfigText = link.vless_link;
  currentConfigUserId = link.user_id || link.uuid || '';
  document.getElementById('config-text').textContent = currentConfigText;
  showQRCode();
  openModal('modal-config');
}

// ============================================================
// TRAFFIC
// ============================================================
async function loadTraffic() {
  try {
    var r = await authFetch('/stats'), d = await r.json();
    document.getElementById('t-total').textContent = (d.total_traffic_mb || 0).toFixed(1) + ' MB';
    if (d.hourly) {
      var labels = Object.keys(d.hourly).sort(), vals = labels.map(function(k) { return +(d.hourly[k] / 1024**2).toFixed(2); });
      if (vals.length) {
        var total = vals.reduce(function(a,b){return a+b;}, 0);
        var avg = total / vals.length;
        var peak = Math.max.apply(null, vals);
        document.getElementById('t-avg').textContent = avg.toFixed(2) + ' MB';
        document.getElementById('t-peak').textContent = peak.toFixed(2) + ' MB';
      }
      var canvas = document.getElementById('traffic-chart');
      if (!canvas) return;
      var ctx = canvas.getContext('2d');
      if (trafficChart) {
        trafficChart.data.labels = labels;
        trafficChart.data.datasets[0].data = vals;
        trafficChart.update();
      } else {
        var grad = ctx.createLinearGradient(0, 0, 0, 300);
        grad.addColorStop(0, 'rgba(43,127,255,0.35)');
        grad.addColorStop(1, 'rgba(43,127,255,0)');
        trafficChart = new Chart(ctx, {
          type: 'line',
          data: {
            labels: labels,
            datasets: [{
              data: vals,
              borderColor: '#2B7FFF',
              backgroundColor: grad,
              fill: true,
              tension: 0.4,
              pointRadius: 0,
              borderWidth: 2.5
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
              x: { grid: { display: false }, ticks: { font: { size: 9 } } },
              y: { grid: { color: 'rgba(43,127,255,0.05)' }, ticks: { font: { size: 9 }, callback: function(v) { return v + ' MB'; } } }
            },
            interaction: { mode: 'index', intersect: false }
          }
        });
      }
    }
  } catch(e) { console.error(e); }
}

// ============================================================
// LOGS
// ============================================================
async function loadLogs() {
  try {
    var r = await authFetch('/api/activity'), d = await r.json();
    var logs = (d.logs || []).slice().reverse();
    var el = document.getElementById('logs-list');
    if (!logs.length) { el.innerHTML = '<div class="empty-state"><i class="ti ti-history-toggle"></i><p>هنوز لاگی ثبت نشده</p></div>'; return; }
    var icMap = { ok: 'ti-circle-check ok', err: 'ti-circle-x err', warn: 'ti-alert-triangle warn', info: 'ti-info-circle info' };
    el.innerHTML = logs.map(function(l) {
      var level = l.level || 'info';
      var icon = icMap[level] || 'ti-info-circle info';
      var cls = level === 'ok' ? 'ok' : level === 'err' ? 'err' : level === 'warn' ? 'warn' : 'info';
      return '<div class="log-row"><div class="log-icon-s ' + cls + '"><i class="ti ' + icon + '"></i></div><div class="log-content"><div class="log-msg">' + esc(l.message) + '</div><div class="log-time"><i class="ti ti-clock"></i> ' + new Date(l.time).toLocaleString('fa-IR') + '</div></div></div>';
    }).join('');
  } catch(e) { console.error(e); }
}

// ============================================================
// DASHBOARD
// ============================================================
async function loadDashboard() {
  try {
    var r = await authFetch('/stats'), d = await r.json();
    animateCounter('s-active-users', d.active_links || 0);
    animateCounter('s-active-configs', d.active_links || 0);
    document.getElementById('s-traffic').innerHTML = (d.total_traffic_mb || 0).toFixed(1) + ' GB';
    document.getElementById('s-online-servers').textContent = '1';
    document.getElementById('last-updated').textContent = 'آخرین بروزرسانی: ' + new Date().toLocaleTimeString('fa-IR');

    // Circular progress
    drawCircle('cpuCanvas', 32, '#2B7FFF');
    drawCircle('ramCanvas', 58, '#7B61FF');
    drawCircle('diskCanvas', 41, '#FFD700');
    drawCircle('netCanvas', 24, '#00FF88');
    document.getElementById('srv-cpu-label').textContent = '32%';
    document.getElementById('srv-ram-label').textContent = '58%';
    document.getElementById('srv-disk-label').textContent = '41%';
    document.getElementById('srv-net-label').textContent = '12 MB/s';

    // Load users
    var lr = await authFetch('/api/links'), ld = await lr.json();
    allLinks = ld.links || [];
    document.getElementById('users-count').textContent = allLinks.length;
    filteredLinks = [...allLinks];
    renderUsersTable(filteredLinks, 'dash-users-table');
  } catch(e) { console.error(e); }
}

function animateCounter(id, target) {
  var el = document.getElementById(id);
  if (!el) return;
  var current = parseInt(el.textContent.replace(/[^0-9]/g, '')) || 0;
  var duration = 800;
  var start = performance.now();
  function update(t) {
    var progress = Math.min(1, (t - start) / duration);
    var eased = 1 - Math.pow(1 - progress, 3);
    var val = Math.round(current + (target - current) * eased);
    el.textContent = val;
    if (progress < 1) requestAnimationFrame(update);
  }
  requestAnimationFrame(update);
}

// ============================================================
// CIRCULAR PROGRESS
// ============================================================
function drawCircle(canvasId, percent, color) {
  var canvas = document.getElementById(canvasId);
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var w = canvas.width, h = canvas.height;
  ctx.clearRect(0, 0, w, h);
  var cx = w/2, cy = h/2, r = 60, lw = 10;
  // Background
  ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI * 2);
  ctx.strokeStyle = 'rgba(255,255,255,0.04)';
  ctx.lineWidth = lw; ctx.stroke();
  // Progress
  var end = (percent / 100) * Math.PI * 2;
  ctx.beginPath(); ctx.arc(cx, cy, r, -Math.PI/2, -Math.PI/2 + end);
  var grad = ctx.createLinearGradient(0, 0, w, h);
  grad.addColorStop(0, color);
  grad.addColorStop(1, color + '80');
  ctx.strokeStyle = grad;
  ctx.lineWidth = lw;
  ctx.lineCap = 'round';
  ctx.stroke();
  // Glow
  ctx.shadowColor = color;
  ctx.shadowBlur = 20;
  ctx.stroke();
  ctx.shadowBlur = 0;
}

// ============================================================
// SETTINGS
// ============================================================
async function loadSettings() {
  try {
    var r = await authFetch('/api/tools/settings'), d = await r.json();
    document.getElementById('set-domain').value = d.domain || '';
    document.getElementById('set-transport').value = d.default_transport || 'ws';
    document.getElementById('set-conn-mode').value = d.default_connection_mode || 'ws';
  } catch(e) { console.error(e); }
}
async function saveSettings() {
  try {
    var body = {
      domain: document.getElementById('set-domain').value.trim(),
      default_transport: document.getElementById('set-transport').value,
      default_connection_mode: document.getElementById('set-conn-mode').value
    };
    var r = await authFetch('/api/tools/settings', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
    if (!r.ok) throw new Error();
    toast('تنظیمات ذخیره شد ✓', 'ok');
  } catch(e) { toast('خطا در ذخیره تنظیمات', 'err'); }
}

// ============================================================
// WORKER
// ============================================================
async function loadWorker() {
  try {
    var r = await authFetch('/api/worker'), d = await r.json();
    // Simple placeholder
    var syncBtn = document.getElementById('worker-sync-btn');
    if (syncBtn) syncBtn.style.display = d.connected ? 'inline-flex' : 'none';
  } catch(e) { console.error(e); }
}
async function syncWorkerProxies() {
  try {
    var r = await authFetch('/api/worker/sync-source', { method: 'POST' });
    var d = await r.json();
    if (!d.ok) throw new Error(d.error || 'sync failed');
    toast('پروکسی‌ها همگام‌سازی شدند ✓', 'ok');
  } catch(e) { toast(e.message, 'err'); }
}

// ============================================================
// REFRESH
// ============================================================
function refreshAll() {
  loadDashboard(); loadUsers(); loadConfigs(); loadTraffic(); loadLogs(); loadWorker();
  toast('بروزرسانی شد ✓', 'ok');
}

// ============================================================
// PARTICLES INTERACTION
// ============================================================
document.addEventListener('mousemove', function(e) {
  var particles = document.querySelectorAll('.particle-bg');
  var x = e.clientX / window.innerWidth - 0.5;
  var y = e.clientY / window.innerHeight - 0.5;
  particles.forEach(function(p, i) {
    var speed = 8 + i * 4;
    p.style.transform = 'translate(' + (x * speed) + 'px, ' + (y * speed) + 'px)';
  });
});

// ============================================================
// INIT
// ============================================================
document.addEventListener('DOMContentLoaded', function() {
  // Apply saved theme
  setTheme(currentTheme);

  checkAuth();
  loadDashboard();
  setInterval(function() {
    if (currentPage === 'dash') loadDashboard();
    if (currentPage === 'users') loadUsers();
    if (currentPage === 'configs') loadConfigs();
    if (currentPage === 'traffic') loadTraffic();
    if (currentPage === 'logs') loadLogs();
    if (currentPage === 'settings') loadSettings();
    if (currentPage === 'worker') loadWorker();
  }, 5000);
});

// ============================================================
// CHART.JS LOADER (از CDN)
// ============================================================
(function loadChartJS() {
  var script = document.createElement('script');
  script.src = 'https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js';
  script.onload = function() { if (currentPage === 'traffic') loadTraffic(); };
  document.head.appendChild(script);
})();
</script>
</body></html>"""


def get_public_page_html(uuid_key: str) -> str:
    """صفحه پابلیک سابسکریپشن با تم Spider Panel"""
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>Spider Panel · اشتراک</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
:root{{
  --spider-blue:#2B7FFF;--spider-purple:#7B61FF;--spider-red:#FF2352;
  --success:#16A34A;--warning:#F59E0B;--danger:#DC2626;
  --text-primary:#0F172A;--text-secondary:#475569;
  --bg:#F8FAFC;--surface:rgba(255,255,255,.8);--surface-glass:rgba(255,255,255,.75);
  --border:rgba(226,232,240,.7);
  --radius:18px;--radius-lg:24px;--radius-xl:28px;
  --shadow-sm:0 2px 8px rgba(0,0,0,.04);--shadow-md:0 8px 24px rgba(0,0,0,.06);
  --shadow-lg:0 16px 48px rgba(0,0,0,.08);
}}
[data-theme="dark"]{{
  --text-primary:#F1F5F9;--text-secondary:#94A3B8;
  --bg:#0B1121;--surface:rgba(15,23,42,.85);--surface-glass:rgba(15,23,42,.7);
  --border:rgba(226,232,240,.06);
  --shadow-sm:0 2px 8px rgba(0,0,0,.2);--shadow-md:0 8px 24px rgba(0,0,0,.3);
  --shadow-lg:0 16px 48px rgba(0,0,0,.4);
}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{min-height:100%;background:var(--bg);font-family:'Vazirmatn',sans-serif;color:var(--text-primary);font-size:14px;transition:background .4s,color .4s}}
.bg-glow{{position:fixed;inset:0;z-index:0;pointer-events:none}}
.bg-orb{{position:absolute;border-radius:50%;filter:blur(120px);opacity:.15;animation:float 14s ease-in-out infinite}}
.bg-orb:nth-child(1){{width:450px;height:450px;background:var(--spider-blue);top:-150px;left:-100px}}
.bg-orb:nth-child(2){{width:350px;height:350px;background:var(--spider-purple);bottom:-100px;right:-80px;animation-delay:-7s}}
@keyframes float{{0%,100%{{transform:translateY(0) scale(1)}}50%{{transform:translateY(-25px) scale(1.04)}}}}
.wrap{{position:relative;z-index:10;max-width:680px;margin:0 auto;padding:28px 16px 60px}}
.top-bar{{display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;gap:10px}}
.brand{{display:flex;align-items:center;gap:10px}}
.brand svg{{width:38px;height:38px;filter:drop-shadow(0 3px 8px rgba(43,127,255,.3))}}
.brand-name{{font-size:14px;font-weight:800;color:var(--text-primary)}}
.brand-sub{{font-size:9.5px;color:var(--text-secondary)}}
.theme-toggle{{width:38px;height:38px;border-radius:var(--radius);background:var(--surface);backdrop-filter:blur(12px);border:1px solid var(--border);color:var(--text-secondary);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:16px;transition:all .2s}}
.theme-toggle:hover{{background:rgba(43,127,255,.1);color:var(--spider-blue)}}
/* Info card */
.info-card{{background:var(--surface);backdrop-filter:blur(20px) saturate(160%);-webkit-backdrop-filter:blur(20px) saturate(160%);border:1px solid var(--border);border-radius:var(--radius-xl);padding:28px 26px 24px;margin-bottom:18px;box-shadow:var(--shadow-lg);position:relative;overflow:hidden}}
.info-card::before{{content:'';position:absolute;top:0;right:0;width:180px;height:180px;background:radial-gradient(circle,rgba(123,97,255,.08),transparent 70%);pointer-events:none}}
.info-name{{font-size:22px;font-weight:800;color:var(--text-primary);position:relative;z-index:1;letter-spacing:-.02em}}
.info-desc{{font-size:12.5px;color:var(--text-secondary);margin-top:6px;position:relative;z-index:1;line-height:1.7}}
.info-stats{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:18px;position:relative;z-index:1}}
.info-stat{{text-align:center;padding:12px 8px;background:rgba(43,127,255,.04);border-radius:var(--radius);border:1px solid var(--border)}}
.info-s-val{{font-size:18px;font-weight:800;color:var(--text-primary)}}
.info-s-label{{font-size:9px;color:var(--text-secondary);margin-top:3px;font-weight:600;text-transform:uppercase;letter-spacing:.04em}}
/* Config cards */
.section-title{{font-size:12.5px;font-weight:800;color:var(--text-secondary);margin-bottom:12px;display:flex;align-items:center;gap:7px;text-transform:uppercase;letter-spacing:.06em}}
.section-title i{{color:var(--spider-blue);font-size:15px}}
.cfg-card{{background:var(--surface);backdrop-filter:blur(16px);border:1px solid var(--border);border-radius:var(--radius-lg);padding:20px 20px 18px;margin-bottom:12px;box-shadow:var(--shadow-sm);transition:all .3s}}
.cfg-card:hover{{border-color:rgba(43,127,255,.2);transform:translateY(-2px);box-shadow:var(--shadow-md)}}
.cfg-head{{display:flex;align-items:flex-start;justify-content:space-between;gap:8px;margin-bottom:12px}}
.cfg-name{{font-size:14px;font-weight:700;color:var(--text-primary)}}
.cfg-status{{font-size:10px;padding:3px 10px;border-radius:20px;font-weight:700;white-space:nowrap}}
.cfg-status.ok{{background:rgba(22,163,74,.1);color:var(--success)}}
.cfg-status.no{{background:rgba(255,35,82,.1);color:var(--spider-red)}}
.cfg-code{{background:rgba(15,23,42,.05);border:1px solid var(--border);border-radius:var(--radius);padding:12px 14px;font-family:'Inter',monospace;font-size:10px;color:var(--spider-blue);word-break:break-all;line-height:1.7;margin-bottom:10px;max-height:80px;overflow-y:auto}}
[data-theme="dark"] .cfg-code{{background:rgba(0,0,0,.2);color:#60A5FA}}
.cfg-actions{{display:flex;gap:7px;flex-wrap:wrap}}
.btn{{font-family:'Vazirmatn',sans-serif;font-size:11.5px;font-weight:700;border-radius:var(--radius);padding:8px 15px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;border:none;transition:all .2s;white-space:nowrap}}
.btn i{{font-size:13px}}
.btn-p{{background:linear-gradient(90deg,var(--spider-blue),var(--spider-purple));color:#fff;box-shadow:0 4px 14px rgba(43,127,255,.25)}}
.btn-p:hover{{transform:translateY(-1px);box-shadow:0 6px 20px rgba(43,127,255,.35)}}
.btn-ghost{{background:rgba(43,127,255,.06);color:var(--spider-blue);border:1px solid rgba(43,127,255,.15)}}
.btn-ghost:hover{{background:rgba(43,127,255,.12)}}
/* Password lock */
.lock-page{{display:flex;align-items:center;justify-content:center;min-height:70vh}}
.lock-card{{background:var(--surface);backdrop-filter:blur(24px);border:1px solid var(--border);border-radius:var(--radius-xl);padding:40px 32px 34px;text-align:center;max-width:380px;width:100%;box-shadow:var(--shadow-lg)}}
.lock-icon{{width:64px;height:64px;border-radius:18px;background:rgba(43,127,255,.1);border:1px solid rgba(43,127,255,.2);display:flex;align-items:center;justify-content:center;margin:0 auto 18px;font-size:28px;color:var(--spider-blue)}}
.lock-title{{font-size:18px;font-weight:800;margin-bottom:6px}}
.lock-sub{{font-size:12px;color:var(--text-secondary);margin-bottom:20px;line-height:1.7}}
.lock-field{{position:relative;margin-bottom:14px}}
.lock-input{{width:100%;padding:13px 44px;border-radius:var(--radius);border:1.5px solid var(--border);background:rgba(255,255,255,.5);backdrop-filter:blur(8px);color:var(--text-primary);font-family:inherit;font-size:14px;text-align:center;outline:none;transition:all .2s;letter-spacing:.1em}}
.lock-input:focus{{border-color:var(--spider-blue);box-shadow:0 0 0 4px rgba(43,127,255,.1)}}
.lock-icon-left{{position:absolute;right:14px;top:50%;transform:translateY(-50%);color:var(--text-secondary);font-size:16px;pointer-events:none}}
.lock-err{{color:var(--spider-red);font-size:11px;margin-bottom:10px;min-height:18px}}
/* Toast */
.toast{{position:fixed;bottom:24px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--surface);backdrop-filter:blur(16px);border:1px solid var(--border);color:var(--text-primary);border-radius:var(--radius);padding:10px 20px;font-size:12px;opacity:0;transition:all .3s;z-index:999;pointer-events:none;white-space:nowrap;box-shadow:var(--shadow-md)}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(22,163,74,.3);color:var(--success)}}
/* Empty */
.empty{{text-align:center;padding:60px 20px;color:var(--text-secondary)}}
.empty i{{font-size:40px;opacity:.3;display:block;margin-bottom:12px}}
.footer{{text-align:center;padding-top:30px;font-size:10.5px;color:var(--text-secondary)}}
@media(max-width:500px){{
  .info-stats{{grid-template-columns:1fr 1fr}}
  .wrap{{padding:20px 12px 50px}}
}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
</style>
</head>
<body data-theme="light">
<div class="bg-glow"><div class="bg-orb"></div><div class="bg-orb"></div></div>
<div class="toast" id="toast"></div>
<div class="wrap">
  <div class="top-bar">
    <div class="brand">
      <svg width="38" height="38" viewBox="0 0 100 100"><defs><linearGradient id="bgg" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#2B7FFF"/><stop offset="50%" style="stop-color:#7B61FF"/><stop offset="100%" style="stop-color:#FF2352"/></linearGradient></defs><ellipse cx="50" cy="48" rx="17" ry="20" fill="url(#bgg)"/><ellipse cx="50" cy="26" rx="11" ry="9" fill="url(#bgg)"/><circle cx="46" cy="23" r="2.5" fill="#fff"/><circle cx="54" cy="23" r="2.5" fill="#fff"/><path d="M50,50 L12,16 M50,50 L16,50 M50,50 L12,84 M50,50 L88,16 M50,50 L84,50 M50,50 L88,84" stroke="url(#bgg)" stroke-width="2.2" fill="none" stroke-linecap="round"/></svg>
      <div><div class="brand-name">Spider Panel</div><div class="brand-sub">Spider Gateway</div></div>
    </div>
    <button class="theme-toggle" onclick="toggleTheme()" title="تغییر تم"><i class="ti ti-sun" id="theme-icon"></i></button>
  </div>
  <div id="root"><div class="empty"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i><p>در حال بارگذاری...</p></div></div>
  <div class="footer">Spider Panel · Spider Gateway</div>
</div>
<script>
var UUID_KEY='{uuid_key}',savedPw='',currentData=null;
var isDark=localStorage.getItem('spider-pub-theme')==='dark';
function applyTheme(d){{document.documentElement.setAttribute('data-theme',d?'dark':'light');document.getElementById('theme-icon').className='ti '+(d?'ti-sun':'ti-moon')}}
function toggleTheme(){{isDark=!isDark;localStorage.setItem('spider-pub-theme',isDark?'dark':'light');applyTheme(isDark)}}
applyTheme(isDark);
function toast(m,t){{var el=document.getElementById('toast');el.textContent=m;el.className='toast show'+(t?' '+t:'');setTimeout(function(){{el.classList.remove('show')}},2400)}}
function esc(s){{return String(s||'').replace(/[&<>"']/g,function(c){{return{{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]}})}}
function fmtB(b){{if(!b)return'0 B';if(b<1024)return b+' B';if(b<1024**2)return(b/1024).toFixed(1)+' KB';if(b<1024**3)return(b/1024**2).toFixed(2)+' MB';return(b/1024**3).toFixed(2)+' GB'}}
function toFa(n){{return String(n).replace(/\\d/g,function(d){{return'۰۱۲۳۴۵۶۷۸۹'[d]}})}}

async function loadData(pw){{var u='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');var r=await fetch(u);return r.json()}}

function renderLock(name,err){{document.getElementById('root').innerHTML='<div class="lock-page"><div class="lock-card"><div class="lock-icon"><i class="ti ti-shield-lock"></i></div><div class="lock-title">'+esc(name)+'</div><div class="lock-sub">این گروه با رمز محافظت می‌شود</div><div class="lock-err" id="lock-err">'+(err?'<i class="ti ti-alert-circle"></i> '+esc(err):'')+'</div><div class="lock-field"><i class="ti ti-lock lock-icon-left"></i><input class="lock-input" type="password" id="lock-pw" placeholder="••••••••" autofocus></div><button class="btn btn-p" style="width:100%;justify-content:center;padding:12px" onclick="submitLock()"><i class="ti ti-lock-open"></i> ورود</button></div></div>';document.getElementById('lock-pw').addEventListener('keydown',function(e){{if(e.key==='Enter')submitLock()}})}}

async function submitLock(){{var pw=document.getElementById('lock-pw').value;var d=await loadData(pw);if(d.locked){{renderLock(d.name,'رمز اشتباه است');return}}savedPw=pw;renderContent(d)}}

function renderContent(d){{currentData=d;var active=d.links.filter(function(l){{return l.active}}).length;var subUrl=d.sub_url||(location.protocol+'//'+location.host+'/sub-group/'+UUID_KEY);subUrl+=savedPw?'?pw='+encodeURIComponent(savedPw):'';
document.getElementById('root').innerHTML='<div class="info-card"><div class="info-name">'+esc(d.name)+'</div>'+(d.desc?'<div class="info-desc">'+esc(d.desc)+'</div>':'')+
'<div class="info-stats"><div class="info-stat"><div class="info-s-val">'+toFa(active)+'</div><div class="info-s-label">کانفیگ فعال</div></div><div class="info-stat"><div class="info-s-val">'+toFa(d.links.length)+'</div><div class="info-s-label">کل کانفیگ‌ها</div></div><div class="info-stat"><div class="info-s-val">'+esc(d.total_used_fmt||'0')+'</div><div class="info-s-label">مصرف</div></div></div></div>'+
'<div class="section-title"><i class="ti ti-link"></i> کانفیگ‌ها ('+toFa(d.links.length)+' عدد)</div>'+
(d.links.length?d.links.map(function(l){{return'<div class="cfg-card"><div class="cfg-head"><div class="cfg-name">'+esc(l.label)+'</div><span class="cfg-status '+(l.active?'ok':'no')+'">'+(l.active?'<i class="ti ti-circle-check"></i> فعال':'<i class="ti ti-circle-x"></i> غیرفعال')+'</span></div><div class="cfg-code">'+esc(l.vless_link)+'</div><div class="cfg-actions"><button class="btn btn-p" onclick="navigator.clipboard.writeText(\''+esc(l.vless_link).replace(/'/g,"\\'")+'\').then(function(){{toast(\'کپی شد ✓\',\'ok\')}})"><i class="ti ti-copy"></i> کپی لینک</button><button class="btn btn-ghost" onclick="window.open(\'https://api.qrserver.com/v1/create-qr-code/?size=220x220&data='+encodeURIComponent(l.vless_link)+'\',\'_blank\')"><i class="ti ti-qrcode"></i> QR Code</button></div></div>'}}).join(''):'<div class="empty"><i class="ti ti-link-off"></i><p>کانفیگی در این گروه وجود ندارد</p></div>')+
'<div style="margin-top:16px;text-align:center"><button class="btn btn-ghost" style="justify-content:center" onclick="location.reload()"><i class="ti ti-refresh"></i> بروزرسانی</button></div>';
}}

async function init(){{try{{var d=await loadData();if(d.locked){{renderLock(d.name);return}}renderContent(d)}}catch(e){{document.getElementById('root').innerHTML='<div class="empty"><i class="ti ti-alert-circle" style="color:var(--spider-red)"></i><p>خطا در بارگذاری</p></div>'}}}}
init();
</script>
</body></html>"""
