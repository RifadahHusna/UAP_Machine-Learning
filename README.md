# 🛒 E-Commerce Text Classification  

### Perbandingan LSTM, BERT, dan DistilBERT

Repositori ini berisi implementasi sistem **klasifikasi teks deskripsi produk e-commerce** menggunakan dataset teks.
Proyek ini membandingkan tiga pendekatan:
* **Pendekatan deep learning** (LSTM)
* **Pretrained transformer** (BERT dan DistilBERT)
   
Model bertugas dalam mengklasifikasikan teks produk ke dalam beberapa kategori e-commerce. Terdapat 4 kelas:
* **Househould**
* **Books**
* **Electronics**
* **Clothing & Accessories**

Tujuan utama proyek ini adalah membangun sistem klasifikasi teks yang **akurat, efisien, dan mudah diimplementasikan**, serta menyajikannya dalam bentuk **website berbasis Streamlit** yang dapat dijalankan secara lokal.

---

## 📂 Dataset

Dataset yang digunakan berasal dari Kaggle:

**E-Commerce Text Classification Dataset**  
🔗 https://www.kaggle.com/datasets/saurabhshahane/ecommerce-text-classification

Dataset terdiri dari dua kolom utama, yaitu **Label** (kategori produk) dan **Text** (deskripsi produk).  
Data dibaca langsung dari file CSV dengan penanganan baris bermasalah untuk mencegah error parsing.

---

## Preprocessing Data

Tahapan preprocessing dilakukan sesuai alur berikut:

1. **Pembacaan dan Validasi Data**  
   Dataset dibaca dari file CSV dengan pemetaan kolom yang sesuai.  
   Baris data yang tidak valid atau mengalami kesalahan parsing diabaikan untuk menjaga konsistensi struktur data.

2. **Pembersihan Data Kosong**  
   Data dengan nilai kosong pada kolom label atau teks dihapus.  
   Seluruh nilai label dan teks dikonversi ke tipe string untuk menghindari inkonsistensi tipe data.

3. **Sampling Data**  
   Untuk efisiensi komputasi, dataset disampling menjadi **10.000 data** dengan distribusi label yang tetap seimbang (stratified sampling).

4. **Pembersihan Teks (Text Cleaning)**  
   Setiap teks diproses melalui tahapan:
   - Konversi ke huruf kecil (lowercase)
   - Penghapusan karakter selain huruf alfabet
   - Penghapusan spasi berlebih  
   Tahapan ini bertujuan untuk mengurangi noise dan variasi yang tidak relevan pada teks.

5. **Encoding Label**  
   Label kategori diubah ke dalam bentuk numerik agar dapat diproses oleh model machine learning dan deep learning.

6. **Pembagian Data**  
   Data yang telah diproses dibagi menjadi **data latih (80%)** dan **data uji (20%)** dengan menjaga proporsi masing-masing kelas.

---

### Pemodelan

Tiga model digunakan dalam penelitian ini:

- **LSTM (Long Short-Term Memory)**  
  Model deep learning berbasis RNN yang mempelajari urutan kata dan konteks lokal dalam teks.

- **BERT (Bidirectional Encoder Representations from Transformers)**  
  Model pretrained transformer yang memahami konteks kata secara dua arah dan memberikan performa klasifikasi terbaik.

- **DistilBERT**  
  Model transformer ringan yang mempertahankan sebagian besar performa BERT dengan kebutuhan komputasi yang lebih rendah.

---

## 🌐 Implementasi Sistem

Sistem klasifikasi teks diimplementasikan dalam bentuk **website berbasis Streamlit**.  
Pengguna dapat memasukkan teks deskripsi produk, memilih model klasifikasi, dan memperoleh hasil prediksi kategori secara real-time melalui antarmuka yang interaktif.

---

## 📊 Evaluasi dan Hasil

Evaluasi dilakukan menggunakan metrik **Accuracy, Precision, Recall, dan F1-Score**.

### Perbandingan Performa Model

| Model       | Akurasi | Analisis Perbandingan |
|-------------|---------|-----------------------|
| LSTM        | 0.521   | Mampu mempelajari urutan kata, namun kurang efektif dalam menangkap konteks global pada teks panjang. |
| BERT        | 0.948   | Memberikan akurasi tinggi berkat pemahaman konteks dua arah, tetapi membutuhkan sumber daya komputasi yang besar. |
| DistilBERT | 0.956   | Menghasilkan akurasi tertinggi dengan waktu inferensi lebih cepat, sehingga lebih efisien dan cocok untuk deployment. |

