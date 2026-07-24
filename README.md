# UAS Data Mining (SIF304) — Klasifikasi Diabetes & Clustering Gerai Kopi

**Nama  :** _saipul bahri_
**NIM   :** _23146010_
**Mata Kuliah :** Data Mining (SIF304)
**Dosen Pengampu :** Teuku Rizky Noviandy, S.Kom., M.Kom.

## 📌 Deskripsi Proyek

Aplikasi web berbasis **Streamlit** yang mengimplementasikan dua model data mining:

1. **Klasifikasi (Supervised Learning)** — memprediksi risiko diabetes pasien
   menggunakan algoritma **KNN**, **Naive Bayes**, dan **Decision Tree**,
   dievaluasi dengan metrik akurasi, precision, recall, F1-score, dan confusion matrix.
2. **Clustering (Unsupervised Learning)** — mengelompokkan lokasi gerai kopi
   menggunakan **K-Means** berdasarkan koordinat lokasi, kepadatan penduduk,
   arus lalu lintas, dan jumlah kompetitor, untuk mendeteksi **zona sepi**.

## 🗂️ Struktur Proyek
```
├── Home.py                              # Halaman utama
├── pages/
│   ├── 1_Prediksi_Diabetes.py           # Halaman klasifikasi diabetes
│   └── 2_Clustering_Gerai_Kopi.py       # Halaman clustering gerai kopi
├── data/
│   ├── diabetes.csv
│   └── lokasi_gerai_kopi_clean.csv
├── requirements.txt
└── README.md
```

## 🚀 Cara Menjalankan Aplikasi Secara Lokal

1. Clone repository ini:
   ```bash
   git clone https://github.com/SaipulBahri07/UAS-Data-Mining.git
   cd NAMA_REPO
   ```
2. (Opsional tapi disarankan) buat virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan aplikasi:
   ```bash
   streamlit run Home.py
   ```
5. Aplikasi akan terbuka otomatis di browser pada `http://localhost:8501`.

## 🌐 Link Aplikasi Streamlit (Live Demo)

👉 link Streamlit Cloud :https://uasdataminingsaipul23146010.streamlit.app/

## 📊 Dataset

- **Diabetes:** [Pima Indians Diabetes Database (Kaggle)](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- **Gerai Kopi:** Dataset lokasi gerai kopi (koordinat x, y, kepadatan penduduk,
  arus lalu lintas, jumlah kompetitor, area komersial)

## 🛠️ Teknologi yang Digunakan

- Python 3
- Streamlit
- scikit-learn
- Pandas & NumPy
- Matplotlib & Seaborn
