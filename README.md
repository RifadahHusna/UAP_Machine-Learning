# 🛒 E-Commerce Text Classification  
### Perbandingan LSTM, BERT, dan DistilBERT

Repositori ini berisi implementasi sistem **klasifikasi teks deskripsi produk e-commerce** menggunakan pendekatan **deep learning** dan **pretrained transformer**.  
Proyek ini membandingkan performa tiga model utama, yaitu **LSTM**, **BERT**, dan **DistilBERT**, dalam mengklasifikasikan teks produk ke dalam beberapa kategori e-commerce.

Tujuan utama proyek ini adalah membangun sistem klasifikasi teks yang **akurat, efisien, dan mudah diimplementasikan**, serta menyajikannya dalam bentuk **website berbasis Streamlit** yang dapat dijalankan secara lokal.

---

## 📂 Dataset

Dataset yang digunakan berasal dari Kaggle:

**E-Commerce Text Classification Dataset**  
🔗 https://www.kaggle.com/datasets/saurabhshahane/ecommerce-text-classification

Dataset terdiri dari dua kolom utama, yaitu **Label** (kategori produk) dan **Text** (deskripsi produk).  
Data dibaca langsung dari file CSV dengan penanganan baris bermasalah untuk mencegah error parsing.

---

## 🔍 Metodologi

### Preprocessing Data

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

| Model       | Performa Umum      | Karakteristik |
|-------------|--------------------|---------------|
| LSTM        | Baik               | Stabil, namun kurang optimal pada teks panjang |
| BERT        | Sangat Baik        | Akurasi tertinggi, komputasi berat |
| DistilBERT | Baik – Sangat Baik | Efisien dan cepat untuk deployment |

---

## 🧪 Analisis Kesalahan

Kesalahan klasifikasi umumnya disebabkan oleh:
- Deskripsi produk yang terlalu singkat atau ambigu
- Tumpang tindih makna antar kategori
- Noise teks seperti typo dan simbol

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
