# 📖 Panduan Lengkap Pengerjaan UAS Data Mining (SIF304)

Panduan ini menjelaskan langkah demi langkah cara menyelesaikan proyek UAS-mu,
dari mulai memahami soal, menjalankan aplikasi yang sudah dibuatkan, sampai
deploy ke Streamlit Cloud dan menyusun laporan PDF.

Aplikasi lengkapnya **sudah dibuatkan dan sudah diuji berjalan** — kamu tinggal
mengikuti langkah di bawah untuk menjalankan, memahami, menyesuaikan (isi
nama/NIM), lalu deploy.

---

## 🧩 Bagian 0 — Gambaran Besar

Soal UAS meminta kamu membuat **satu aplikasi Streamlit** berisi dua bagian:

| Bagian | Jenis | Tujuan |
|---|---|---|
| A. Prediksi Diabetes | Supervised (klasifikasi) | Prediksi apakah pasien diabetes/tidak, pakai KNN, Naive Bayes, Decision Tree |
| B. Clustering Gerai Kopi | Unsupervised (clustering) | Kelompokkan lokasi gerai kopi jadi beberapa klaster & deteksi "zona sepi" |

Lalu proyek harus:
1. Disimpan di **GitHub**
2. Di-deploy ke **Streamlit Cloud**
3. Dilaporkan dalam **PDF** + link GitHub

Struktur file yang sudah disiapkan:
```
uas_project/
├── Home.py                          <- halaman utama
├── pages/
│   ├── 1_Prediksi_Diabetes.py       <- Bagian A
│   └── 2_Clustering_Gerai_Kopi.py   <- Bagian B
├── data/
│   ├── diabetes.csv
│   └── lokasi_gerai_kopi_clean.csv
├── requirements.txt
├── README.md
└── .gitignore
```

Streamlit otomatis membuat **navigasi multi-halaman** di sidebar kiri kalau
kamu punya folder `pages/` — jadi kamu tidak perlu coding navigasi manual.

---

## 🧠 Bagian 1 — Memahami Isi Kode (Wajib, jangan dilewati!)

Sebelum deploy, **pahami dulu** apa yang terjadi di tiap file, karena saat
sidang/presentasi kamu pasti ditanya. Berikut penjelasan singkat tiap bagian:

### `pages/1_Prediksi_Diabetes.py`
1. **Load data** — baca `diabetes.csv`. Nilai `0` pada kolom Glucose, BMI, dll
   dianggap data hilang (karena secara medis tidak mungkin 0), lalu diganti
   dengan median kolom tersebut.
2. **Split data** — 80% data latih, 20% data uji.
3. **Scaling** — KNN butuh data yang di-*scale* (StandardScaler) karena
   berbasis jarak; Naive Bayes & Decision Tree tidak butuh scaling.
4. **Training 3 model**: `KNeighborsClassifier`, `GaussianNB`, `DecisionTreeClassifier`.
5. **Evaluasi**: akurasi, precision, recall, F1-score ditampilkan dalam tabel.
6. **Confusion matrix**: heatmap interaktif, pilih model dari dropdown.
7. **Form prediksi**: input data pasien baru → pilih model → tombol prediksi.

### `pages/2_Clustering_Gerai_Kopi.py`
1. **Load data** — baca `lokasi_gerai_kopi_clean.csv` (kolom: x, y,
   population_density, traffic_flow, competitor_count, is_commercial).
2. **Slider jumlah klaster (k)** — kamu bisa coba k=2 sampai 8.
3. **Scaling + K-Means** — fitur di-scale lalu di-cluster.
4. **Deteksi zona sepi** — tiap klaster dihitung skor "aktivitas" dari
   kepadatan penduduk + traffic − jumlah kompetitor. Klaster dengan skor
   terendah otomatis ditandai **"Zona Sepi"**.
5. **Visualisasi scatter plot** — sebaran gerai kopi berwarna per klaster,
   zona sepi ditandai marker `x`.
