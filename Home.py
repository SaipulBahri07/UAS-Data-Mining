import streamlit as st  # type: ignore[import]

st.set_page_config(
    page_title="UAS Data Mining - Diabetes & Gerai Kopi",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<div class="identity-strip">
    <span class="identity-label">Mahasiswa</span>
    <span class="pill strong">Saipul Bahri</span>
    <span class="pill">NIM 23146010</span>
    <span class="pill">Data Mining (SIF304)</span>
    <span class="pill">Dosen: Teuku Rizky Noviandy, S.Kom., M.Kom.</span>
</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# Custom styling — split identity: espresso/latte (gerai kopi) meets
# clinical teal (diabetes), joined by a shared cream canvas.
# ----------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,500&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap');

:root{
    --espresso:#2C1B12;
    --latte:#C9A77C;
    --cream:#F7F1E6;
    --teal:#0E5C56;
    --mint:#E7F2EF;
    --ink:#26201A;
}

#MainMenu, footer, header {visibility: hidden;}
.block-container{padding-top:2rem; padding-bottom:3rem; max-width:1100px;}
html, body, [class*="css"]{font-family:'Inter', sans-serif; color:var(--ink);}

/* ---------- Eyebrow ---------- */
.eyebrow{
    font-family:'JetBrains Mono', monospace;
    font-size:0.72rem;
    letter-spacing:0.18em;
    text-transform:uppercase;
    color:var(--teal);
    display:flex;
    align-items:center;
    gap:10px;
    margin-bottom:0.6rem;
}
.eyebrow::before{
    content:"";
    width:26px; height:1px;
    background:var(--teal);
    display:inline-block;
}

/* ---------- Hero ---------- */
.hero-title{
    font-family:'Fraunces', serif;
    font-weight:600;
    font-size:2.6rem;
    line-height:1.15;
    color:var(--espresso);
    margin:0 0 0.9rem 0;
}
.hero-title .accent{
    font-style:italic;
    font-weight:500;
    color:var(--teal);
}
.hero-sub{
    font-size:1.02rem;
    color:#5b5148;
    max-width:640px;
    line-height:1.65;
    margin-bottom:0.2rem;
}

.hero-divider{
    height:2px;
    margin:1.8rem 0 2rem 0;
    background:linear-gradient(90deg, var(--espresso) 0%, var(--latte) 45%, var(--teal) 100%);
    border-radius:2px;
}

/* ---------- Split cards ---------- */
.card{
    border-radius:18px;
    padding:1.7rem 1.6rem 1.5rem 1.6rem;
    height:100%;
    position:relative;
    overflow:hidden;
}
.card-coffee{
    background:var(--espresso);
    color:var(--cream);
}
.card-health{
    background:var(--mint);
    color:var(--espresso);
    border:1px solid #cfe4df;
}
.card-tag{
    font-family:'JetBrains Mono', monospace;
    font-size:0.68rem;
    letter-spacing:0.14em;
    text-transform:uppercase;
    opacity:0.75;
    margin-bottom:0.7rem;
    display:block;
}
.card-coffee .card-tag{color:var(--latte);}
.card-health .card-tag{color:var(--teal);}

.card-title{
    font-family:'Fraunces', serif;
    font-weight:600;
    font-size:1.4rem;
    margin-bottom:0.6rem;
}
.card-body{
    font-size:0.93rem;
    line-height:1.6;
    opacity:0.92;
}
.card-ring{
    position:absolute;
    width:150px; height:150px;
    border-radius:50%;
    border:14px solid var(--latte);
    opacity:0.18;
    top:-55px; right:-55px;
}
.card-pulse{
    position:absolute;
    bottom:14px; right:16px;
    opacity:0.35;
}

/* ---------- Nav hint ---------- */
.nav-hint{
    margin-top:2.1rem;
    font-size:0.85rem;
    color:#7a6f63;
    display:flex;
    align-items:center;
    gap:8px;
}
.nav-hint b{color:var(--espresso);}

/* ---------- Footer identity strip ---------- */
.identity-strip{
    margin-top:2.6rem;
    border-top:1px solid #e4dccb;
    padding-top:1.4rem;
    display:flex;
    flex-wrap:wrap;
    gap:0.6rem 0.8rem;
    align-items:center;
}
.identity-label{
    font-family:'JetBrains Mono', monospace;
    font-size:0.68rem;
    letter-spacing:0.12em;
    text-transform:uppercase;
    color:#a89c8a;
    margin-right:0.4rem;
}
.pill{
    font-size:0.83rem;
    padding:0.32rem 0.78rem;
    border-radius:999px;
    background:var(--cream);
    border:1px solid #e4dccb;
    color:var(--espresso);
}
.pill.strong{
    background:var(--espresso);
    color:var(--cream);
    border:none;
    font-weight:600;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# Hero
# ----------------------------------------------------------------------
st.markdown("""
<div class="eyebrow">UAS · Data Mining · SIF304</div>
<div class="hero-title">Aplikasi UAS <span class="accent">Data Mining</span></div>
<div class="hero-sub">
Implementasi Supervised dan Unsupervised Learning — dua model, satu aplikasi.
Dibangun untuk memenuhi tugas UAS mata kuliah <b>Data Mining (SIF304)</b>.
</div>
<div class="hero-divider"></div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# Two feature cards (content identical to before — diabetes & coffee)
# ----------------------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card card-health">
        <span class="card-tag">Supervised · Klasifikasi</span>
        <div class="card-title">🩺 Prediksi Risiko Diabetes</div>
        <div class="card-body">
            Model klasifikasi (KNN, Naive Bayes, Decision Tree) untuk memprediksi
            apakah seorang pasien berisiko mengidap diabetes berdasarkan data medis
            seperti kadar glukosa, BMI, usia, dan jumlah kehamilan.
        </div>
        <svg class="card-pulse" width="90" height="24" viewBox="0 0 90 24" fill="none">
            <path d="M0 12 H24 L30 2 L38 22 L44 12 H90" stroke="#0E5C56" stroke-width="2" fill="none"/>
        </svg>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card card-coffee">
        <div class="card-ring"></div>
        <span class="card-tag">Unsupervised · Clustering</span>
        <div class="card-title">☕ Clustering Lokasi Gerai Kopi</div>
        <div class="card-body">
            Model clustering (K-Means) untuk mengelompokkan lokasi gerai kopi
            berdasarkan data spasial dan lingkungan, serta mendeteksi zona
            dengan potensi pelanggan rendah (zona sepi).
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="nav-hint">👈 Pilih salah satu halaman lewat menu di <b>sidebar kiri</b> untuk mulai eksplorasi.</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# Identity footer
# ----------------------------------------------------------------------
st.markdown("""
<div class="identity-strip">
    <span class="identity-label">Mahasiswa</span>
    <span class="pill strong">Saipul Bahri</span>
    <span class="pill">NIM 23146010</span>
    <span class="pill">Data Mining (SIF304)</span>
    <span class="pill">Dosen: Teuku Rizky Noviandy, S.Kom., M.Kom.</span>
</div>
""", unsafe_allow_html=True)