# UAP_Machine-Learning

Siap 👍
Di bawah ini **sudah dalam format `README.md` GitHub** (Markdown), **langsung bisa kamu copy–paste tanpa diedit lagi**.

---

````md
# 🛒 E-Commerce Text Classification  
**Perbandingan LSTM, BERT, dan DistilBERT**

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk melakukan **klasifikasi teks deskripsi produk e-commerce** ke dalam beberapa kategori menggunakan pendekatan **deep learning** dan **pretrained transformer**.  
Tiga model yang digunakan dan dibandingkan dalam proyek ini adalah:

- **LSTM (Long Short-Term Memory)**
- **BERT (Bidirectional Encoder Representations from Transformers)**
- **DistilBERT**

Sistem ini diimplementasikan dalam bentuk **website berbasis Streamlit** yang dapat dijalankan secara lokal.

---

## 📂 Dataset
Dataset yang digunakan adalah **E-Commerce Text Classification Dataset** dari Kaggle:

🔗 https://www.kaggle.com/datasets/saurabhshahane/ecommerce-text-classification

### Karakteristik Dataset
- Format: CSV
- Kolom:
  - `Label` → kategori produk
  - `Text` → deskripsi produk
- Contoh kategori:
  - Clothing
  - Electronics
  - Household
  - Books

---

## 🔧 Preprocessing Data
Tahapan preprocessing data yang dilakukan adalah sebagai berikut:

1. **Load Dataset**
   - Dataset dibaca dari file CSV tanpa header.
   - Kolom dimapping secara manual menjadi `Label` dan `Text`.
   - Baris bermasalah dilewati untuk mencegah error parsing.

2. **Pembersihan Data**
   - Menghapus data yang memiliki nilai kosong (NaN).
   - Mengubah seluruh teks menjadi huruf kecil.
   - Menghapus karakter selain huruf.
   - Menghapus spasi berlebih.

3. **Sampling Data**
   - Dataset disampling menjadi **10.000 data** menggunakan **stratified sampling** agar distribusi label tetap seimbang.

4. **Encoding Label**
   - Label kategori dikonversi menjadi nilai numerik menggunakan **LabelEncoder**.
   - Mapping label disimpan untuk proses inference.

5. **Split Data**
   - Data dibagi menjadi:
     - 80% data latih
     - 20% data uji
   - Pembagian dilakukan secara stratified.

---

## 🤖 Model yang Digunakan

### 1️⃣ LSTM (Long Short-Term Memory)
- Menggunakan embedding layer untuk representasi kata
- Mampu menangkap pola sekuensial pada teks
- Digunakan sebagai baseline model

**Kelemahan:**
- Performa lebih rendah dibanding transformer
- Kurang optimal untuk teks panjang

---

### 2️⃣ BERT
- Menggunakan model pretrained `bert-base-uncased`
- Memahami konteks dua arah (bidirectional)
- Memberikan performa klasifikasi terbaik

**Kelemahan:**
- Ukuran model besar
- Waktu training dan inference lebih lama

---

### 3️⃣ DistilBERT
- Versi ringan dari BERT
- Lebih cepat dan efisien
- Cocok untuk deployment website

**Keunggulan:**
- Akurasi mendekati BERT
- Waktu inference lebih cepat
- Ukuran model lebih kecil

---

## 📊 Hasil Evaluasi dan Analisis

| Model       | Akurasi        | Kecepatan | Ukuran Model |
|------------|----------------|-----------|--------------|
| LSTM       | Rendah–Sedang  | Lambat    | Kecil        |
| BERT       | Tinggi         | Lambat    | Besar        |
| DistilBERT | Tinggi         | Cepat     | Sedang       |

### Analisis Perbandingan
- **BERT** menghasilkan akurasi tertinggi dalam klasifikasi teks.
- **DistilBERT** memberikan keseimbangan terbaik antara akurasi dan efisiensi.
- **LSTM** dapat digunakan sebagai pembanding, namun kalah performa dari model transformer.

---

## 🌐 Panduan Menjalankan Website Secara Lokal

### 1️⃣ Clone Repository
```bash
git clone https://github.com/username/nama-repo.git
cd nama-repo
````

### 2️⃣ Buat Virtual Environment (Opsional)

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependency

```bash
pip install -r requirements.txt
```

### 4️⃣ Jalankan Aplikasi Streamlit

```bash
streamlit run app.py
```

### 5️⃣ Akses Website

Buka browser dan akses:

```
http://localhost:8501
```

---

## 📌 Kesimpulan

Model berbasis **transformer (BERT dan DistilBERT)** terbukti lebih unggul dibandingkan **LSTM** dalam tugas klasifikasi teks e-commerce.
Untuk implementasi pada website, **DistilBERT** menjadi pilihan paling optimal karena efisien dan tetap memberikan performa tinggi.

```

---

Kalau kamu mau, aku bisa:
- Menyesuaikan README dengan **nama repo & struktur folder kamu**
- Menambahkan **hasil akurasi aktual dari training**
- Menambahkan **screenshot Streamlit**
- Membuat versi **bahasa Inggris**

Tinggal bilang saja 👌
```
