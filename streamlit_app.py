import streamlit as st
 
st.set_page_config(
    page_title="OrganIQ — Identifikasi Senyawa Organik",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)
 
# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Mono:wght@400;500&display=swap');
 
html, body, [class*="css"] { font-family: 'Syne', sans-serif; }
 
/* Sidebar */
[data-testid="stSidebar"] {
    background: #0d1117;
    border-right: 1px solid rgba(255,255,255,0.08);
}
[data-testid="stSidebar"] * { color: #e6edf3 !important; }
[data-testid="stSidebar"] .stRadio label {
    font-size: 0.9rem;
    padding: 6px 0;
}
 
/* Main */
[data-testid="stAppViewContainer"] { background: #0d1117; }
[data-testid="stHeader"] { background: #0d1117; }
 
h1, h2, h3 { font-family: 'Syne', sans-serif !important; }
p, li, td, th { color: #c9d1d9; }
 
/* Metric cards */
[data-testid="stMetric"] {
    background: #161b22;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px;
    padding: 1rem;
}
[data-testid="stMetricLabel"] { color: #7d8590 !important; font-size: 0.8rem !important; }
[data-testid="stMetricValue"] { color: #39d4a5 !important; font-family: 'DM Mono', monospace !important; }
 
/* Expander */
[data-testid="stExpander"] {
    background: #161b22;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 10px !important;
}
details summary { color: #e6edf3 !important; font-weight: 700; }
 
/* Buttons */
.stButton > button {
    background: #39d4a5;
    color: #0d1117;
    border: none;
    border-radius: 8px;
    font-weight: 700;
    font-family: 'Syne', sans-serif;
    padding: 0.5rem 1.5rem;
    transition: all 0.2s;
}
.stButton > button:hover { background: #52e8b8; border: none; }
.stButton > button[kind="secondary"] {
    background: transparent;
    color: #7d8590 !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
}
 
/* Selectbox, radio */
[data-testid="stSelectbox"] > div > div,
[data-testid="stRadio"] > div { background: #161b22; border-radius: 8px; }
 
/* Info/success/warning boxes */
[data-testid="stAlert"] { border-radius: 10px; }
 
/* Progress bar */
[data-testid="stProgressBar"] > div > div { background: #39d4a5; }
 
/* DataFrame */
[data-testid="stDataFrame"] { border-radius: 10px; overflow: hidden; }
 
/* Divider */
hr { border-color: rgba(255,255,255,0.08) !important; }
 
/* Tag pill */
.tag {
    display: inline-block;
    padding: 2px 10px;
    border-radius: 20px;
    font-size: 0.72rem;
    font-family: 'DM Mono', monospace;
    font-weight: 500;
    margin: 2px;
}
.tag-teal   { background: rgba(57,212,165,0.15); color: #39d4a5; }
.tag-amber  { background: rgba(240,160,58,0.15);  color: #f0a03a; }
.tag-coral  { background: rgba(240,120,120,0.15); color: #f07878; }
.tag-blue   { background: rgba(77,166,255,0.15);  color: #4da6ff; }
.tag-purple { background: rgba(167,139,250,0.15); color: #a78bfa; }
.tag-green  { background: rgba(86,211,100,0.15);  color: #56d364; }
 
/* Card */
.card {
    background: #161b22;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    margin-bottom: 0.75rem;
}
.card-high { border-color: #39d4a5; background: rgba(57,212,165,0.08); }
.card-mid  { border-color: #f0a03a; background: rgba(240,160,58,0.08);  }
</style>
""", unsafe_allow_html=True)
 
# ── Data ────────────────────────────────────────────────────────────────────
from data.compounds   import COMPOUNDS, GOLONGAN_TAGS
from data.questions   import ID_QUESTIONS, SCORING_RULES
from data.materi      import MATERI_LIST
 
# ── Sidebar navigation ──────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🧪 OrganIQ")
    st.markdown("<p style='color:#7d8590;font-size:0.8rem;margin-bottom:1.5rem'>Sistem Identifikasi Senyawa Organik</p>", unsafe_allow_html=True)
    st.divider()
    page = st.radio(
        "Navigasi",
        ["🏠 Beranda", "🔬 Identifikasi Senyawa", "🗃️ Database Senyawa", "📚 Materi Uji"],
        label_visibility="collapsed",
    )
    st.divider()
    st.markdown("<p style='color:#7d8590;font-size:0.72rem;font-family:DM Mono,monospace'>OrganIQ v1.0 · 2025<br>Kimia Organik Kualitatif</p>", unsafe_allow_html=True)
 
# ════════════════════════════════════════════════════════════════════════════
# PAGE: BERANDA
# ════════════════════════════════════════════════════════════════════════════
if page == "🏠 Beranda":
    st.markdown("""
    <div style='text-align:center; padding: 3rem 0 2rem'>
        <div style='font-family:DM Mono,monospace;font-size:0.75rem;color:#39d4a5;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:1rem'>
            Laboratorium Digital Kimia Organik
        </div>
        <h1 style='font-size:3rem;font-weight:800;letter-spacing:-0.03em;color:#e6edf3;line-height:1.1'>
            Identifikasi<br><span style='color:#39d4a5'>Senyawa Organik</span><br>secara Kualitatif
        </h1>
        <p style='color:#7d8590;font-size:1rem;max-width:540px;margin:1.5rem auto 0;line-height:1.8'>
            Platform edukasi interaktif untuk mengidentifikasi golongan senyawa organik
            berdasarkan uji laboratorium — Tollens, Baeyer, Bromin, Iodoform, dan lainnya.
        </p>
    </div>
    """, unsafe_allow_html=True)
 
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class='card'>
            <div style='font-size:2rem;margin-bottom:.75rem'>🔬</div>
            <h3 style='color:#e6edf3;font-size:1rem;margin-bottom:.5rem'>Identifikasi Senyawa</h3>
            <p style='color:#7d8590;font-size:.82rem;line-height:1.6'>Jawab 10 pertanyaan uji dan dapatkan kemungkinan golongan senyawa sampelmu secara otomatis.</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class='card'>
            <div style='font-size:2rem;margin-bottom:.75rem'>🗃️</div>
            <h3 style='color:#e6edf3;font-size:1rem;margin-bottom:.5rem'>Database Senyawa</h3>
            <p style='color:#7d8590;font-size:.82rem;line-height:1.6'>Cari dan telusuri 30+ senyawa organik dengan data uji kualitatif lengkap dan terstruktur.</p>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class='card'>
            <div style='font-size:2rem;margin-bottom:.75rem'>📚</div>
            <h3 style='color:#e6edf3;font-size:1rem;margin-bottom:.5rem'>Materi Uji</h3>
            <p style='color:#7d8590;font-size:.82rem;line-height:1.6'>Pelajari prinsip reaksi, interpretasi hasil, dan catatan praktikum setiap uji kualitatif.</p>
        </div>""", unsafe_allow_html=True)
 
    st.divider()
    st.markdown("<h3 style='color:#e6edf3;text-align:center;margin-bottom:1.5rem'>Referensi Cepat Uji Kualitatif</h3>", unsafe_allow_html=True)
 
    uji_data = [
        ("🧪", "Tollens",    "Cermin perak ✔",         "Aldehid, Asam Format, Gula pereduksi"),
        ("🟠", "Baeyer",     "KMnO₄ coklat ✔",         "Alkena, Alkuna"),
        ("🟤", "Bromin",     "Dekolorisasi Br₂ ✔",      "Alkena, Alkuna, Fenol, Aldehid"),
        ("🟡", "Iodoform",   "Endapan CHI₃ kuning ✔",   "Metil keton, Etanol, Asetaldehid"),
        ("🔵", "FeCl₃",      "Warna ungu/violet ✔",     "Fenol, Enol"),
        ("🟢", "Biuret",     "Warna ungu ✔",            "Protein (ikatan peptida)"),
        ("🟣", "Molisch",    "Cincin ungu ✔",           "Semua karbohidrat"),
        ("🟠", "2,4-DNPH",   "Endapan oranye ✔",        "Aldehid dan Keton"),
        ("🔴", "Lakmus",     "Biru → merah",            "Asam karboksilat, Fenol"),
    ]
    r1, r2, r3 = st.columns(3)
    cols = [r1, r2, r3]
    for i, (icon, name, result, target) in enumerate(uji_data):
        with cols[i % 3]:
            st.markdown(f"""<div class='card' style='padding:1rem'>
                <div style='font-size:1.4rem;margin-bottom:.5rem'>{icon}</div>
                <div style='font-family:DM Mono,monospace;font-size:.75rem;color:#7d8590;margin-bottom:.2rem'>UJI {name.upper()}</div>
                <div style='color:#39d4a5;font-size:.82rem;font-weight:700;margin-bottom:.3rem'>{result}</div>
                <div style='color:#7d8590;font-size:.78rem'>{target}</div>
            </div>""", unsafe_allow_html=True)
 
 
# ════════════════════════════════════════════════════════════════════════════
# PAGE: IDENTIFIKASI
# ════════════════════════════════════════════════════════════════════════════
elif page == "🔬 Identifikasi Senyawa":
    st.markdown("<h2 style='color:#e6edf3;margin-bottom:.25rem'>🔬 Identifikasi Senyawa</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#7d8590;margin-bottom:1.5rem'>Jawab pertanyaan berdasarkan hasil pengujian laboratoriummu. Sistem akan menganalisis kemungkinan golongan senyawa.</p>", unsafe_allow_html=True)
 
    # Init session state
    if "id_answers" not in st.session_state:
        st.session_state.id_answers = {}
    if "id_step" not in st.session_state:
        st.session_state.id_step = 0
    if "id_done" not in st.session_state:
        st.session_state.id_done = False
 
    # Reset button
    col_title, col_reset = st.columns([5, 1])
    with col_reset:
        if st.button("⟳ Reset", key="id_reset"):
            st.session_state.id_answers = {}
            st.session_state.id_step = 0
            st.session_state.id_done = False
            st.rerun()
 
    if not st.session_state.id_done:
        total = len(ID_QUESTIONS)
        step  = st.session_state.id_step
 
        # Progress
        st.progress(step / total)
        st.markdown(f"<p style='font-family:DM Mono,monospace;font-size:.75rem;color:#7d8590;margin-bottom:1rem'>Pertanyaan {step+1} dari {total}</p>", unsafe_allow_html=True)
 
        q = ID_QUESTIONS[step]
 
        with st.container():
            st.markdown(f"""<div class='card'>
                <div style='font-family:DM Mono,monospace;font-size:.7rem;color:#7d8590;margin-bottom:.5rem'>PERTANYAAN {step+1}</div>
                <h3 style='color:#e6edf3;font-size:1.15rem;margin-bottom:.4rem'>{q["text"]}</h3>
                <p style='font-size:.85rem;color:#f0a03a;font-style:italic;margin-bottom:0'>🔬 {q["context"]}</p>
            </div>""", unsafe_allow_html=True)
 
        # Previously answered value
        prev = st.session_state.id_answers.get(q["id"])
        opt_labels = [o["label"] for o in q["opts"]]
        prev_idx = next((i for i, o in enumerate(q["opts"]) if o["val"] == prev), 0)
 
        choice = st.radio(
            "Pilih jawaban:",
            options=opt_labels,
            index=prev_idx,
            key=f"radio_{step}",
        )
        chosen_val = q["opts"][opt_labels.index(choice)]["val"]
        chosen_desc = q["opts"][opt_labels.index(choice)]["desc"]
        st.caption(f"💡 {chosen_desc}")
 
        col_prev, col_spacer, col_next = st.columns([1, 4, 1])
        with col_prev:
            if step > 0:
                if st.button("← Kembali"):
                    st.session_state.id_answers[q["id"]] = chosen_val
                    st.session_state.id_step -= 1
                    st.rerun()
        with col_next:
            btn_label = "Lanjut →" if step < total - 1 else "Lihat Hasil ✔"
            if st.button(btn_label, key="id_next"):
                st.session_state.id_answers[q["id"]] = chosen_val
                if step < total - 1:
                    st.session_state.id_step += 1
                else:
                    st.session_state.id_done = True
                st.rerun()
 
    else:
        # ── Show results ────────────────────────────────────────────────
        answers = st.session_state.id_answers
 
        scores = []
        for rule in SCORING_RULES:
            raw = rule["score_fn"](answers)
            scores.append({**rule, "score": max(0, raw)})
        scores.sort(key=lambda x: x["score"], reverse=True)
        max_s = scores[0]["score"] or 1
        top = [s for s in scores if s["score"] > 0][:5]
 
        st.markdown(f"""
        <div style='text-align:center;padding:2rem 0 1.5rem'>
            <div style='font-family:DM Mono,monospace;font-size:.75rem;color:#7d8590;letter-spacing:.1em;margin-bottom:.5rem'>ANALISIS SELESAI</div>
            <div style='font-size:2.5rem;font-weight:800;color:#39d4a5;font-family:Syne,sans-serif'>{top[0]["group"] if top else "Tidak diketahui"}</div>
            <div style='color:#7d8590;font-size:.9rem;margin-top:.25rem'>Kemungkinan golongan terkuat</div>
        </div>
        """, unsafe_allow_html=True)
 
        st.markdown("**Kemungkinan golongan (berdasarkan skor kecocokan):**")
 
        for i, s in enumerate(top):
            pct = int((s["score"] / max_s) * 100)
            card_cls = "card-high" if i == 0 else ("card-mid" if i == 1 else "card")
            tag_col   = "#39d4a5" if i == 0 else ("#f0a03a" if i == 1 else "#4da6ff")
            tags_html = "".join(f"<span class='tag tag-teal' style='font-size:.6rem'>{t}</span>" for t in s.get("tags", []))
 
            st.markdown(f"""<div class='{card_cls}'>
                <div style='display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:.5rem'>
                    <div>
                        <div style='font-family:Syne,sans-serif;font-size:1.05rem;font-weight:700;color:#e6edf3'>{s["group"]}</div>
                        <div style='font-family:DM Mono,monospace;font-size:.8rem;color:#7d8590'>{s["formula"]}</div>
                    </div>
                    <span style='background:rgba(57,212,165,.15);color:{tag_col};font-family:DM Mono,monospace;font-size:.7rem;padding:3px 10px;border-radius:20px'>{pct}% cocok</span>
                </div>
                <p style='font-size:.85rem;color:#7d8590;line-height:1.6;margin-bottom:.75rem'>{s["desc"]}</p>
                {tags_html}
            </div>""", unsafe_allow_html=True)
            st.progress(pct / 100)
 
        st.divider()
        if st.button("⟳ Identifikasi Ulang"):
            st.session_state.id_answers = {}
            st.session_state.id_step = 0
            st.session_state.id_done = False
            st.rerun()
 
 
# ════════════════════════════════════════════════════════════════════════════
# PAGE: DATABASE
# ════════════════════════════════════════════════════════════════════════════
elif page == "🗃️ Database Senyawa":
    import pandas as pd
 
    st.markdown("<h2 style='color:#e6edf3;margin-bottom:.25rem'>🗃️ Database Senyawa Organik</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#7d8590;margin-bottom:1.5rem'>Klik ekspander senyawa untuk melihat detail uji kualitatif lengkap.</p>", unsafe_allow_html=True)
 
    # Stats row
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Senyawa",   len(COMPOUNDS))
    c2.metric("Golongan",        len(GOLONGAN_TAGS))
    c3.metric("Uji Kualitatif",  10)
    c4.metric("Data Uji",        f"{len(COMPOUNDS) * 10}+")
 
    st.divider()
 
    # Filter & search
    col_s, col_f = st.columns([3, 2])
    with col_s:
        search = st.text_input("🔍 Cari senyawa, rumus, atau golongan", placeholder="contoh: etanol, aldehid, C₂H₅OH…")
    with col_f:
        group_filter = st.selectbox("Filter Golongan", ["Semua"] + GOLONGAN_TAGS)
 
    # Filter logic
    filtered = COMPOUNDS
    if group_filter != "Semua":
        filtered = [c for c in filtered if c["group"] == group_filter]
    if search:
        s = search.lower()
        filtered = [c for c in filtered if s in c["name"].lower() or s in c["formula"].lower() or s in c["group"].lower()]
 
    st.markdown(f"<p style='font-family:DM Mono,monospace;font-size:.75rem;color:#7d8590;margin-bottom:1rem'>Menampilkan {len(filtered)} dari {len(COMPOUNDS)} senyawa</p>", unsafe_allow_html=True)
 
    # Group color map
    GROUP_TAG = {
        "Alkohol": "tag-teal", "Aldehid": "tag-amber", "Keton": "tag-coral",
        "Fenol": "tag-purple", "Asam Karboksilat": "tag-blue", "Ester": "tag-green",
        "Alkena": "tag-teal", "Alkuna": "tag-amber", "Karbohidrat": "tag-purple",
        "Protein": "tag-coral", "Aromatik": "tag-blue", "Asam Amino": "tag-green",
    }
 
    for c in filtered:
        tag_cls = GROUP_TAG.get(c["group"], "tag-blue")
        pos_str = ", ".join(c["positive"][:3])
        neg_str = ", ".join(c["negative"][:2])
        label = f"{c['name']}  ·  {c['formula']}  ·  {c['group']}"
        with st.expander(label):
            col_info, col_tests = st.columns([2, 3])
            with col_info:
                st.markdown(f"""
                <div style='margin-bottom:.75rem'>
                    <span style='font-size:1.2rem;font-weight:800;color:#e6edf3;font-family:Syne,sans-serif'>{c['name']}</span><br>
                    <span style='font-family:DM Mono,monospace;font-size:.9rem;color:#7d8590'>{c['formula']}</span>&nbsp;
                    <span class='tag {tag_cls}'>{c['group']}</span>
                </div>
                <p style='font-size:.85rem;color:#7d8590;line-height:1.6'>{c['desc']}</p>
                """, unsafe_allow_html=True)
 
                st.markdown("**Uji Positif:**")
                for p in c["positive"]:
                    st.markdown(f"<span style='color:#39d4a5;font-size:.85rem'>✔ {p}</span>", unsafe_allow_html=True)
                st.markdown("**Uji Negatif:**")
                for n in c["negative"]:
                    st.markdown(f"<span style='color:#f07878;font-size:.85rem'>✖ {n}</span>", unsafe_allow_html=True)
 
            with col_tests:
                st.markdown("<div style='font-family:DM Mono,monospace;font-size:.7rem;color:#7d8590;text-transform:uppercase;letter-spacing:.08em;margin-bottom:.75rem'>Hasil Uji Kualitatif</div>", unsafe_allow_html=True)
                test_items = list(c["tests"].items())
                half = (len(test_items) + 1) // 2
                tc1, tc2 = st.columns(2)
                for idx, (test_name, result) in enumerate(test_items):
                    col = tc1 if idx < half else tc2
                    is_pos = result.startswith("pos")
                    color  = "#39d4a5" if is_pos else "#f07878"
                    icon   = "✔" if is_pos else "✖"
                    result_label = "Positif" if is_pos else result.replace("neg", "Negatif").strip()
                    with col:
                        st.markdown(f"""<div style='background:#0d1117;border-radius:8px;padding:.6rem .85rem;margin-bottom:.5rem'>
                            <div style='font-family:DM Mono,monospace;font-size:.65rem;color:#7d8590;margin-bottom:2px'>{test_name.upper()}</div>
                            <div style='color:{color};font-size:.82rem;font-weight:600'>{icon} {result_label}</div>
                        </div>""", unsafe_allow_html=True)
 
 
# ════════════════════════════════════════════════════════════════════════════
# PAGE: MATERI
# ════════════════════════════════════════════════════════════════════════════
elif page == "📚 Materi Uji":
    st.markdown("<h2 style='color:#e6edf3;margin-bottom:.25rem'>📚 Materi Uji Kualitatif</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#7d8590;margin-bottom:1.5rem'>Pelajari prinsip, reaksi kimia, dan interpretasi hasil setiap uji kualitatif organik.</p>", unsafe_allow_html=True)
 
    tab_names = [f"{m['icon']} {m['title']}" for m in MATERI_LIST]
    tabs = st.tabs(tab_names)
 
    for tab, materi in zip(tabs, MATERI_LIST):
        with tab:
            col_left, col_right = st.columns([3, 2])
 
            with col_left:
                st.markdown(f"### {materi['icon']} {materi['title']}")
                st.markdown(f"<p style='color:#f0a03a;font-style:italic;font-size:.9rem'>{materi['short']}</p>", unsafe_allow_html=True)
                st.divider()
 
                st.markdown("**Prinsip Reaksi**")
                st.markdown(f"<p style='color:#c9d1d9;font-size:.9rem;line-height:1.7'>{materi['prinsip']}</p>", unsafe_allow_html=True)
 
                st.markdown("**Persamaan Reaksi**")
                st.code(materi["reaksi"], language=None)
 
            with col_right:
                st.markdown("""<div style='font-family:DM Mono,monospace;font-size:.7rem;color:#7d8590;text-transform:uppercase;letter-spacing:.08em;margin-bottom:.75rem'>HASIL UJI</div>""", unsafe_allow_html=True)
 
                st.markdown("✅ **Senyawa yang memberikan hasil positif:**")
                for item in materi["positif"]:
                    st.markdown(f"<div style='color:#39d4a5;font-size:.85rem;padding:4px 0'>• {item}</div>", unsafe_allow_html=True)
 
                st.divider()
                st.markdown("❌ **Senyawa yang memberikan hasil negatif:**")
                for item in materi["negatif"]:
                    st.markdown(f"<div style='color:#f07878;font-size:.85rem;padding:4px 0'>• {item}</div>", unsafe_allow_html=True)
 
                st.divider()
                st.info(f"💡 **Catatan Praktikum:** {materi['catatan']}")
 