---

## 🚀 Panduan Menjalankan Sistem Website Secara Lokal

Aplikasi ini merupakan sistem klasifikasi teks e-commerce berbasis **Streamlit**.  
Model **LSTM, BERT, dan DistilBERT** telah **dilatih sebelumnya menggunakan Google Colab** dengan kode: 

**Code_UAP.ipynb**


Model hasil pelatihan kemudian digunakan kembali (load model) pada aplikasi website lokal.

### 1️⃣ Persiapan Model
Sebelum menjalankan website secara lokal, pastikan:
* Proses training pada **Google Colab (`Code_UAP.ipynb`)** telah selesai
* File model hasil training sudah diunduh dari Colab
* Seluruh file model disimpan pada folder proyek lokal sesuai struktur yang ditentukan

Model yang telah dilatih tersedia di folder models. Namun dalam hal ini, untuk seluruh model (lstm, BERT, dan DistilBERT) tidak dapat diupload ke dalam direktori github karena keterbtasan ukuran file. Berikut disediakan seluruh model hasil training dalam bentuk link Google Drive. 

Link Model: https://drive.google.com/drive/folders/1W6x7zRTa-PVlMSb9BbreTaKkeyr03DIb?usp=sharing


Model tidak dilatih ulang saat website dijalankan.


---

### 2️⃣ Persiapan Lingkungan Lokal
Pastikan perangkat telah terpasang:
* **Python 3.10.16 atau lebih baru**
* **pip** sebagai package manager
* Sistem operasi Windows 

Disarankan menggunakan **virtual environment** untuk menjaga konsistensi dependensi.

Caranya : **pdm init** pada terminal lokal di laptop atau komputer masing masing ke pada folder project yang akan digunakan

---

### 3️⃣ Instalasi Dependensi
Instal seluruh library yang dibutuhkan sesuai dengan dependensi proyek, meliputi:
* Streamlit (antarmuka website)
* PyTorch (model LSTM)
* Transformers (BERT dan DistilBERT)
* Library pendukung pemrosesan teks dan data

---

Anda juga dapat menginstal code app.py untuk membangun sistem website streamlit secara lokal

---

### 4️⃣ Menjalankan Aplikasi Website
Setelah lingkungan dan dependensi siap:
* Jalankan aplikasi Streamlit dari terminal **streamlit run app.py** atau **phyton -m streamlit run app.py**
* Browser akan terbuka otomatis pada alamat **localhost**
* Aplikasi siap digunakan tanpa proses training ulang

---

### 5️⃣ Penggunaan Sistem
Pada halaman website, pengguna dapat:
- Memasukkan teks deskripsi produk e-commerce
- Memilih model klasifikasi (**LSTM / BERT / DistilBERT**)
- Melihat hasil prediksi kategori secara langsung

---

### 6️⃣ Catatan Penting
- Loading awal dapat memerlukan waktu karena proses pemuatan model
- Model Transformer akan berjalan lebih cepat jika tersedia GPU
- Pastikan versi library di lokal kompatibel dengan environment Google Colab saat training



## 🧪 Analisis Kesalahan

Kesalahan klasifikasi umumnya disebabkan oleh:
* Deskripsi produk yang terlalu singkat atau ambigu
* Tumpang tindih makna antar kategori
* Noise teks seperti typo dan simbol

Perbaikan yang dapat dilakukan meliputi augmentasi teks, penambahan konteks, serta tuning hyperparameter model.

---

## 📌 Kesimpulan

Model berbasis transformer (**BERT dan DistilBERT**) menunjukkan performa terbaik dalam klasifikasi teks e-commerce.  
**DistilBERT** menjadi pilihan yang lebih efisien untuk aplikasi berbasis web, sementara **LSTM** tetap relevan sebagai baseline deep learning.  
Proyek ini dapat dikembangkan lebih lanjut untuk kebutuhan NLP lainnya seperti sentiment analysis dan multi-language classification.

---

## 👩‍💻 Author

**Rifadah Husna**  
Machine Learning Project  
2025