6. **Form lokasi baru** — masukkan koordinat & fitur lokasi baru → sistem
   menentukan klaster & status ramai/sepi-nya.

> 💡 **Tips presentasi**: kalau dosen tanya "kenapa pakai median untuk
> mengisi missing value?" atau "kenapa KNN perlu scaling tapi Decision Tree
> tidak?", jawaban ada di penjelasan di atas — pelajari supaya bisa jawab
> dengan percaya diri.

---

## 💻 Bagian 2 — Menjalankan Aplikasi di Komputer Sendiri

1. **Install Python** (3.9–3.12) kalau belum ada — download di python.org.
2. **Ekstrak** folder proyek yang sudah kamu terima.
3. Buka terminal/command prompt, masuk ke folder proyek:
   ```bash
   cd uas_project
   ```
4. (Disarankan) buat virtual environment supaya rapi:
   ```bash
   python -m venv venv
   source venv/bin/activate        # kalau Windows: venv\Scripts\activate
   ```
5. Install semua library yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   ```
6. Jalankan aplikasi:
   ```bash
   streamlit run Home.py
   ```
7. Browser akan otomatis terbuka di `http://localhost:8501`. Coba klik-klik
   semua fitur: ubah slider k, ganti model, isi form prediksi — pastikan
   semua jalan tanpa error.

---

## ✏️ Bagian 3 — Personalisasi Sebelum Submit

Sebelum lanjut ke GitHub, edit dulu:

1. Buka `Home.py`, ganti bagian:
   ```python
   - Nama : _(isi nama kamu)_
   - NIM : _(isi NIM kamu)_
   ```
   dengan nama dan NIM asli kamu.
