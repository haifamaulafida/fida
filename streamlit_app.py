<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OrganIQ — Sistem Identifikasi Senyawa Organik</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@400;500&family=Lora:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
<style>
:root {
  --bg: #0d1117;
  --bg2: #161b22;
  --bg3: #21262d;
  --border: rgba(255,255,255,0.08);
  --border2: rgba(255,255,255,0.15);
  --text: #e6edf3;
  --muted: #7d8590;
  --teal: #39d4a5;
  --teal-dim: rgba(57,212,165,0.12);
  --amber: #f0a03a;
  --amber-dim: rgba(240,160,58,0.12);
  --coral: #f07878;
  --coral-dim: rgba(240,120,120,0.12);
  --blue: #4da6ff;
  --blue-dim: rgba(77,166,255,0.12);
  --purple: #a78bfa;
  --purple-dim: rgba(167,139,250,0.12);
  --green: #56d364;
  --green-dim: rgba(86,211,100,0.12);
  --radius: 12px;
  --font-head: 'Syne', sans-serif;
  --font-mono: 'DM Mono', monospace;
  --font-body: 'Lora', serif;
}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg);color:var(--text);font-family:var(--font-body);font-size:16px;line-height:1.7;min-height:100vh;overflow-x:hidden}
::selection{background:var(--teal);color:#000}

/* NAV */
nav{position:fixed;top:0;left:0;right:0;z-index:100;background:rgba(13,17,23,0.85);backdrop-filter:blur(12px);border-bottom:1px solid var(--border);padding:0 2rem;height:56px;display:flex;align-items:center;gap:2rem}
.nav-logo{font-family:var(--font-head);font-size:1.1rem;font-weight:800;color:var(--teal);letter-spacing:-0.02em;cursor:pointer}
.nav-links{display:flex;gap:0.25rem;flex:1}
.nav-link{background:none;border:none;color:var(--muted);font-family:var(--font-body);font-size:0.85rem;padding:6px 12px;border-radius:8px;cursor:pointer;transition:all 0.2s}
.nav-link:hover,.nav-link.active{color:var(--text);background:var(--bg3)}
.nav-badge{font-family:var(--font-mono);font-size:0.65rem;background:var(--teal-dim);color:var(--teal);padding:2px 6px;border-radius:4px;margin-left:4px}

/* PAGES */
.page{display:none;padding-top:56px;min-height:100vh}
.page.active{display:block}

/* ===== LANDING ===== */
#page-home{display:none;align-items:center;justify-content:center;padding-top:56px}
#page-home.active{display:flex;flex-direction:column}
.hero{text-align:center;padding:5rem 2rem 3rem;max-width:800px;margin:0 auto}
.hero-eyebrow{font-family:var(--font-mono);font-size:0.75rem;color:var(--teal);letter-spacing:0.12em;text-transform:uppercase;margin-bottom:1.5rem}
.hero h1{font-family:var(--font-head);font-size:clamp(2.5rem,6vw,4.5rem);font-weight:800;line-height:1.05;letter-spacing:-0.03em;margin-bottom:1.5rem}
.hero h1 span{color:var(--teal)}
.hero p{font-size:1.05rem;color:var(--muted);max-width:540px;margin:0 auto 2.5rem;line-height:1.8}
.hero-btns{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap}
.btn-primary{background:var(--teal);color:#0d1117;font-family:var(--font-head);font-weight:700;font-size:0.9rem;padding:12px 28px;border:none;border-radius:var(--radius);cursor:pointer;transition:all 0.2s;letter-spacing:0.02em}
.btn-primary:hover{background:#52e8b8;transform:translateY(-1px)}
.btn-secondary{background:transparent;color:var(--text);font-family:var(--font-head);font-weight:600;font-size:0.9rem;padding:12px 28px;border:1px solid var(--border2);border-radius:var(--radius);cursor:pointer;transition:all 0.2s}
.btn-secondary:hover{border-color:var(--teal);color:var(--teal)}

.feature-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1px;background:var(--border);border-top:1px solid var(--border);max-width:900px;width:100%;margin:0 auto}
.feature-card{background:var(--bg);padding:2rem 1.5rem;cursor:pointer;transition:background 0.2s}
.feature-card:hover{background:var(--bg2)}
.feature-icon{font-size:1.8rem;margin-bottom:1rem}
.feature-card h3{font-family:var(--font-head);font-size:0.95rem;font-weight:700;margin-bottom:0.5rem;color:var(--text)}
.feature-card p{font-size:0.8rem;color:var(--muted);line-height:1.6}

/* ===== SECTION LAYOUT ===== */
.section-wrap{max-width:900px;margin:0 auto;padding:2rem 1.5rem}
.section-header{margin-bottom:2rem}
.section-header h2{font-family:var(--font-head);font-size:1.8rem;font-weight:800;letter-spacing:-0.02em;margin-bottom:0.5rem}
.section-header p{color:var(--muted);font-size:0.9rem}
.tag{display:inline-block;font-family:var(--font-mono);font-size:0.65rem;padding:3px 8px;border-radius:4px;font-weight:500;letter-spacing:0.05em}
.tag-teal{background:var(--teal-dim);color:var(--teal)}
.tag-amber{background:var(--amber-dim);color:var(--amber)}
.tag-coral{background:var(--coral-dim);color:var(--coral)}
.tag-blue{background:var(--blue-dim);color:var(--blue)}
.tag-purple{background:var(--purple-dim);color:var(--purple)}
.tag-green{background:var(--green-dim);color:var(--green)}

/* CARD */
.card{background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);padding:1.5rem;margin-bottom:1rem}
.card-sm{padding:1rem 1.25rem}

/* ===== IDENTIFIKASI ===== */
.question-track{display:flex;gap:6px;margin-bottom:2rem;flex-wrap:wrap}
.q-dot{width:28px;height:4px;border-radius:2px;background:var(--bg3);transition:background 0.3s}
.q-dot.done{background:var(--teal)}
.q-dot.active{background:var(--amber)}
.question-box{background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);padding:2rem}
.q-number{font-family:var(--font-mono);font-size:0.7rem;color:var(--muted);margin-bottom:0.75rem}
.q-text{font-family:var(--font-head);font-size:1.2rem;font-weight:700;margin-bottom:0.5rem}
.q-context{font-size:0.85rem;color:var(--muted);margin-bottom:1.5rem;font-style:italic}
.q-options{display:grid;grid-template-columns:1fr 1fr;gap:0.75rem}
.q-opt{background:var(--bg3);border:1px solid var(--border);border-radius:var(--radius);padding:1rem;cursor:pointer;transition:all 0.2s;text-align:left;color:var(--text);font-family:var(--font-body);font-size:0.9rem}
.q-opt:hover{border-color:var(--teal);background:var(--teal-dim)}
.q-opt.selected{border-color:var(--teal);background:var(--teal-dim);color:var(--teal)}
.q-opt-icon{font-size:1.2rem;margin-bottom:0.5rem}
.q-opt-label{font-weight:500}
.q-opt-desc{font-size:0.75rem;color:var(--muted);margin-top:4px}
.q-nav{display:flex;gap:1rem;margin-top:1.5rem;align-items:center}
.btn-ghost{background:none;border:1px solid var(--border2);color:var(--muted);padding:8px 16px;border-radius:8px;cursor:pointer;font-family:var(--font-body);font-size:0.85rem;transition:all 0.2s}
.btn-ghost:hover{color:var(--text);border-color:var(--text)}
.btn-next{background:var(--teal);color:#0d1117;border:none;padding:10px 24px;border-radius:8px;cursor:pointer;font-family:var(--font-head);font-weight:700;font-size:0.85rem;transition:all 0.2s;margin-left:auto}
.btn-next:hover{background:#52e8b8}
.btn-next:disabled{opacity:0.4;cursor:not-allowed}
.btn-reset{background:none;border:1px solid var(--coral-dim);color:var(--coral);padding:8px 16px;border-radius:8px;cursor:pointer;font-size:0.85rem;font-family:var(--font-body)}

/* HASIL */
.hasil-header{text-align:center;padding:2rem 0;border-bottom:1px solid var(--border);margin-bottom:1.5rem}
.hasil-header .score-big{font-family:var(--font-head);font-size:3rem;font-weight:800;color:var(--teal)}
.compound-result{background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);padding:1.25rem;margin-bottom:0.75rem}
.compound-result.high{border-color:var(--teal);background:var(--teal-dim)}
.compound-result.mid{border-color:var(--amber);background:var(--amber-dim)}
.compound-name{font-family:var(--font-head);font-size:1.1rem;font-weight:700;margin-bottom:0.25rem}
.compound-formula{font-family:var(--font-mono);font-size:0.8rem;color:var(--muted);margin-bottom:0.75rem}
.compound-explanation{font-size:0.85rem;color:var(--muted);line-height:1.6}
.match-bar{height:4px;border-radius:2px;background:var(--bg3);margin:0.5rem 0}
.match-fill{height:100%;border-radius:2px;background:var(--teal);transition:width 0.8s ease}
.match-fill.mid{background:var(--amber)}

/* ===== DATABASE ===== */
.search-box{position:relative;margin-bottom:1.5rem}
.search-box input{width:100%;background:var(--bg2);border:1px solid var(--border2);color:var(--text);padding:12px 16px 12px 44px;border-radius:var(--radius);font-size:0.9rem;font-family:var(--font-body);outline:none;transition:border-color 0.2s}
.search-box input:focus{border-color:var(--teal)}
.search-icon{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--muted);font-size:1.1rem}
.filter-row{display:flex;gap:0.5rem;margin-bottom:1.5rem;flex-wrap:wrap}
.filter-btn{background:var(--bg3);border:1px solid var(--border);color:var(--muted);padding:6px 14px;border-radius:20px;cursor:pointer;font-size:0.8rem;font-family:var(--font-mono);transition:all 0.2s}
.filter-btn.active,.filter-btn:hover{background:var(--teal-dim);border-color:var(--teal);color:var(--teal)}
.compound-table{width:100%;border-collapse:collapse}
.compound-table th{font-family:var(--font-mono);font-size:0.7rem;color:var(--muted);text-transform:uppercase;letter-spacing:0.08em;padding:8px 12px;text-align:left;border-bottom:1px solid var(--border);white-space:nowrap}
.compound-table td{padding:12px;border-bottom:1px solid var(--border);font-size:0.85rem;vertical-align:middle}
.compound-table tr:hover td{background:var(--bg3)}
.compound-table tr{cursor:pointer;transition:background 0.15s}
.mono{font-family:var(--font-mono);font-size:0.8rem;color:var(--muted)}

/* DETAIL MODAL */
.modal-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.7);z-index:200;align-items:center;justify-content:center;padding:1rem}
.modal-overlay.open{display:flex}
.modal{background:var(--bg2);border:1px solid var(--border2);border-radius:16px;padding:2rem;max-width:560px;width:100%;max-height:85vh;overflow-y:auto}
.modal-close{float:right;background:none;border:none;color:var(--muted);font-size:1.5rem;cursor:pointer;line-height:1}
.modal h3{font-family:var(--font-head);font-size:1.4rem;font-weight:800;margin-bottom:0.25rem}
.test-grid{display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;margin-top:1rem}
.test-item{background:var(--bg3);border-radius:8px;padding:0.75rem 1rem;font-size:0.8rem}
.test-item .test-name{font-family:var(--font-mono);font-size:0.7rem;color:var(--muted);margin-bottom:0.25rem}
.test-item .test-result{font-weight:500}
.test-item.positive .test-result{color:var(--teal)}
.test-item.negative .test-result{color:var(--coral)}

