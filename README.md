# 💤 Prediksi Kualitas Tidur Menggunakan Logistic Regression & Random Forest

## 📘 Deskripsi Proyek
Proyek ini bertujuan untuk **memprediksi kualitas tidur seseorang** berdasarkan faktor gaya hidup dan kesehatan seperti durasi tidur, aktivitas fisik, tingkat stres, dan detak jantung.  
Model yang digunakan adalah:
- **Logistic Regression**
- **Random Forest Classifier**

Dataset yang digunakan:  
[`Sleep_health_and_lifestyle_dataset.csv`](./Sleep_health_and_lifestyle_dataset.csv)

---

## 📊 Fitur Dataset
Beberapa fitur yang digunakan dalam penelitian ini meliputi:

| Fitur | Deskripsi |
|-------|------------|
| Age | Usia responden |
| Sleep Duration | Durasi tidur (jam) |
| Physical Activity Level | Tingkat aktivitas fisik |
| Stress Level | Skala tingkat stres |
| Heart Rate | Detak jantung per menit |
| Daily Steps | Jumlah langkah per hari |
| Quality of Sleep | Label target (1–5) |

---

## ⚙️ Alur Pengerjaan
1. **Load Dataset**  
   Membaca file CSV dan menampilkan struktur data.
2. **Preprocessing**  
   - Menghapus kolom tidak relevan  
   - Mengatasi nilai kategorikal dengan *Label Encoding*  
   - Melakukan *Standardization* pada fitur numerik  
3. **EDA (Exploratory Data Analysis)**  
   - Distribusi kelas target  
   - Korelasi antar fitur  
   - Histogram dan Heatmap  
4. **Modeling**  
   - Logistic Regression  
   - Random Forest  
5. **Evaluasi**  
   - Akurasi model  
   - *Classification report*  
   - Confusion Matrix  

---

## 📈 Hasil Model
| Model | Akurasi | Catatan |
|--------|----------|----------|
| Logistic Regression | ~XX% | Model sederhana dan cepat |
| Random Forest | ~XX% | Performa lebih tinggi pada dataset non-linear |

> *Nilai akurasi akan bervariasi tergantung dataset dan random seed.*

---

## 🧠 Struktur Direktori