2. Buka `README.md`, isi juga nama & NIM di bagian atas.
3. *(Opsional tapi bagus untuk nilai tambah)* — kamu bisa menambahkan
   penjelasan singkat di tiap halaman tentang insight dari hasil clustering
   atau perbandingan model (misalnya: "Decision Tree memberi F1-score
   tertinggi karena ..."). Ini menunjukkan kamu paham, bukan cuma copy-paste.

---

## 🐙 Bagian 4 — Push ke GitHub

1. Buat akun GitHub kalau belum punya: https://github.com
2. Buat repository baru (klik tombol **New repository**):
   - Nama repo bebas, misal: `uas-datamining-diabetes-kopi`
   - Pilih **Public** (supaya Streamlit Cloud bisa akses gratis)
   - Jangan centang "Add README" (karena kita sudah punya)
3. Di terminal, dari dalam folder `uas_project`, jalankan:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: UAS Data Mining - Diabetes & Clustering"
   git branch -M main
   git remote add origin https://github.com/USERNAME/NAMA_REPO.git
   git push -u origin main
   ```
   Ganti `USERNAME` dan `NAMA_REPO` sesuai akun & repo kamu.
4. Refresh halaman GitHub-mu, pastikan semua file (termasuk folder `data/`
   dan `pages/`) sudah terupload.

> ⚠️ Kalau `git` belum terinstall di komputermu, download di
> https://git-scm.com/downloads terlebih dahulu.

---

## ☁️ Bagian 5 — Deploy ke Streamlit Cloud

1. Buka https://share.streamlit.io dan login pakai akun GitHub kamu.
2. Klik **New app**.
3. Pilih:
   - **Repository**: repo GitHub yang barusan kamu buat
   - **Branch**: `main`
   - **Main file path**: `Home.py`
4. Klik **Deploy**. Tunggu beberapa menit sampai proses build selesai
   (Streamlit Cloud akan otomatis install dari `requirements.txt`).
5. Setelah selesai, kamu akan mendapat link publik seperti:
   `https://nama-repo-kamu.streamlit.app`
6. **Tes link tersebut** dari browser lain / HP untuk memastikan aplikasi
   benar-benar bisa diakses publik.
7. Kalau ada error saat build, buka menu **Manage app → Logs** di Streamlit
   Cloud untuk melihat pesan error-nya (biasanya karena ada library yang
   belum tercantum di `requirements.txt`, atau path file yang salah).
8. Setelah berhasil, **masukkan link ini** ke bagian README.md di GitHub-mu
   (bagian "Link Aplikasi Streamlit"), lalu commit & push ulang perubahan itu.

---

## 📄 Bagian 6 — Menyusun Laporan PDF

Laporan PDF bisa memuat (urutan sesuai instruksi soal):

1. **Cover**: Judul proyek, nama, NIM, mata kuliah, dosen pengampu.
2. **Bagian A — Klasifikasi Diabetes**
   - Judul halaman & deskripsi singkat
   - Penjelasan 3 model yang digunakan (KNN, Naive Bayes, Decision Tree)
   - Tabel metrik evaluasi (akurasi, precision, recall, F1) — screenshot dari
     aplikasi
   - Screenshot confusion matrix
   - Screenshot fitur prediksi pasien baru
3. **Bagian B — Clustering Gerai Kopi**
   - Judul halaman & deskripsi singkat
   - Penjelasan metode K-Means & cara menentukan zona sepi
   - Screenshot scatter plot hasil clustering
   - Screenshot fitur cek lokasi baru
4. **Kesimpulan** singkat: model mana yang performanya paling baik, insight
   dari hasil clustering (misalnya klaster mana yang paling sepi dan
   kenapa).
5. **Lampiran**: link GitHub repository & link aplikasi Streamlit Cloud.

💡 Kamu bisa screenshot langsung dari aplikasi yang sudah live di Streamlit
Cloud, lalu susun di Word/Google Docs, dan export ke PDF.

---

## ✅ Checklist Akhir Sebelum Submit

- [ ] Aplikasi jalan lancar secara lokal (`streamlit run Home.py`)
- [ ] Nama & NIM sudah diisi di `Home.py` dan `README.md`
- [ ] Ketiga model (KNN, Naive Bayes, Decision Tree) tampil dengan metrik
      evaluasinya
- [ ] Confusion matrix bisa ditampilkan
- [ ] Form prediksi pasien baru berfungsi
- [ ] Scatter plot clustering tampil dengan warna berbeda per klaster
- [ ] Zona sepi teridentifikasi & ditandai jelas
- [ ] Form cek lokasi baru berfungsi
- [ ] Repo GitHub sudah public dan lengkap (termasuk folder `data/`)
- [ ] README.md berisi nama, NIM, penjelasan, cara run, dan link Streamlit
- [ ] Aplikasi sudah live di Streamlit Cloud dan bisa diakses publik
- [ ] Laporan PDF sudah disusun dan mencakup semua poin di atas

---

## 🆘 Troubleshooting Umum

| Masalah | Kemungkinan Penyebab & Solusi |
|---|---|
| `ModuleNotFoundError` saat deploy | Library belum ada di `requirements.txt` → tambahkan lalu commit ulang |
| App di Streamlit Cloud error "File not found" untuk `data/...csv` | Pastikan folder `data/` ikut ter-push ke GitHub (cek `.gitignore` tidak mengecualikannya) |
| Push ke GitHub ditolak (`rejected`) | Jalankan `git pull origin main --rebase` dulu sebelum push lagi |
| Streamlit Cloud build lama/gagal | Cek tab **Logs**, biasanya versi Python di `runtime.txt` atau kesalahan penulisan di requirements.txt |
| Hasil clustering berubah tiap dijalankan ulang | Pastikan `random_state=42` sudah diset di `KMeans(...)` (sudah ada di kode) |

---

Selamat mengerjakan! Kalau ada bagian yang error, cek dulu pesan error di
terminal/Logs Streamlit Cloud — biasanya pesan errornya cukup jelas
menunjukkan file dan baris mana yang bermasalah.