/* ===== SIMULASI ===== */
.sim-layout{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem}
@media(max-width:640px){.sim-layout{grid-template-columns:1fr}}
.sim-select-label{font-family:var(--font-mono);font-size:0.7rem;color:var(--muted);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.75rem}
.sim-chips{display:flex;flex-wrap:wrap;gap:0.5rem;margin-bottom:1.5rem}
.sim-chip{background:var(--bg3);border:1px solid var(--border);color:var(--muted);padding:8px 14px;border-radius:20px;cursor:pointer;font-size:0.85rem;font-family:var(--font-body);transition:all 0.2s}
.sim-chip.active{background:var(--blue-dim);border-color:var(--blue);color:var(--blue)}
.sim-chip.test-chip.active{background:var(--purple-dim);border-color:var(--purple);color:var(--purple)}
.btn-sim{background:var(--teal);color:#0d1117;font-family:var(--font-head);font-weight:700;padding:12px 32px;border:none;border-radius:var(--radius);cursor:pointer;font-size:0.9rem;transition:all 0.2s;width:100%;margin-top:0.5rem}
.btn-sim:hover{background:#52e8b8}
.btn-sim:disabled{opacity:0.4;cursor:not-allowed}

.result-panel{background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);padding:1.5rem;min-height:300px}
.result-panel.empty{display:flex;align-items:center;justify-content:center;flex-direction:column;gap:1rem;color:var(--muted)}
.result-panel .result-title{font-family:var(--font-head);font-size:1rem;font-weight:700;margin-bottom:1rem;color:var(--muted)}
.test-result-item{border-left:3px solid var(--border2);padding:0.75rem 1rem;margin-bottom:0.75rem;border-radius:0 8px 8px 0}
.test-result-item.positive{border-color:var(--teal);background:var(--teal-dim)}
.test-result-item.negative{border-color:var(--coral);background:var(--coral-dim)}
.test-result-item .r-test{font-family:var(--font-mono);font-size:0.7rem;color:var(--muted);margin-bottom:4px}
.test-result-item .r-status{font-weight:600;font-size:0.95rem;margin-bottom:4px}
.test-result-item.positive .r-status{color:var(--teal)}
.test-result-item.negative .r-status{color:var(--coral)}
.test-result-item .r-desc{font-size:0.8rem;color:var(--muted);line-height:1.5}
.conclusion-box{background:var(--bg3);border-radius:8px;padding:1rem;margin-top:1rem}
.conclusion-box .c-label{font-family:var(--font-mono);font-size:0.7rem;color:var(--muted);margin-bottom:6px}
.conclusion-box .c-text{font-size:0.9rem;color:var(--text)}

/* ===== KUIS ===== */
.quiz-progress{display:flex;align-items:center;gap:1rem;margin-bottom:2rem}
.quiz-bar{flex:1;height:4px;background:var(--bg3);border-radius:2px;overflow:hidden}
.quiz-bar-fill{height:100%;background:var(--purple);transition:width 0.4s ease}
.quiz-score-live{font-family:var(--font-mono);font-size:0.8rem;color:var(--purple)}
.quiz-q-box{background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);padding:2rem;margin-bottom:1rem}
.quiz-q-num{font-family:var(--font-mono);font-size:0.7rem;color:var(--muted);margin-bottom:0.75rem}
.quiz-q-text{font-family:var(--font-head);font-size:1.1rem;font-weight:700;line-height:1.4;margin-bottom:0.5rem}
.quiz-scenario{font-size:0.85rem;color:var(--amber);font-style:italic;margin-bottom:1.5rem;padding:0.75rem 1rem;background:var(--amber-dim);border-radius:8px;border-left:3px solid var(--amber)}
.quiz-opts{display:flex;flex-direction:column;gap:0.65rem}
.quiz-opt{background:var(--bg3);border:1px solid var(--border);border-radius:var(--radius);padding:1rem 1.25rem;cursor:pointer;transition:all 0.2s;font-size:0.9rem;font-family:var(--font-body);text-align:left;color:var(--text);display:flex;align-items:center;gap:0.75rem}
.quiz-opt:hover:not(:disabled){border-color:var(--purple);background:var(--purple-dim)}
.quiz-opt.correct{border-color:var(--green);background:var(--green-dim);color:var(--green)}
.quiz-opt.wrong{border-color:var(--coral);background:var(--coral-dim);color:var(--coral)}
.quiz-opt:disabled{cursor:not-allowed}
.opt-letter{width:28px;height:28px;border-radius:50%;border:1px solid var(--border2);display:flex;align-items:center;justify-content:center;font-family:var(--font-mono);font-size:0.75rem;flex-shrink:0;transition:all 0.2s}
.quiz-opt.correct .opt-letter{background:var(--green);color:#000;border-color:var(--green)}
.quiz-opt.wrong .opt-letter{background:var(--coral);color:#fff;border-color:var(--coral)}
.quiz-feedback{background:var(--bg3);border-radius:8px;padding:1rem 1.25rem;font-size:0.85rem;color:var(--muted);line-height:1.6;margin-top:0.75rem}
.quiz-feedback strong{color:var(--text)}
.btn-quiz-next{background:var(--purple);color:#fff;border:none;padding:10px 24px;border-radius:8px;cursor:pointer;font-family:var(--font-head);font-weight:700;font-size:0.85rem;margin-left:auto;display:block;margin-top:1rem;transition:all 0.2s}
.btn-quiz-next:hover{opacity:0.85}
.quiz-final{text-align:center;padding:3rem 2rem;background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius)}
.quiz-final-score{font-family:var(--font-head);font-size:4rem;font-weight:800;line-height:1}
.quiz-grade{font-size:1rem;font-family:var(--font-mono);margin:0.5rem 0 1.5rem}

/* ===== MATERI ===== */
.materi-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1rem}
.materi-card{background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);padding:1.5rem;cursor:pointer;transition:all 0.2s}
.materi-card:hover{border-color:var(--teal);transform:translateY(-2px)}
.materi-icon{font-size:2rem;margin-bottom:1rem}
.materi-card h3{font-family:var(--font-head);font-size:1rem;font-weight:700;margin-bottom:0.5rem}
.materi-card p{font-size:0.8rem;color:var(--muted);line-height:1.5}
.materi-detail{display:none;background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);padding:2rem;margin-top:1rem}
.materi-detail.open{display:block}
.materi-detail h3{font-family:var(--font-head);font-size:1.3rem;font-weight:800;margin-bottom:1rem}
.materi-detail h4{font-family:var(--font-head);font-size:0.95rem;font-weight:700;margin:1.25rem 0 0.5rem;color:var(--teal)}
.materi-detail p,.materi-detail li{font-size:0.9rem;color:var(--muted);line-height:1.7}
.materi-detail ul{padding-left:1.5rem;margin-bottom:0.75rem}
.materi-detail .formula{font-family:var(--font-mono);background:var(--bg3);padding:4px 10px;border-radius:6px;font-size:0.85rem;color:var(--teal)}
.btn-back-materi{background:none;border:1px solid var(--border2);color:var(--muted);padding:8px 16px;border-radius:8px;cursor:pointer;font-family:var(--font-body);font-size:0.85rem;margin-bottom:1.5rem}

/* TENTANG */
.about-hero{text-align:center;padding:3rem 2rem;max-width:640px;margin:0 auto}
.about-hero h2{font-family:var(--font-head);font-size:2rem;font-weight:800;margin-bottom:1rem}
.team-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:1rem;margin-top:2rem}
.uji-ref{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1rem;margin-top:1.5rem}
.uji-card{background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);padding:1.25rem}
.uji-card h4{font-family:var(--font-head);font-size:0.9rem;font-weight:700;margin-bottom:0.5rem}
.uji-card p{font-size:0.8rem;color:var(--muted);line-height:1.5}

