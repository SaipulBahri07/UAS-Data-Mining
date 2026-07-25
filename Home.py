import streamlit as st  # type: ignore[import]

st.set_page_config(
    page_title="UAS Data Mining - Diabetes & Gerai Kopi",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Aplikasi UAS Data Mining")
st.subheader("Implementasi Supervised dan Unsupervised Learning")

st.markdown("""
Selamat datang! Aplikasi ini dibuat untuk memenuhi tugas UAS mata kuliah **Data Mining (SIF304)**.

Aplikasi ini terdiri dari dua bagian utama, silakan pilih melalui menu di **sidebar kiri**:
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🩺 Prediksi Risiko Diabetes")
    st.write("""
    Model klasifikasi (KNN, Naive Bayes, Decision Tree) untuk memprediksi
    apakah seorang pasien berisiko mengidap diabetes berdasarkan data medis
    seperti kadar glukosa, BMI, usia, dan jumlah kehamilan.
    """)

with col2:
    st.markdown("### ☕ Clustering Lokasi Gerai Kopi")
    st.write("""
    Model clustering (K-Means) untuk mengelompokkan lokasi gerai kopi
    berdasarkan data spasial dan lingkungan, serta mendeteksi zona
    dengan potensi pelanggan rendah (zona sepi).
    """)

st.markdown("---")
st.markdown("""
**Identitas Mahasiswa**
- Nama : _Saipul Bahri_
- NIM : _23146010_
- Mata Kuliah : Data Mining (SIF304)
- Dosen Pengampu : Teuku Rizky Noviandy, S.Kom., M.Kom.
""")