/* GRID DOTS BG */
.grid-bg{position:fixed;inset:0;pointer-events:none;z-index:-1;opacity:0.03;background-image:radial-gradient(circle,#fff 1px,transparent 1px);background-size:28px 28px}

/* RESPONSIVE */
@media(max-width:600px){
  .q-options{grid-template-columns:1fr}
  .sim-layout{grid-template-columns:1fr}
  nav{padding:0 1rem}
  .section-wrap{padding:1.5rem 1rem}
}

/* ANIMATION */
@keyframes fadeUp{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}
.page.active .section-wrap,.page.active .hero{animation:fadeUp 0.4s ease both}
</style>
</head>
<body>
<div class="grid-bg"></div>

<!-- NAV -->
<nav>
  <div class="nav-logo" onclick="showPage('home')">OrganIQ</div>
  <div class="nav-links">
    <button class="nav-link" onclick="showPage('identifikasi')">Identifikasi</button>
    <button class="nav-link" onclick="showPage('database')">Database</button>
    <button class="nav-link" onclick="showPage('simulasi')">Simulasi</button>
    <button class="nav-link" onclick="showPage('kuis')">Kuis</button>
    <button class="nav-link" onclick="showPage('materi')">Materi</button>
    <button class="nav-link" onclick="showPage('tentang')">Tentang</button>
  </div>
</nav>

<!-- HOME -->
<div id="page-home" class="page active">
  <div class="hero">
    <div class="hero-eyebrow">Laboratorium Digital Kimia Organik</div>
    <h1>Identifikasi<br><span>Senyawa Organik</span><br>secara Kualitatif</h1>
    <p>Platform edukasi interaktif untuk mengidentifikasi golongan senyawa organik berdasarkan uji laboratorium — uji Tollens, Baeyer, Bromin, Iodoform, dan lainnya.</p>
    <div class="hero-btns">
      <button class="btn-primary" onclick="showPage('identifikasi')">▶ Mulai Identifikasi</button>
      <button class="btn-secondary" onclick="showPage('materi')">Pelajari Materi</button>
      <button class="btn-secondary" onclick="showPage('kuis')">Uji Kemampuan</button>
    </div>
  </div>
  <div class="feature-grid">
    <div class="feature-card" onclick="showPage('identifikasi')">
      <div class="feature-icon">🧪</div>
      <h3>Identifikasi Senyawa</h3>
      <p>Jawab serangkaian pertanyaan uji dan dapatkan kemungkinan golongan senyawa sampelmu.</p>
    </div>
    <div class="feature-card" onclick="showPage('database')">
      <div class="feature-icon">🗃️</div>
      <h3>Database Senyawa</h3>
      <p>Cari dan telusuri 30+ senyawa organik dengan data uji kualitatif lengkap.</p>
    </div>
    <div class="feature-card" onclick="showPage('simulasi')">
      <div class="feature-icon">⚗️</div>
      <h3>Simulasi Praktikum</h3>
      <p>Simulasikan reaksi uji kualitatif antara berbagai sampel dan pereaksi laboratorium.</p>
    </div>
    <div class="feature-card" onclick="showPage('kuis')">
      <div class="feature-icon">🎯</div>
      <h3>Kuis Interaktif</h3>
      <p>Uji pemahamanmu dengan 10 soal pilihan ganda yang disertai penjelasan lengkap.</p>
    </div>
  </div>
</div>

<!-- IDENTIFIKASI -->
<div id="page-identifikasi" class="page">
<div class="section-wrap">
  <div class="section-header">
    <h2>Identifikasi Senyawa</h2>
    <p>Jawab pertanyaan berdasarkan hasil pengujian laboratoriummu, sistem akan menganalisis kemungkinan golongan senyawa.</p>
  </div>
  <div id="id-quiz-area"></div>
</div>
</div>

<!-- DATABASE -->
<div id="page-database" class="page">
<div class="section-wrap">
  <div class="section-header">
    <h2>Database Senyawa Organik</h2>
    <p>Klik baris senyawa untuk melihat detail uji kualitatif lengkap.</p>
  </div>
  <div class="search-box">
    <span class="search-icon">🔍</span>
    <input type="text" id="db-search" placeholder="Cari nama senyawa, rumus, atau golongan..." oninput="filterDB()">
  </div>
  <div class="filter-row" id="db-filters"></div>
  <div style="overflow-x:auto">
    <table class="compound-table" id="compound-table">
      <thead>
        <tr>
          <th>Senyawa</th>
          <th>Rumus</th>
          <th>Golongan</th>
          <th>Uji Positif</th>
          <th>Uji Negatif</th>
        </tr>
      </thead>
      <tbody id="compound-tbody"></tbody>
    </table>
  </div>
</div>
</div>

<!-- SIMULASI -->
<div id="page-simulasi" class="page">
<div class="section-wrap">
  <div class="section-header">
    <h2>Simulasi Praktikum</h2>
    <p>Pilih senyawa sampel dan pereaksi, lalu amati hasil simulasinya.</p>
  </div>
  <div class="sim-layout">
    <div>
      <div class="sim-select-label">Pilih Sampel</div>
      <div class="sim-chips" id="sim-samples"></div>
      <div class="sim-select-label" style="margin-top:1rem">Pilih Uji (bisa lebih dari satu)</div>
      <div class="sim-chips" id="sim-tests"></div>
      <button class="btn-sim" onclick="runSim()" id="btn-sim" disabled>Jalankan Simulasi</button>
    </div>
    <div class="result-panel empty" id="sim-result">
      <div style="font-size:2rem">⚗️</div>
      <div>Pilih sampel dan pereaksi untuk memulai simulasi</div>
    </div>
  </div>
</div>
</div>

<!-- KUIS -->
<div id="page-kuis" class="page">
<div class="section-wrap">
  <div class="section-header">
    <h2>Kuis Uji Kualitatif</h2>
    <p>10 soal pilihan ganda dengan penjelasan. Nilai langsung muncul setelah menjawab.</p>
  </div>
  <div id="quiz-area"></div>
</div>
</div>

<!-- MATERI -->
<div id="page-materi" class="page">
<div class="section-wrap">
  <div class="section-header">
    <h2>Materi Uji Kualitatif</h2>
    <p>Pelajari prinsip dan interpretasi berbagai uji kualitatif senyawa organik.</p>
  </div>
  <div id="materi-content"></div>
</div>
</div>

<!-- TENTANG -->
<div id="page-tentang" class="page">
<div class="section-wrap">
  <div class="about-hero">
    <div class="tag tag-teal" style="margin-bottom:1rem">v1.0 · 2025</div>
    <h2>Tentang OrganIQ</h2>
    <p style="color:var(--muted);font-size:0.95rem;line-height:1.8">OrganIQ adalah platform edukasi digital untuk identifikasi senyawa organik berdasarkan uji kualitatif laboratorium. Dirancang untuk membantu mahasiswa, pelajar, dan praktisi kimia memahami karakteristik senyawa organik melalui pendekatan sistematis dan interaktif.</p>
  </div>
  <div class="uji-ref">
    <div class="uji-card">
      <h4>🧫 Uji Tollens</h4>
      <p>Menggunakan larutan [Ag(NH₃)₂]⁺. Positif: terbentuk cermin perak. Mengidentifikasi <strong>aldehid</strong>.</p>
    </div>
    <div class="uji-card">
      <h4>🟠 Uji Baeyer</h4>
      <p>Menggunakan KMnO₄ alkali (encer). Positif: larutan ungu berubah coklat/bening. Mengidentifikasi <strong>ikatan rangkap (alkena/alkuna)</strong>.</p>
    </div>
    <div class="uji-card">
      <h4>🟤 Uji Bromin</h4>
      <p>Menggunakan Br₂/CCl₄. Positif: warna merah-coklat hilang (dekolorisasi). Mengidentifikasi <strong>alkena, alkuna, fenol, aldehid</strong>.</p>
    </div>
    <div class="uji-card">
      <h4>🟡 Uji Iodoform</h4>
      <p>Menggunakan I₂/NaOH. Positif: endapan kuning CHI₃. Mengidentifikasi <strong>metil keton dan etanol</strong>.</p>
    </div>
    <div class="uji-card">
      <h4>🔵 Uji FeCl₃</h4>
      <p>Menggunakan FeCl₃ encer. Positif: warna ungu-violet. Mengidentifikasi <strong>fenol</strong>.</p>
    </div>
    <div class="uji-card">
      <h4>🔴 Uji 2,4-DNPH</h4>
      <p>Menggunakan 2,4-dinitrofenilhidrazin. Positif: endapan kuning/oranye. Mengidentifikasi <strong>aldehid dan keton</strong>.</p>
    </div>
    <div class="uji-card">
      <h4>🟢 Uji Biuret</h4>
      <p>Menggunakan NaOH + CuSO₄. Positif: warna ungu-merah muda. Mengidentifikasi <strong>protein (ikatan peptida)</strong>.</p>
    </div>
    <div class="uji-card">
      <h4>🟣 Uji Molisch</h4>
      <p>Menggunakan α-naftol + H₂SO₄ pekat. Positif: cincin ungu. Mengidentifikasi <strong>karbohidrat</strong>.</p>
    </div>
    <div class="uji-card">
      <h4>🟥 Uji Lucas</h4>
      <p>Menggunakan ZnCl₂ + HCl. Positif: kekeruhan/lapisan terpisah. Membedakan <strong>alkohol primer, sekunder, tersier</strong>.</p>
    </div>
  </div>
  <div style="text-align:center;margin-top:3rem;color:var(--muted);font-size:0.8rem;font-family:var(--font-mono)">
    Dibuat untuk keperluan edukasi kimia organik · OrganIQ 2025
  </div>
</div>
</div>

<!-- MODAL -->
<div class="modal-overlay" id="modal-overlay" onclick="closeModal(event)">
  <div class="modal" id="modal-content"></div>
</div>

<script>
// ===== DATA =====
const COMPOUNDS = [
  {name:'Metanol',formula:'CH₃OH',group:'Alkohol',tests:{tollens:'neg',baeyer:'neg',bromin:'neg',iodoform:'neg',dnph:'neg',fecl3:'neg',lucas:'neg (lambat)',biuret:'neg',molisch:'neg',esterifikasi:'pos',lakmus:'neg'},desc:'Alkohol paling sederhana. Bersifat racun. Larut sempurna dalam air.',positive:['Esterifikasi','Uji Na logam'],negative:['Tollens','Iodoform']},
  {name:'Etanol',formula:'C₂H₅OH',group:'Alkohol',tests:{tollens:'neg',baeyer:'neg',bromin:'neg',iodoform:'pos',dnph:'neg',fecl3:'neg',lucas:'neg (lambat)',biuret:'neg',molisch:'neg',esterifikasi:'pos',lakmus:'neg'},desc:'Alkohol paling umum, terdapat dalam minuman beralkohol.',positive:['Iodoform','Esterifikasi'],negative:['Tollens','DNPH']},
  {name:'2-Propanol',formula:'(CH₃)₂CHOH',group:'Alkohol',tests:{tollens:'neg',baeyer:'neg',bromin:'neg',iodoform:'pos',dnph:'neg',fecl3:'neg',lucas:'pos (sedang)',biuret:'neg',molisch:'neg',esterifikasi:'pos',lakmus:'neg'},desc:'Isopropanol, alkohol sekunder. Digunakan sebagai antiseptik.',positive:['Iodoform','Lucas (sedang)'],negative:['Tollens','DNPH']},
  {name:'Formaldehid',formula:'HCHO',group:'Aldehid',tests:{tollens:'pos',baeyer:'neg',bromin:'pos',iodoform:'neg',dnph:'pos',fecl3:'neg',lucas:'neg',biuret:'neg',molisch:'neg',esterifikasi:'neg',lakmus:'neg'},desc:'Aldehid paling sederhana. Gas berbau menyengat, digunakan sebagai formalin.',positive:['Tollens','DNPH','Bromin'],negative:['Baeyer','Iodoform']},
  {name:'Asetaldehid',formula:'CH₃CHO',group:'Aldehid',tests:{tollens:'pos',baeyer:'neg',bromin:'pos',iodoform:'pos',dnph:'pos',fecl3:'neg',lucas:'neg',biuret:'neg',molisch:'neg',esterifikasi:'neg',lakmus:'neg'},desc:'Aldehid dengan gugus metil. Bersifat reaktif, mudah teroksidasi.',positive:['Tollens','Iodoform','DNPH'],negative:['Baeyer','FeCl₃']},
  {name:'Benzaldehid',formula:'C₆H₅CHO',group:'Aldehid',tests:{tollens:'pos',baeyer:'neg',bromin:'neg',iodoform:'neg',dnph:'pos',fecl3:'neg',lucas:'neg',biuret:'neg',molisch:'neg',esterifikasi:'neg',lakmus:'neg'},desc:'Aldehid aromatik dengan aroma almond. Tidak bereaksi dengan iodoform.',positive:['Tollens','DNPH'],negative:['Iodoform','Baeyer']},
  {name:'Aseton',formula:'CH₃COCH₃',group:'Keton',tests:{tollens:'neg',baeyer:'neg',bromin:'neg',iodoform:'pos',dnph:'pos',fecl3:'neg',lucas:'neg',biuret:'neg',molisch:'neg',esterifikasi:'neg',lakmus:'neg'},desc:'Keton paling sederhana. Pelarut organik yang umum digunakan.',positive:['Iodoform','DNPH'],negative:['Tollens','Baeyer']},
  {name:'Metil Etil Keton',formula:'CH₃COC₂H₅',group:'Keton',tests:{tollens:'neg',baeyer:'neg',bromin:'neg',iodoform:'pos',dnph:'pos',fecl3:'neg',lucas:'neg',biuret:'neg',molisch:'neg',esterifikasi:'neg',lakmus:'neg'},desc:'Butanon/MEK, keton asimetris. Pelarut industri yang penting.',positive:['Iodoform','DNPH'],negative:['Tollens','FeCl₃']},
  {name:'Sikloheksanon',formula:'C₆H₁₀O',group:'Keton',tests:{tollens:'neg',baeyer:'neg',bromin:'neg',iodoform:'neg',dnph:'pos',fecl3:'neg',lucas:'neg',biuret:'neg',molisch:'neg',esterifikasi:'neg',lakmus:'neg'},desc:'Keton siklik. Iodoform negatif karena bukan metil keton.',positive:['DNPH'],negative:['Tollens','Iodoform']},
  {name:'Asam Asetat',formula:'CH₃COOH',group:'Asam Karboksilat',tests:{tollens:'neg',baeyer:'neg',bromin:'neg',iodoform:'neg',dnph:'neg',fecl3:'neg',lucas:'neg',biuret:'neg',molisch:'neg',esterifikasi:'pos',lakmus:'pos'},desc:'Asam asetat, komponen utama cuka. Asam organik lemah.',positive:['Lakmus merah','Esterifikasi','Na₂CO₃ (gelembung)'],negative:['Tollens','DNPH']},
  {name:'Asam Format',formula:'HCOOH',group:'Asam Karboksilat',tests:{tollens:'pos',baeyer:'neg',bromin:'neg',iodoform:'neg',dnph:'neg',fecl3:'neg',lucas:'neg',biuret:'neg',molisch:'neg',esterifikasi:'pos',lakmus:'pos'},desc:'Asam format. Unik karena memiliki gugus aldehid tersembunyi, bereaksi positif Tollens.',positive:['Tollens (unik)','Lakmus','Esterifikasi'],negative:['DNPH','Iodoform']},
  {name:'Asam Benzoat',formula:'C₆H₅COOH',group:'Asam Karboksilat',tests:{tollens:'neg',baeyer:'neg',bromin:'neg',iodoform:'neg',dnph:'neg',fecl3:'pos',lucas:'neg',biuret:'neg',molisch:'neg',esterifikasi:'pos',lakmus:'pos'},desc:'Asam karboksilat aromatik. Memberikan warna dengan FeCl₃.',positive:['Lakmus','FeCl₃ (kuning)','Esterifikasi'],negative:['Tollens','DNPH']},
  {name:'Fenol',formula:'C₆H₅OH',group:'Fenol',tests:{tollens:'neg',baeyer:'neg',bromin:'pos',iodoform:'neg',dnph:'neg',fecl3:'pos',lucas:'neg',biuret:'neg',molisch:'neg',esterifikasi:'neg',lakmus:'pos'},desc:'Fenol, alkohol aromatik. Bereaksi kuat dengan FeCl₃ menghasilkan warna violet.',positive:['FeCl₃ (violet)','Bromin (putih↓)','Lakmus'],negative:['Tollens','Iodoform']},
  {name:'Kresol',formula:'CH₃C₆H₄OH',group:'Fenol',tests:{tollens:'neg',baeyer:'neg',bromin:'pos',iodoform:'neg',dnph:'neg',fecl3:'pos',lucas:'neg',biuret:'neg',molisch:'neg',esterifikasi:'neg',lakmus:'pos'},desc:'Metil fenol (isomer orto, meta, para). Digunakan sebagai antiseptik.',positive:['FeCl₃','Bromin'],negative:['Tollens','DNPH']},
  {name:'Etil Asetat',formula:'CH₃COOC₂H₅',group:'Ester',tests:{tollens:'neg',baeyer:'neg',bromin:'neg',iodoform:'neg',dnph:'neg',fecl3:'neg',lucas:'neg',biuret:'neg',molisch:'neg',esterifikasi:'neg',lakmus:'neg',hidrolisis:'pos'},desc:'Ester paling umum. Berbau harum (buah pir). Dapat dihidrolisis dengan asam/basa.',positive:['Hidrolisis (bau↓, asam terbentuk)'],negative:['Tollens','DNPH','FeCl₃']},
  {name:'Metil Salisilat',formula:'C₈H₈O₃',group:'Ester',tests:{tollens:'neg',baeyer:'neg',bromin:'neg',iodoform:'neg',dnph:'neg',fecl3:'pos',lucas:'neg',biuret:'neg',molisch:'neg',esterifikasi:'neg',hidrolisis:'pos'},desc:'Ester fenol. Setelah hidrolisis menghasilkan fenol yang bereaksi FeCl₃.',positive:['FeCl₃ (setelah hidrolisis)','Hidrolisis'],negative:['Tollens','DNPH']},
  {name:'Etilena (Etena)',formula:'CH₂=CH₂',group:'Alkena',tests:{tollens:'neg',baeyer:'pos',bromin:'pos',iodoform:'neg',dnph:'neg',fecl3:'neg',lucas:'neg',biuret:'neg',molisch:'neg',esterifikasi:'neg',lakmus:'neg'},desc:'Alkena paling sederhana. Gas tidak berwarna, penting dalam industri plastik.',positive:['Baeyer (KMnO₄ coklat)','Bromin (dekolorisasi)'],negative:['Tollens','DNPH']},
  {name:'1-Butena',formula:'CH₃CH₂CH=CH₂',group:'Alkena',tests:{tollens:'neg',baeyer:'pos',bromin:'pos',iodoform:'neg',dnph:'neg',fecl3:'neg',lucas:'neg',biuret:'neg',molisch:'neg',esterifikasi:'neg',lakmus:'neg'},desc:'Alkena rantai lurus. Bereaksi adisi dengan bromin dan dioksidasi oleh KMnO₄.',positive:['Baeyer','Bromin'],negative:['Tollens','Iodoform']},
  {name:'Sikloheksena',formula:'C₆H₁₀',group:'Alkena',tests:{tollens:'neg',baeyer:'pos',bromin:'pos',iodoform:'neg',dnph:'neg',fecl3:'neg',lucas:'neg',biuret:'neg',molisch:'neg',esterifikasi:'neg',lakmus:'neg'},desc:'Alkena siklik. Ikatan rangkap reaktif terhadap reagen Baeyer dan bromin.',positive:['Baeyer','Bromin'],negative:['Tollens','FeCl₃']},
  {name:'Asetilena',formula:'HC≡CH',group:'Alkuna',tests:{tollens:'neg',baeyer:'pos',bromin:'pos',iodoform:'neg',dnph:'neg',fecl3:'neg',lucas:'neg',biuret:'neg',molisch:'neg',esterifikasi:'neg',lakmus:'neg'},desc:'Alkuna terminal paling sederhana. Bereaksi dengan AgNO₃ menghasilkan endapan putih.',positive:['Baeyer','Bromin','AgNO₃ (endapan)'],negative:['Tollens','DNPH']},
  {name:'Glukosa',formula:'C₆H₁₂O₆',group:'Karbohidrat',tests:{tollens:'pos',baeyer:'neg',bromin:'neg',iodoform:'neg',dnph:'neg',fecl3:'neg',lucas:'neg',biuret:'neg',molisch:'pos',fehling:'pos',lakmus:'neg'},desc:'Monosakarida aldosa. Memiliki gugus aldehid bebas yang mereduksi pereaksi Tollens dan Fehling.',positive:['Tollens','Fehling/Benedict','Molisch'],negative:['Iodine (tidak berwarna biru)']},
  {name:'Fruktosa',formula:'C₆H₁₂O₆',group:'Karbohidrat',tests:{tollens:'pos',baeyer:'neg',bromin:'neg',iodoform:'neg',dnph:'neg',fecl3:'neg',lucas:'neg',biuret:'neg',molisch:'pos',fehling:'pos',lakmus:'neg'},desc:'Monosakarida ketosa. Gula termanis, meskipun ketosa tetap mereduksi karena isomerisasi.',positive:['Tollens (melalui isomerisasi)','Fehling','Molisch'],negative:['Iodine']},
  {name:'Amilum (Pati)',formula:'(C₆H₁₀O₅)ₙ',group:'Karbohidrat',tests:{tollens:'neg',baeyer:'neg',bromin:'neg',iodoform:'neg',dnph:'neg',fecl3:'neg',lucas:'neg',biuret:'neg',molisch:'pos',iodine:'pos',lakmus:'neg'},desc:'Polisakarida non-pereduksi. Bereaksi khas dengan larutan iodin menghasilkan warna biru-hitam.',positive:['Iodine (biru-hitam)','Molisch','Hidrolisis → Glukosa'],negative:['Tollens (tidak mereduksi)']},
  {name:'Selulosa',formula:'(C₆H₁₀O₅)ₙ',group:'Karbohidrat',tests:{tollens:'neg',baeyer:'neg',bromin:'neg',iodoform:'neg',dnph:'neg',fecl3:'neg',lucas:'neg',biuret:'neg',molisch:'pos',iodine:'neg',lakmus:'neg'},desc:'Polisakarida struktural tumbuhan. Tidak bereaksi dengan iodin karena struktur ikatan β-glikosidik.',positive:['Molisch','Hidrolisis → Glukosa'],negative:['Iodine','Tollens']},
  {name:'Albumin',formula:'Protein',group:'Protein',tests:{tollens:'neg',baeyer:'neg',bromin:'neg',iodoform:'neg',dnph:'neg',fecl3:'neg',lucas:'neg',biuret:'pos',xantoproteat:'pos',ninhydrin:'pos',lakmus:'neg'},desc:'Protein plasma darah. Mengandung ikatan peptida dan residu asam amino aromatik.',positive:['Biuret (ungu)','Xantoproteat (kuning)','Ninhydrin (ungu)'],negative:['Tollens','DNPH']},
  {name:'Kasein',formula:'Protein',group:'Protein',tests:{tollens:'neg',baeyer:'neg',bromin:'neg',iodoform:'neg',dnph:'neg',fecl3:'neg',lucas:'neg',biuret:'pos',xantoproteat:'pos',ninhydrin:'pos',lakmus:'neg'},desc:'Protein susu. Mengandung semua asam amino esensial.',positive:['Biuret','Xantoproteat','Ninhydrin'],negative:['Tollens','Molisch']},
  {name:'Benzena',formula:'C₆H₆',group:'Aromatik',tests:{tollens:'neg',baeyer:'neg',bromin:'neg',iodoform:'neg',dnph:'neg',fecl3:'neg',lucas:'neg',biuret:'neg',molisch:'neg',lakmus:'neg'},desc:'Senyawa aromatik paling sederhana. Sangat stabil, tidak bereaksi dengan Br₂/CCl₄ tanpa katalis.',positive:['Nitrasi (dengan HNO₃/H₂SO₄)'],negative:['Bromin (tanpa katalis)','Baeyer']},
  {name:'Toluena',formula:'C₆H₅CH₃',group:'Aromatik',tests:{tollens:'neg',baeyer:'neg',bromin:'neg',iodoform:'neg',dnph:'neg',fecl3:'neg',lucas:'neg',biuret:'neg',molisch:'neg',lakmus:'neg'},desc:'Metilbenzena. Pelarut organik yang umum. Gugus metil aktifkan cincin aromatik.',positive:['Nitrasi'],negative:['Bromin (tanpa katalis)','Tollens']},
  {name:'Naftalena',formula:'C₁₀H₈',group:'Aromatik',tests:{tollens:'neg',baeyer:'neg',bromin:'neg',iodoform:'neg',dnph:'neg',fecl3:'neg',lucas:'neg',biuret:'neg',molisch:'neg',lakmus:'neg'},desc:'PAH paling sederhana. Berbentuk padatan kristal dengan bau khas (kapur barus).',positive:['Nitrasi (reaktif)'],negative:['Bromin (tanpa katalis)','Baeyer']},
  {name:'Glisin',formula:'H₂NCH₂COOH',group:'Asam Amino',tests:{tollens:'neg',baeyer:'neg',bromin:'neg',iodoform:'neg',dnph:'neg',fecl3:'neg',lucas:'neg',biuret:'neg',ninhydrin:'pos',lakmus:'amfoter'},desc:'Asam amino paling sederhana (tidak punya rantai samping). Bersifat amfoter.',positive:['Ninhydrin (ungu)','Biuret (setelah kondensasi)'],negative:['Tollens','DNPH']},
];

const GOLONGAN_TAGS = [...new Set(COMPOUNDS.map(c=>c.group))];

// ===== IDENTIFIKASI DATA =====
const ID_QUESTIONS = [
  {id:'q1',text:'Apakah sampel larut dalam air?',context:'Tambahkan 5 tetes sampel ke 2 mL air distilat, kocok.',opts:[{label:'Ya — larut',desc:'Homogen, tidak ada lapisan',val:'larut'},{label:'Tidak — tidak larut',desc:'Terbentuk lapisan atau kekeruhan',val:'tidak_larut'}]},
  {id:'q2',text:'Apakah sampel mengubah warna kertas lakmus merah?',context:'Celupkan kertas lakmus merah ke dalam larutan sampel.',opts:[{label:'Ya — menjadi biru',desc:'Menunjukkan sifat basa',val:'basa'},{label:'Tidak berubah / merah tetap',desc:'Netral atau asam',val:'netral_asam'}]},
  {id:'q3',text:'Apakah sampel bereaksi positif pada uji Tollens?',context:'Tambahkan 2 mL reagen Tollens ke sampel, hangatkan 60°C.',opts:[{label:'Ya — terbentuk cermin perak',desc:'Endapan perak pada dinding tabung',val:'tollens_pos'},{label:'Tidak ada cermin perak',desc:'Larutan tetap bening',val:'tollens_neg'}]},
  {id:'q4',text:'Apakah sampel bereaksi positif pada uji 2,4-DNPH?',context:'Tambahkan 1 mL reagen Brady ke sampel, kocok.',opts:[{label:'Ya — endapan kuning/oranye',desc:'Terbentuk presipitat berwarna',val:'dnph_pos'},{label:'Tidak ada endapan',desc:'Larutan tetap bening',val:'dnph_neg'}]},
  {id:'q5',text:'Apakah terjadi dekolorisasi larutan bromin (Br₂)?',context:'Tambahkan 3 tetes Br₂ dalam CCl₄ ke sampel.',opts:[{label:'Ya — warna merah-coklat hilang',desc:'Dekolorisasi terjadi spontan',val:'bromin_pos'},{label:'Tidak — warna tetap',desc:'Larutan bromin tetap berwarna',val:'bromin_neg'}]},
  {id:'q6',text:'Apakah larutan KMnO₄ mengalami dekolorisasi (uji Baeyer)?',context:'Tambahkan beberapa tetes larutan KMnO₄ encer ke sampel.',opts:[{label:'Ya — ungu menjadi coklat/bening',desc:'KMnO₄ tereduksi',val:'baeyer_pos'},{label:'Tidak — tetap ungu',desc:'Tidak terjadi reduksi',val:'baeyer_neg'}]},
  {id:'q7',text:'Apakah sampel bereaksi positif pada uji Iodoform?',context:'Tambahkan I₂/NaOH ke sampel, hangatkan sedikit.',opts:[{label:'Ya — endapan kuning CHI₃',desc:'Bau khas iodoform terbentuk',val:'iodoform_pos'},{label:'Tidak ada endapan kuning',desc:'Tidak ada reaksi positif',val:'iodoform_neg'}]},
  {id:'q8',text:'Apakah uji FeCl₃ memberikan warna ungu/violet?',context:'Tambahkan 1-2 tetes larutan FeCl₃ encer ke sampel.',opts:[{label:'Ya — warna ungu/violet',desc:'Kompleks besi-fenolat terbentuk',val:'fecl3_pos'},{label:'Tidak — tidak ada warna khas',desc:'Tidak ada perubahan warna ungu',val:'fecl3_neg'}]},
  {id:'q9',text:'Apakah uji Biuret memberikan warna ungu?',context:'Tambahkan NaOH encer, lalu 1-2 tetes CuSO₄ encer.',opts:[{label:'Ya — warna ungu',desc:'Ikatan peptida terdeteksi',val:'biuret_pos'},{label:'Tidak — biru pucat atau tidak ada',desc:'Bukan protein',val:'biuret_neg'}]},
  {id:'q10',text:'Apakah uji Molisch memberikan cincin ungu?',context:'Tambahkan 2 tetes reagen Molisch, miringkan tabung, alirkan H₂SO₄ pekat.',opts:[{label:'Ya — cincin ungu terbentuk',desc:'Karbohidrat terdeteksi',val:'molisch_pos'},{label:'Tidak — tidak ada cincin ungu',desc:'Bukan karbohidrat',val:'molisch_neg'}]},
];

const SCORING_RULES = [
  {group:'Aldehid',formula:'R-CHO',desc:'Senyawa dengan gugus -CHO. Agen pereduksi kuat yang bereaksi positif dengan pereaksi oksidasi seperti Tollens dan Fehling. Berbeda dari keton, aldehid dapat dioksidasi lebih lanjut menjadi asam karboksilat.',score:(a)=>{let s=0;if(a.q3==='tollens_pos')s+=35;if(a.q4==='dnph_pos')s+=25;if(a.q5==='bromin_pos')s+=15;if(a.q3==='tollens_neg')s-=40;return s},tags:['🧪 Tollens +','🟠 DNPH +','🟤 Bromin +']},
  {group:'Keton',formula:'R-CO-R\'',desc:'Senyawa dengan gugus karbonil flanked oleh dua rantai karbon. Tidak dapat dioksidasi oleh Tollens, sehingga negatif Tollens menjadi ciri khas. Bereaksi positif dengan 2,4-DNPH seperti aldehid.',score:(a)=>{let s=0;if(a.q4==='dnph_pos')s+=35;if(a.q3==='tollens_neg')s+=25;if(a.q7==='iodoform_pos')s+=15;if(a.q3==='tollens_pos')s-=40;return s},tags:['🟠 DNPH +','🧪 Tollens −','🟡 Iodoform + (metil keton)']},
  {group:'Alkohol',formula:'R-OH',desc:'Senyawa dengan gugus hidroksil alifatik. Bersifat netral, larut dalam air (rantai pendek), tidak bereaksi dengan DNPH atau Tollens. Alkohol sekunder dan metil keton bereaksi positif iodoform.',score:(a)=>{let s=0;if(a.q1==='larut')s+=20;if(a.q3==='tollens_neg')s+=15;if(a.q4==='dnph_neg')s+=15;if(a.q5==='bromin_neg')s+=10;if(a.q8==='fecl3_neg')s+=10;if(a.q7==='iodoform_pos')s+=10;if(a.q3==='tollens_pos')s-=20;return s},tags:['💧 Larut air','🧪 Tollens −','🟡 Iodoform + (etanol/sekunder)']},
  {group:'Fenol',formula:'Ar-OH',desc:'Alkohol aromatik. Bersifat sedikit asam karena resonansi cincin aromatik. Ciri khas: warna violet/ungu dengan FeCl₃. Juga bereaksi dengan bromin menghasilkan endapan putih (substitusi elektrofilik).',score:(a)=>{let s=0;if(a.q8==='fecl3_pos')s+=50;if(a.q5==='bromin_pos')s+=15;if(a.q2==='netral_asam')s+=10;if(a.q8==='fecl3_neg')s-=40;return s},tags:['🔵 FeCl₃ + (violet)','🟤 Bromin +','⚗️ Sedikit asam']},
  {group:'Asam Karboksilat',formula:'R-COOH',desc:'Senyawa dengan gugus -COOH. Bersifat asam, membirukan kertas lakmus merah. Bereaksi dengan Na₂CO₃ menghasilkan gelembung CO₂. Asam format unik karena bereaksi positif dengan Tollens.',score:(a)=>{let s=0;if(a.q2==='netral_asam')s+=15;if(a.q3==='tollens_neg')s+=15;if(a.q4==='dnph_neg')s+=15;if(a.q1==='larut')s+=10;if(a.q3==='tollens_pos')s+=10;return s},tags:['🔴 Lakmus merah → biru','🧪 Tollens − (umumnya)','⚗️ Bereaksi Na₂CO₃']},
  {group:'Ester',formula:'R-COO-R\'',desc:'Produk reaksi asam dengan alkohol. Umumnya berbau harum. Bersifat netral, tidak bereaksi dengan sebagian besar pereaksi umum kecuali hidrolisis asam/basa (saponifikasi).',score:(a)=>{let s=0;if(a.q3==='tollens_neg')s+=15;if(a.q4==='dnph_neg')s+=15;if(a.q5==='bromin_neg')s+=10;if(a.q8==='fecl3_neg')s+=10;if(a.q9==='biuret_neg')s+=10;if(a.q10==='molisch_neg')s+=10;return s},tags:['🌸 Bau harum','🧪 Umumnya negatif semua uji','⚗️ Hidrolisis + asam/basa']},
  {group:'Alkena',formula:'R-CH=CH-R\'',desc:'Hidrokarbon tidak jenuh dengan satu ikatan rangkap C=C. Ikatan pi yang reaktif menyebabkan positif pada uji Baeyer (oksidasi KMnO₄) dan reaksi adisi dengan bromin.',score:(a)=>{let s=0;if(a.q6==='baeyer_pos')s+=40;if(a.q5==='bromin_pos')s+=30;if(a.q3==='tollens_neg')s+=10;if(a.q4==='dnph_neg')s+=10;if(a.q6==='baeyer_neg')s-=40;return s},tags:['🟠 Baeyer + (KMnO₄)','🟤 Bromin +','⚗️ Adisi']},
  {group:'Alkuna',formula:'R-C≡C-R\'',desc:'Hidrokarbon tidak jenuh dengan satu ikatan rangkap tiga. Reaktif seperti alkena. Alkuna terminal (R-C≡CH) bereaksi dengan AgNO₃ menghasilkan endapan perak.',score:(a)=>{let s=0;if(a.q6==='baeyer_pos')s+=35;if(a.q5==='bromin_pos')s+=25;if(a.q3==='tollens_neg')s+=10;if(a.q6==='baeyer_neg')s-=35;return s},tags:['🟠 Baeyer +','🟤 Bromin +','🧪 AgNO₃ + (terminal)']},
  {group:'Karbohidrat',formula:'Cₙ(H₂O)ₙ',desc:'Biomolekul dengan gugus aldehida/keton dan banyak hidroksil. Bereaksi khas dengan uji Molisch. Monosakarida pereduksi bereaksi positif Tollens dan Fehling/Benedict.',score:(a)=>{let s=0;if(a.q10==='molisch_pos')s+=50;if(a.q3==='tollens_pos')s+=15;if(a.q1==='larut')s+=10;if(a.q10==='molisch_neg')s-=50;return s},tags:['🟣 Molisch +','🧪 Tollens + (pereduksi)','💧 Larut air']},
  {group:'Protein',formula:'Polipeptida',desc:'Biopolimer asam amino yang dihubungkan ikatan peptida (-CO-NH-). Bereaksi ungu dengan uji Biuret. Mengandung asam amino aromatik yang bereaksi kuning dengan HNO₃ (xantoproteat).',score:(a)=>{let s=0;if(a.q9==='biuret_pos')s+=60;if(a.q1==='larut')s+=10;if(a.q3==='tollens_neg')s+=10;if(a.q9==='biuret_neg')s-=40;return s},tags:['🟢 Biuret + (ungu)','🧬 Xantoproteat +','🔬 Ninhydrin +']},
];

// ===== SIMULASI DATA =====
const SIM_SAMPLES = ['Formaldehid','Etanol','Aseton','Benzena','Fenol','Glukosa','Asetaldehid','Kasein','Etilena'];
const SIM_TESTS = ['Tollens','Baeyer','Bromin','Iodoform','DNPH','FeCl₃','Biuret','Molisch'];
const SIM_RESULTS = {
  'Formaldehid':{'Tollens':{r:'pos',obs:'Terbentuk lapisan cermin perak pada dinding tabung',conc:'Sampel mengandung gugus aldehid (-CHO) yang mereduksi ion Ag⁺'},'Bromin':{r:'pos',obs:'Warna merah-coklat bromin menghilang',conc:'Aldehid teroksidasi oleh bromin'},'DNPH':{r:'pos',obs:'Terbentuk endapan kuning-oranye',conc:'Sampel mengandung gugus karbonil (C=O)'},'Baeyer':{r:'neg',obs:'Larutan ungu KMnO₄ tidak berubah',conc:'Tidak ada ikatan rangkap C=C'},'Iodoform':{r:'neg',obs:'Tidak ada endapan kuning',conc:'Bukan metil keton atau etanol'},'FeCl₃':{r:'neg',obs:'Tidak ada perubahan warna khas',conc:'Bukan fenol'},'Biuret':{r:'neg',obs:'Tidak ada warna ungu',conc:'Bukan protein'},'Molisch':{r:'neg',obs:'Tidak ada cincin ungu',conc:'Bukan karbohidrat'}},
  'Etanol':{'Iodoform':{r:'pos',obs:'Terbentuk endapan kuning CHI₃ dengan bau khas',conc:'Etanol teroksidasi menjadi asetaldehid lalu bereaksi iodoform'},'Tollens':{r:'neg',obs:'Tidak ada cermin perak',conc:'Alkohol primer tidak langsung mereduksi Tollens'},'Bromin':{r:'neg',obs:'Warna bromin tetap',conc:'Tidak ada ikatan rangkap atau gugus reaktif'},'Baeyer':{r:'neg',obs:'KMnO₄ tetap ungu',conc:'Tidak ada ikatan C=C'},'DNPH':{r:'neg',obs:'Tidak ada endapan',conc:'Alkohol tidak memiliki gugus karbonil C=O bebas'},'FeCl₃':{r:'neg',obs:'Tidak ada perubahan',conc:'Bukan fenol'},'Biuret':{r:'neg',obs:'Tidak ada warna ungu',conc:'Bukan protein'},'Molisch':{r:'neg',obs:'Tidak ada cincin ungu',conc:'Bukan karbohidrat'}},
  'Aseton':{'DNPH':{r:'pos',obs:'Terbentuk endapan oranye-kuning',conc:'Keton memiliki gugus karbonil yang reaktif dengan 2,4-DNPH'},'Iodoform':{r:'pos',obs:'Endapan kuning CHI₃ terbentuk',conc:'Aseton adalah metil keton, bereaksi positif iodoform'},'Tollens':{r:'neg',obs:'Tidak ada cermin perak',conc:'Keton tidak dapat dioksidasi oleh Tollens'},'Bromin':{r:'neg',obs:'Warna tetap',conc:'Keton tidak mudah bereaksi dengan Br₂/CCl₄'},'Baeyer':{r:'neg',obs:'KMnO₄ tetap ungu',conc:'Tidak ada ikatan C=C'},'FeCl₃':{r:'neg',obs:'Tidak ada perubahan',conc:'Bukan fenol'},'Biuret':{r:'neg',obs:'Tidak ada perubahan',conc:'Bukan protein'},'Molisch':{r:'neg',obs:'Tidak ada perubahan',conc:'Bukan karbohidrat'}},
  'Benzena':{'Bromin':{r:'neg',obs:'Warna merah-coklat tetap (tanpa katalis)',conc:'Benzena stabil karena resonansi aromatik, tidak terjadi adisi spontan'},'Baeyer':{r:'neg',obs:'KMnO₄ tetap ungu',conc:'Cincin aromatik tidak dioksidasi seperti alkena'},'Tollens':{r:'neg',obs:'Tidak ada cermin',conc:'Bukan aldehid'},'DNPH':{r:'neg',obs:'Tidak ada endapan',conc:'Bukan aldehid/keton'},'Iodoform':{r:'neg',obs:'Tidak ada endapan kuning',conc:'Bukan metil keton'},'FeCl₃':{r:'neg',obs:'Tidak ada warna ungu',conc:'Bukan fenol (tidak ada -OH pada cincin)'},'Biuret':{r:'neg',obs:'Tidak ada perubahan',conc:'Bukan protein'},'Molisch':{r:'neg',obs:'Tidak ada perubahan',conc:'Bukan karbohidrat'}},
  'Fenol':{'FeCl₃':{r:'pos',obs:'Larutan berubah menjadi ungu/violet pekat',conc:'Fenol membentuk kompleks besi-fenolat yang berwarna violet'},'Bromin':{r:'pos',obs:'Larutan bromin terdekolorisasi, endapan putih terbentuk (2,4,6-tribromofenol)',conc:'Cincin aromatik fenol disubtitusi oleh bromin pada posisi orto dan para'},'Tollens':{r:'neg',obs:'Tidak ada cermin perak',conc:'Bukan aldehid'},'Baeyer':{r:'neg',obs:'KMnO₄ tetap ungu',conc:'Tidak ada ikatan rangkap alifatik'},'DNPH':{r:'neg',obs:'Tidak ada endapan',conc:'Bukan aldehid/keton'},'Iodoform':{r:'neg',obs:'Tidak ada endapan kuning',conc:'Bukan etanol atau metil keton'},'Biuret':{r:'neg',obs:'Tidak ada perubahan',conc:'Bukan protein'},'Molisch':{r:'neg',obs:'Tidak ada perubahan',conc:'Bukan karbohidrat'}},
  'Glukosa':{'Tollens':{r:'pos',obs:'Cermin perak terbentuk di dinding tabung',conc:'Glukosa adalah aldosa, memiliki gugus aldehid yang mereduksi Ag⁺'},'Molisch':{r:'pos',obs:'Cincin ungu terbentuk di antarmuka dua larutan',conc:'Glukosa adalah karbohidrat, terdehidrasi membentuk furfural dengan H₂SO₄'},'Bromin':{r:'neg',obs:'Warna tetap',conc:'Tidak ada ikatan rangkap C=C reaktif'},'Baeyer':{r:'neg',obs:'KMnO₄ tidak berubah secara nyata',conc:'Tidak ada alkena'},'DNPH':{r:'neg',obs:'Reaksi lemah/negatif dalam air',conc:'Gugus aldehid pada gula tidak selalu reaktif terhadap DNPH'},'FeCl₃':{r:'neg',obs:'Tidak ada warna ungu',conc:'Bukan fenol'},'Iodoform':{r:'neg',obs:'Tidak ada endapan kuning',conc:'Bukan metil keton'},'Biuret':{r:'neg',obs:'Tidak ada warna ungu',conc:'Bukan protein'}},
  'Asetaldehid':{'Tollens':{r:'pos',obs:'Cermin perak mengkilap terbentuk',conc:'Aldehid teroksidasi menjadi asam asetat oleh ion Ag⁺'},'Iodoform':{r:'pos',obs:'Endapan kuning CHI₃ dengan bau khas',conc:'Asetaldehid (CH₃CHO) bereaksi iodoform karena gugus -CH₃ di sebelah C=O'},'DNPH':{r:'pos',obs:'Endapan oranye-kuning terbentuk',conc:'Gugus karbonil bereaksi dengan 2,4-DNPH'},'Bromin':{r:'pos',obs:'Dekolorisasi terjadi',conc:'Aldehid teroksidasi'},'Baeyer':{r:'neg',obs:'Tidak ada perubahan',conc:'Tidak ada ikatan rangkap C=C'},'FeCl₃':{r:'neg',obs:'Tidak ada perubahan',conc:'Bukan fenol'},'Biuret':{r:'neg',obs:'Tidak ada perubahan',conc:'Bukan protein'},'Molisch':{r:'neg',obs:'Tidak ada perubahan',conc:'Bukan karbohidrat'}},
  'Kasein':{'Biuret':{r:'pos',obs:'Larutan berubah menjadi ungu',conc:'Ikatan peptida (-CO-NH-) membentuk kompleks dengan Cu²⁺ dalam suasana basa'},'Tollens':{r:'neg',obs:'Tidak ada cermin perak',conc:'Protein bukan aldehid'},'Molisch':{r:'neg',obs:'Tidak ada cincin ungu',conc:'Protein bukan karbohidrat murni'},'Bromin':{r:'neg',obs:'Tidak ada dekolorisasi',conc:'Tidak ada ikatan rangkap reaktif'},'Baeyer':{r:'neg',obs:'KMnO₄ tetap ungu',conc:'Tidak ada alkena'},'DNPH':{r:'neg',obs:'Tidak ada endapan',conc:'Bukan aldehid/keton'},'FeCl₃':{r:'neg',obs:'Tidak ada warna ungu',conc:'Bukan fenol'},'Iodoform':{r:'neg',obs:'Tidak ada endapan kuning',conc:'Bukan metil keton'}},
  'Etilena':{'Baeyer':{r:'pos',obs:'Larutan ungu KMnO₄ berubah menjadi coklat (MnO₂)',conc:'Ikatan rangkap C=C teroksidasi oleh KMnO₄ membentuk diol'},'Bromin':{r:'pos',obs:'Warna merah-coklat bromin menghilang',conc:'Reaksi adisi bromin pada ikatan rangkap membentuk 1,2-dibromoetana'},'Tollens':{r:'neg',obs:'Tidak ada cermin perak',conc:'Bukan aldehid'},'DNPH':{r:'neg',obs:'Tidak ada endapan',conc:'Tidak ada gugus karbonil'},'Iodoform':{r:'neg',obs:'Tidak ada endapan kuning',conc:'Bukan metil keton'},'FeCl₃':{r:'neg',obs:'Tidak ada perubahan',conc:'Bukan fenol'},'Biuret':{r:'neg',obs:'Tidak ada perubahan',conc:'Bukan protein'},'Molisch':{r:'neg',obs:'Tidak ada perubahan',conc:'Bukan karbohidrat'}},
};

// ===== KUIS DATA =====
const QUIZ_QUESTIONS = [
  {q:'Suatu senyawa memberikan hasil positif pada uji Tollens tetapi negatif pada uji Iodoform. Golongan senyawa tersebut adalah…',scenario:'Sampel cair, berbau sedikit tajam, larut dalam air.',opts:['Alkohol','Aldehid (bukan asetaldehid)','Keton','Fenol'],ans:1,explanation:'Tollens positif menandakan adanya gugus aldehid (-CHO). Iodoform negatif menyingkirkan asetaldehid (CH₃CHO) dan mengarahkan ke aldehid lain seperti formaldehid atau benzaldehid.'},
  {q:'Senyawa X bereaksi positif dengan 2,4-DNPH dan negatif dengan uji Tollens. Senyawa X kemungkinan adalah…',scenario:'Sampel cair tidak berwarna dengan bau pelarut yang khas.',opts:['Etanol','Asam asetat','Aseton','Benzaldehid'],ans:2,explanation:'DNPH positif menandakan gugus karbonil (C=O). Tollens negatif menyingkirkan aldehid. Kombinasi ini khas untuk keton seperti aseton (CH₃COCH₃).'},
  {q:'Senyawa organik mengubah lakmus merah menjadi biru, bereaksi dengan Na₂CO₃ menghasilkan gelembung, dan negatif Tollens. Senyawa ini termasuk…',scenario:'Sampel berupa cairan encer, tercium bau asam.',opts:['Alkohol','Fenol','Asam karboksilat','Ester'],ans:2,explanation:'Bersifat asam (membirukan lakmus) dan bereaksi dengan Na₂CO₃ (pKa < 6) khas untuk asam karboksilat. Fenol hanya mengasamkan sedikit dan tidak menghasilkan gelembung dengan Na₂CO₃ standar.'},
  {q:'Uji dengan FeCl₃ menghasilkan warna ungu intens. Uji Tollens negatif. Senyawa ini adalah…',scenario:'Sampel berbentuk kristal putih yang larut membentuk larutan jernih.',opts:['Glukosa','Asetaldehid','Fenol','Asam asetat'],ans:2,explanation:'Warna ungu/violet dengan FeCl₃ adalah ciri khas fenol (kompleks besi-fenolat). Tollens negatif menyingkirkan aldehid.'},
  {q:'Suatu larutan memberikan cincin ungu pada uji Molisch dan cermin perak pada uji Tollens. Kemungkinan senyawa ini adalah…',scenario:'Larutan bening, rasa manis.',opts:['Sukrosa','Pati (amilum)','Glukosa','Fruktosa (dengan catatan)'],ans:2,explanation:'Molisch positif menandakan karbohidrat. Tollens positif menandakan gula pereduksi. Glukosa adalah aldosa dengan gugus aldehid bebas yang mereduksi Ag⁺. Sukrosa dan pati tidak mereduksi Tollens.'},
  {q:'KMnO₄ alkali (uji Baeyer) berubah coklat, dan bromin dalam CCl₄ terdekolorisasi. Senyawa ini kemungkinan…',scenario:'Senyawa gas tidak berwarna, tersimpan dalam silinder bertekanan.',opts:['Benzena','Etilena (alkena)','Etanol','Aseton'],ans:1,explanation:'Baeyer positif (KMnO₄ berubah) dan Bromin positif (dekolorisasi) keduanya menandakan adanya ikatan rangkap C=C. Benzena tidak bereaksi dengan kedua pereaksi ini tanpa katalis.'},
  {q:'Uji Biuret memberikan warna ungu, uji Molisch negatif. Senyawa ini termasuk…',scenario:'Larutan keruh putih saat dipanaskan.',opts:['Karbohidrat','Lemak','Protein','Asam amino bebas'],ans:2,explanation:'Biuret positif (ungu) khas untuk protein yang memiliki ikatan peptida (-CO-NH-). Molisch negatif menyingkirkan karbohidrat. Asam amino bebas tidak selalu memberikan Biuret positif karena tidak punya ikatan peptida.'},
  {q:'Senyawa X: Iodoform positif (endapan kuning), DNPH negatif, Tollens negatif. Senyawa X adalah…',scenario:'Cairan tidak berwarna, bau alkohol, larut sempurna dalam air.',opts:['Aseton','Etanol','2-Propanol','Asetaldehid'],ans:1,explanation:'Iodoform positif bisa dari alkohol metil sekunder (seperti etanol atau isopropanol). DNPH negatif menyingkirkan keton. Tollens negatif menyingkirkan aldehid. Etanol (CH₃CH₂OH) bereaksi iodoform positif.'},
  {q:'Larutan iodin (I₂/KI) berubah menjadi biru-hitam intensif saat ditambahkan ke sampel. Ini menandakan kehadiran…',scenario:'Serbuk putih, tidak berasa.',opts:['Glukosa','Fruktosa','Amilum (pati)','Selulosa'],ans:2,explanation:'Perubahan warna menjadi biru-hitam dengan iodin adalah uji khas untuk amilum/pati. Ini terjadi karena molekul I₂ terjebak dalam heliks amilosa. Glukosa, fruktosa, dan selulosa tidak memberikan reaksi ini.'},
  {q:'Senyawa X larut dalam air, mengubah lakmus merah sedikit, memberikan FeCl₃ warna ungu, dan bromin positif (endapan putih). Senyawa X adalah…',scenario:'Kristal berwarna putih dengan bau khas.',opts:['Etanol','Fenol','Asam asetat','Alkena'],ans:1,explanation:'FeCl₃ ungu khas fenol. Bromin menghasilkan endapan putih (tribromofenol) — ini substitusi aromatik khas fenol. Lakmus sedikit asam juga cocok karena fenol bersifat asam lemah.'},
];

// ===== MATERI DATA =====
const MATERI = [
  {icon:'🧪',title:'Uji Tollens',short:'Uji cermin perak untuk aldehid',content:`<h4>Prinsip</h4><p>Reagen Tollens ([Ag(NH₃)₂]⁺, ion diaminoargent) bereaksi dengan aldehid yang mereduksi ion Ag⁺ menjadi Ag logam yang mengendap sebagai cermin perak pada dinding tabung.</p><h4>Reaksi</h4><p class="formula">RCHO + 2[Ag(NH₃)₂]⁺ + 2OH⁻ → RCOO⁻ + 2Ag↓ + 4NH₃ + H₂O</p><h4>Hasil Positif</h4><ul><li>Semua aldehid (formaldehid, asetaldehid, benzaldehid, dll)</li><li>Asam format (HCOOH) — memiliki karakter aldehid</li><li>Glukosa dan gula pereduksi lain</li></ul><h4>Hasil Negatif</h4><ul><li>Keton — tidak dapat dioksidasi lebih lanjut</li><li>Alkohol, asam karboksilat, ester, fenol</li></ul><h4>Catatan Praktikum</h4><p>Reagen harus segar (dibuat baru). Hangatkan pada water bath 50–60°C. Jangan dipanaskan terlalu tinggi karena dapat menghasilkan endapan palsu.</p>`},
  {icon:'🟠',title:'Uji Baeyer',short:'Deteksi ikatan rangkap C=C',content:`<h4>Prinsip</h4><p>Larutan KMnO₄ alkali encer (pereaksi Baeyer) mengoksidasi ikatan rangkap C=C. Ion MnO₄⁻ berwarna ungu tereduksi menjadi MnO₂ (coklat) atau Mn²⁺ (tak berwarna).</p><h4>Reaksi</h4><p class="formula">3 R-CH=CH-R' + 2 KMnO₄ + 4 H₂O → 3 R-CH(OH)-CH(OH)-R' + 2 MnO₂↓ + 2 KOH</p><h4>Hasil Positif</h4><ul><li>Semua alkena (etilena, propena, sikloheksena, dll)</li><li>Semua alkuna (asetilena, propuna, dll)</li><li>Beberapa aldehid (teroksidasi)</li></ul><h4>Hasil Negatif</h4><ul><li>Alkana — tidak ada ikatan rangkap</li><li>Benzena dan aromatik — ikatan resonansi stabil</li><li>Alkohol, keton, asam karboksilat</li></ul>`},
  {icon:'🟤',title:'Uji Bromin',short:'Adisi/substitusi dengan Br₂',content:`<h4>Prinsip</h4><p>Br₂ dalam CCl₄ (larutan merah-coklat) beradisi ke ikatan rangkap (alkena/alkuna) atau tersubstitusi elektrofilik pada cincin yang teraktifasi (fenol), menyebabkan dekolorisasi.</p><h4>Reaksi (Adisi)</h4><p class="formula">R-CH=CH-R' + Br₂ → R-CHBr-CHBr-R'</p><h4>Reaksi (Fenol)</h4><p class="formula">C₆H₅OH + 3Br₂ → C₆H₂Br₃OH↓ + 3HBr</p><h4>Hasil Positif</h4><ul><li>Alkena dan alkuna (adisi, tak berwarna)</li><li>Fenol (substitusi, endapan putih terbentuk)</li><li>Aldehid (teroksidasi)</li></ul><h4>Hasil Negatif</h4><ul><li>Alkana, benzena (stabil)</li><li>Alkohol, keton, ester</li></ul>`},
  {icon:'🟡',title:'Uji Iodoform',short:'Metil keton dan etanol',content:`<h4>Prinsip</h4><p>I₂ dalam NaOH mengiodinasi gugus metil di sebelah karbonil (atau etanol yang teroksidasi menjadi asetaldehid), menghasilkan CHI₃ (iodoform) — endapan kuning berbau khas.</p><h4>Reaksi</h4><p class="formula">CH₃COR + 3I₂ + 3NaOH → CHI₃↓ + RCOONa + 3NaI + 3H₂O</p><h4>Hasil Positif</h4><ul><li>Aseton (CH₃COCH₃) dan semua metil keton</li><li>Etanol (CH₃CH₂OH)</li><li>Asetaldehid (CH₃CHO)</li><li>Alkohol sekunder dengan gugus metil (isopropanol)</li></ul><h4>Hasil Negatif</h4><ul><li>Aldehid lain (formaldehid, benzaldehid)</li><li>Keton non-metil (sikloheksanon, benzofenon)</li></ul>`},
  {icon:'🔵',title:'Uji FeCl₃',short:'Identifikasi fenol',content:`<h4>Prinsip</h4><p>Ion Fe³⁺ membentuk kompleks berwarna dengan fenol (ikatan koordinasi melalui oksigen). Warna ungu/violet yang dihasilkan sangat khas.</p><h4>Reaksi</h4><p class="formula">6 ArOH + FeCl₃ → [Fe(OAr)₆]³⁻ + 3H⁺ + 3Cl⁻ (ungu-violet)</p><h4>Hasil Positif</h4><ul><li>Fenol — ungu/violet intens</li><li>Kresol — ungu</li><li>Asam salisilat — ungu-merah</li><li>Enol dari beberapa keton — warna bervariasi</li></ul><h4>Interpretasi Warna</h4><ul><li>Ungu/violet — fenol atau turunannya</li><li>Merah/jingga — asam benzoat atau salisilat</li><li>Hijau — beberapa enol keton</li></ul>`},
  {icon:'🟢',title:'Uji Biuret',short:'Deteksi protein (ikatan peptida)',content:`<h4>Prinsip</h4><p>Dalam suasana basa, Cu²⁺ membentuk kompleks berwarna ungu dengan ikatan peptida (-CO-NH-). Intensitas warna sebanding dengan jumlah ikatan peptida.</p><h4>Reaksi</h4><p class="formula">Ikatan peptida + Cu²⁺ + 2OH⁻ → Kompleks ungu [Cu-N-C=O]</p><h4>Hasil Positif</h4><ul><li>Protein — ungu</li><li>Dipeptida dan polipeptida</li><li>Urea juga memberikan hasil positif (mengandung struktur mirip)</li></ul><h4>Hasil Negatif</h4><ul><li>Asam amino bebas (tidak punya ikatan peptida)</li><li>Karbohidrat, lipid</li></ul>`},
];

// ===== STATE =====
let idAnswers={},idCurrentQ=0;
let simSample=null,simTests=[];
let quizCurrent=0,quizScore=0,quizAnswered=false,quizDone=false;
let materiOpen=null;
let dbFilterGroup='Semua';

// ===== NAVIGATION =====
function showPage(id){
  document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
  document.getElementById('page-'+id).classList.add('active');
  document.querySelectorAll('.nav-link').forEach(b=>b.classList.remove('active'));
  const map={home:0,identifikasi:1,database:2,simulasi:3,kuis:4,materi:5,tentang:6};
  const idx=map[id];
  if(idx>0){document.querySelectorAll('.nav-link')[idx-1].classList.add('active');}
  if(id==='identifikasi')initIdentifikasi();
  if(id==='database')initDB();
  if(id==='simulasi')initSim();
  if(id==='kuis')initKuis();
  if(id==='materi')initMateri();
}

// ===== IDENTIFIKASI =====
function initIdentifikasi(){
  idAnswers={};idCurrentQ=0;
  renderIDQuestion();
}
function renderIDQuestion(){
  const area=document.getElementById('id-quiz-area');
  const q=ID_QUESTIONS[idCurrentQ];
  const dots=ID_QUESTIONS.map((_,i)=>`<div class="q-dot ${i<idCurrentQ?'done':''} ${i===idCurrentQ?'active':''}"></div>`).join('');
  const optsHtml=q.opts.map((o,i)=>`
    <button class="q-opt ${idAnswers[q.id]===o.val?'selected':''}" onclick="selectIDAnswer('${q.id}','${o.val}',this)">
      <div class="q-opt-label">${o.label}</div>
      <div class="q-opt-desc">${o.desc}</div>
    </button>`).join('');
  area.innerHTML=`
    <div class="question-track">${dots}</div>
    <div class="question-box">
      <div class="q-number">Pertanyaan ${idCurrentQ+1} dari ${ID_QUESTIONS.length}</div>
      <div class="q-text">${q.text}</div>
      <div class="q-context">🔬 ${q.context}</div>
      <div class="q-options">${optsHtml}</div>
      <div class="q-nav">
        ${idCurrentQ>0?`<button class="btn-ghost" onclick="idPrev()">← Kembali</button>`:''}
        <button class="btn-next" id="btn-id-next" onclick="idNext()" ${!idAnswers[q.id]?'disabled':''}>
          ${idCurrentQ<ID_QUESTIONS.length-1?'Lanjut →':'Lihat Hasil'}
        </button>
      </div>
    </div>`;
}
function selectIDAnswer(qid,val){
  idAnswers[qid]=val;
  document.querySelectorAll('.q-opt').forEach(b=>b.classList.remove('selected'));
  event.currentTarget.classList.add('selected');
  document.getElementById('btn-id-next').disabled=false;
}
function idNext(){
  if(idCurrentQ<ID_QUESTIONS.length-1){idCurrentQ++;renderIDQuestion();}
  else showIDResult();
}
function idPrev(){idCurrentQ--;renderIDQuestion();}
function showIDResult(){
  const scores=SCORING_RULES.map(r=>({...r,s:Math.max(0,r.score(idAnswers))}));
  scores.sort((a,b)=>b.s-a.s);
  const max=scores[0].s||1;
  const area=document.getElementById('id-quiz-area');
  const top=scores.filter(s=>s.s>0).slice(0,5);
  const resultsHtml=top.map((s,i)=>`
    <div class="compound-result ${i===0?'high':i<2?'mid':''}">
      <div style="display:flex;justify-content:space-between;align-items:flex-start">
        <div>
          <div class="compound-name">${s.group}</div>
          <div class="compound-formula">${s.formula}</div>
        </div>
        <span class="tag ${i===0?'tag-teal':i<2?'tag-amber':'tag-blue'}">${Math.round(s.s)}% cocok</span>
      </div>
      <div class="match-bar"><div class="match-fill ${i>0?'mid':''}" style="width:${(s.s/max)*100}%"></div></div>
      <div class="compound-explanation">${s.desc}</div>
      <div style="margin-top:0.75rem;display:flex;flex-wrap:wrap;gap:0.35rem">${s.tags.map(t=>`<span class="tag tag-teal" style="font-size:0.6rem">${t}</span>`).join('')}</div>
    </div>`).join('');
  area.innerHTML=`
    <div class="hasil-header">
      <div style="font-family:var(--font-mono);font-size:0.8rem;color:var(--muted);margin-bottom:0.5rem">ANALISIS SELESAI</div>
      <div class="score-big">${top[0]?.group||'Tidak diketahui'}</div>
      <div style="color:var(--muted);font-size:0.9rem;margin-top:0.5rem">Kemungkinan golongan terkuat</div>
    </div>
    <div style="margin-bottom:1rem"><strong style="font-size:0.9rem">Kemungkinan golongan (berdasarkan skor cocok):</strong></div>
    ${resultsHtml}
    <button class="btn-reset" onclick="initIdentifikasi()" style="margin-top:1.5rem">⟳ Identifikasi Ulang</button>`;
}

// ===== DATABASE =====
function initDB(){
  const filters=['Semua',...GOLONGAN_TAGS];
  document.getElementById('db-filters').innerHTML=filters.map(g=>`<button class="filter-btn ${g===dbFilterGroup?'active':''}" onclick="setDBFilter('${g}')">${g}</button>`).join('');
  renderDB();
}
function setDBFilter(g){dbFilterGroup=g;initDB();}
function filterDB(){renderDB();}
function renderDB(){
  const search=document.getElementById('db-search')?.value.toLowerCase()||'';
  const tbody=document.getElementById('compound-tbody');
  const filtered=COMPOUNDS.filter(c=>{
    const matchGroup=dbFilterGroup==='Semua'||c.group===dbFilterGroup;
    const matchSearch=!search||(c.name.toLowerCase().includes(search)||c.formula.toLowerCase().includes(search)||c.group.toLowerCase().includes(search));
    return matchGroup&&matchSearch;
  });
  tbody.innerHTML=filtered.map(c=>`
    <tr onclick="openCompoundModal('${c.name}')">
      <td><strong style="font-family:var(--font-head);font-size:0.9rem">${c.name}</strong></td>
      <td class="mono">${c.formula}</td>
      <td><span class="tag ${getGroupTag(c.group)}">${c.group}</span></td>
      <td style="font-size:0.8rem;color:var(--teal)">${c.positive.slice(0,2).join(', ')}</td>
      <td style="font-size:0.8rem;color:var(--coral)">${c.negative.slice(0,2).join(', ')}</td>
    </tr>`).join('');
  document.querySelectorAll('.filter-btn').forEach(b=>{b.classList.toggle('active',b.textContent===dbFilterGroup);});
}
function getGroupTag(g){const m={Alkohol:'tag-teal',Aldehid:'tag-amber',Keton:'tag-coral',Fenol:'tag-purple',Asam_Karboksilat:'tag-blue','Asam Karboksilat':'tag-blue',Ester:'tag-green',Alkena:'tag-teal',Alkuna:'tag-amber',Karbohidrat:'tag-purple',Protein:'tag-coral',Aromatik:'tag-blue','Asam Amino':'tag-green'};return m[g]||'tag-blue';}
function openCompoundModal(name){
  const c=COMPOUNDS.find(x=>x.name===name);
  if(!c)return;
  const tests=Object.entries(c.tests).map(([k,v])=>`
    <div class="test-item ${v.startsWith('pos')?'positive':'negative'}">
      <div class="test-name">${k.toUpperCase()}</div>
      <div class="test-result">${v.startsWith('pos')?'✔ Positif':'✖ '+v}</div>
    </div>`).join('');
  document.getElementById('modal-content').innerHTML=`
    <button class="modal-close" onclick="closeModal()">×</button>
    <div style="display:flex;gap:1rem;align-items:flex-start;margin-bottom:1rem;flex-wrap:wrap">
      <div>
        <h3>${c.name}</h3>
        <span class="mono" style="font-size:1rem">${c.formula}</span>
        &nbsp;<span class="tag ${getGroupTag(c.group)}">${c.group}</span>
      </div>
    </div>
    <p style="color:var(--muted);font-size:0.85rem;margin-bottom:1rem">${c.desc}</p>
    <div style="margin-bottom:0.75rem;font-family:var(--font-mono);font-size:0.7rem;color:var(--muted);text-transform:uppercase;letter-spacing:0.08em">Hasil Uji Kualitatif</div>
    <div class="test-grid">${tests}</div>`;
  document.getElementById('modal-overlay').classList.add('open');
}
function closeModal(e){if(!e||e.target===document.getElementById('modal-overlay'))document.getElementById('modal-overlay').classList.remove('open');}

// ===== SIMULASI =====
function initSim(){
  document.getElementById('sim-samples').innerHTML=SIM_SAMPLES.map(s=>`<button class="sim-chip" onclick="selectSim('sample','${s}',this)">${s}</button>`).join('');
  document.getElementById('sim-tests').innerHTML=SIM_TESTS.map(t=>`<button class="sim-chip test-chip" onclick="selectSim('test','${t}',this)">${t}</button>`).join('');
  simSample=null;simTests=[];
  document.getElementById('sim-result').innerHTML='<div style="font-size:2rem">⚗️</div><div>Pilih sampel dan pereaksi untuk memulai</div>';
  document.getElementById('sim-result').classList.add('empty');
  document.getElementById('btn-sim').disabled=true;
}
function selectSim(type,val,btn){
  if(type==='sample'){
    document.querySelectorAll('#sim-samples .sim-chip').forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    simSample=val;
  } else {
    btn.classList.toggle('active');
    if(btn.classList.contains('active')){if(!simTests.includes(val))simTests.push(val);}
    else simTests=simTests.filter(t=>t!==val);
  }
  document.getElementById('btn-sim').disabled=!simSample||simTests.length===0;
}
function runSim(){
  const data=SIM_RESULTS[simSample];
  if(!data)return;
  const compound=COMPOUNDS.find(c=>c.name===simSample);
  const resultsHtml=simTests.map(t=>{
    const r=data[t];
    if(!r)return `<div class="test-result-item negative"><div class="r-test">${t.toUpperCase()}</div><div class="r-status">Data tidak tersedia</div></div>`;
    return `<div class="test-result-item ${r.r}">
      <div class="r-test">${t.toUpperCase()}</div>
      <div class="r-status">${r.r==='pos'?'✔ Positif':'✖ Negatif'}</div>
      <div class="r-desc">${r.obs}</div>
    </div>`;
  }).join('');
  const conclusions=[...new Set(simTests.filter(t=>data[t]).map(t=>data[t].conc))];
  const panel=document.getElementById('sim-result');
  panel.classList.remove('empty');
  panel.innerHTML=`
    <div class="result-title">HASIL SIMULASI — ${simSample.toUpperCase()}</div>
    ${compound?`<p style="font-size:0.8rem;color:var(--muted);margin-bottom:1rem">${compound.desc}</p>`:''}
    ${resultsHtml}
    <div class="conclusion-box">
      <div class="c-label">KESIMPULAN</div>
      ${conclusions.map(c=>`<div class="c-text">• ${c}</div>`).join('')}
    </div>`;
}

// ===== KUIS =====
function initKuis(){
  quizCurrent=0;quizScore=0;quizAnswered=false;quizDone=false;
  renderKuis();
}
function renderKuis(){
  const area=document.getElementById('quiz-area');
  if(quizDone){
    const pct=Math.round((quizScore/QUIZ_QUESTIONS.length)*100);
    const grade=pct>=90?'A':pct>=80?'B':pct>=70?'C':pct>=60?'D':'E';
    const msg=pct>=80?'Luar biasa! Pemahaman sangat baik.':pct>=60?'Bagus! Terus berlatih.':'Perlu banyak berlatih lagi.';
    area.innerHTML=`<div class="quiz-final">
      <div class="quiz-final-score" style="color:${pct>=80?'var(--teal)':pct>=60?'var(--amber)':'var(--coral)'}">${pct}</div>
      <div class="quiz-grade" style="color:var(--muted)">Nilai ${grade} · ${quizScore}/${QUIZ_QUESTIONS.length} benar</div>
      <p style="color:var(--muted);margin-bottom:2rem">${msg}</p>
      <button class="btn-primary" onclick="initKuis()">Ulangi Kuis</button>
    </div>`;
    return;
  }
  const q=QUIZ_QUESTIONS[quizCurrent];
  const progress=(quizCurrent/QUIZ_QUESTIONS.length)*100;
  const optsHtml=q.opts.map((o,i)=>`
    <button class="quiz-opt" id="qopt-${i}" onclick="answerKuis(${i})" ${quizAnswered?'disabled':''}>
      <span class="opt-letter">${'ABCD'[i]}</span>
      ${o}
    </button>`).join('');
  area.innerHTML=`
    <div class="quiz-progress">
      <span style="font-family:var(--font-mono);font-size:0.75rem;color:var(--muted);">${quizCurrent+1}/${QUIZ_QUESTIONS.length}</span>
      <div class="quiz-bar"><div class="quiz-bar-fill" style="width:${progress}%"></div></div>
      <span class="quiz-score-live">✓ ${quizScore}</span>
    </div>
    <div class="quiz-q-box">
      <div class="quiz-q-num">Soal ${quizCurrent+1}</div>
      <div class="quiz-q-text">${q.q}</div>
      <div class="quiz-scenario">${q.scenario}</div>
      <div class="quiz-opts">${optsHtml}</div>
      <div id="quiz-feedback"></div>
    </div>`;
}
function answerKuis(idx){
  if(quizAnswered)return;
  quizAnswered=true;
  const q=QUIZ_QUESTIONS[quizCurrent];
  const correct=idx===q.ans;
  if(correct)quizScore++;
  document.querySelectorAll('.quiz-opt').forEach((b,i)=>{
    b.disabled=true;
    if(i===q.ans)b.classList.add('correct');
    else if(i===idx&&!correct)b.classList.add('wrong');
  });
  document.getElementById('quiz-feedback').innerHTML=`
    <div class="quiz-feedback">${correct?'<strong style="color:var(--teal)">✓ Benar!</strong> ':'<strong style="color:var(--coral)">✖ Salah.</strong> '} ${q.explanation}</div>
    <button class="btn-quiz-next" onclick="nextKuis()">${quizCurrent<QUIZ_QUESTIONS.length-1?'Soal Berikutnya →':'Lihat Hasil'}</button>`;
}
function nextKuis(){quizAnswered=false;quizCurrent++;if(quizCurrent>=QUIZ_QUESTIONS.length)quizDone=true;renderKuis();}

// ===== MATERI =====
function initMateri(){
  const el=document.getElementById('materi-content');
  el.innerHTML=`<div class="materi-grid">${MATERI.map((m,i)=>`
    <div class="materi-card" onclick="toggleMateri(${i})">
      <div class="materi-icon">${m.icon}</div>
      <h3>${m.title}</h3>
      <p>${m.short}</p>
    </div>`).join('')}</div>
  ${MATERI.map((m,i)=>`
    <div class="materi-detail" id="materi-detail-${i}">
      <button class="btn-back-materi" onclick="toggleMateri(${i})">← Tutup</button>
      <h3>${m.icon} ${m.title}</h3>
      ${m.content}
    </div>`).join('')}`;
  materiOpen=null;
}
function toggleMateri(i){
  if(materiOpen===i){
    document.getElementById(`materi-detail-${i}`).classList.remove('open');
    materiOpen=null;
  } else {
    if(materiOpen!==null)document.getElementById(`materi-detail-${materiOpen}`).classList.remove('open');
    document.getElementById(`materi-detail-${i}`).classList.add('open');
    materiOpen=i;
    setTimeout(()=>document.getElementById(`materi-detail-${i}`).scrollIntoView({behavior:'smooth',block:'start'}),100);
  }
}

// INIT
showPage('home');
</script>
</body>
</html>
