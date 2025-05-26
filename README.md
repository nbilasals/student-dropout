# Menyelesaikan Permasalahan Institusi Pendidikan

## 📊 Deliverables
**Tool**: Looker Studio dan Streamlit  
**Link**: 
- [Students Performance Dashboard](https://lookerstudio.google.com/reporting/ebd65a5e-c2f3-4aa0-b28f-f7644b9d70fe) 
- [Students Performance Streamlit Prediction](https://student-dropout-rcvv37srkuw2sv758cxjbr.streamlit.app/ ) 
---

## 💼 Business Understanding

### 🎯 Latar Belakang
Jaya Jaya Institute adalah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan dikenal menghasilkan lulusan berkualitas. Namun, angka **dropout** (siswa putus studi) yang cukup tinggi menjadi tantangan serius bagi keberlangsungan dan reputasi institusi ini.

Tingginya angka dropout berdampak pada:
- Penurunan angka kelulusan
- Risiko terhadap akreditasi institusi
- Menurunnya kepercayaan masyarakat

### ❗ Permasalahan Bisnis
- Tidak adanya sistem monitoring siswa berbasis data untuk deteksi dini siswa berisiko dropout
- Kurangnya strategi intervensi berbasis analisis historis dan prediksi
- Sulitnya mengidentifikasi faktor utama penyebab siswa mengalami kegagalan studi

---

## 🎯 Tujuan Proyek
- Mengidentifikasi faktor-faktor utama penyebab dropout siswa
- Mengembangkan model machine learning untuk memprediksi kemungkinan dropout
- Menyusun dashboard interaktif untuk monitoring dan pengambilan keputusan oleh pihak manajemen akademik

---

## 🔍 Cakupan Proyek
- Data preparation & data cleaning
- Exploratory Data Analysis (EDA) untuk menemukan insight
- Pembuatan dashboard Looker faktor penyebab dropout
- Pemodelan machine learning untuk prediksi status siswa (dropout/lulus)

---

## 🧪 Preparation
### Data Source:
Data yang digunakan merupakan dataset dari Dicoding, yang berasal dari ari sebuah institusi pendidikan tinggi dan dikompilasi dari beberapa database yang terpisah. Isinya mencakup informasi mahasiswa dari berbagai program studi sarjana, seperti agronomi, desain, pendidikan, keperawatan, jurnalistik, manajemen, layanan sosial, dan teknologi. Data yang dikumpulkan meliputi informasi yang sudah diketahui saat mahasiswa pertama kali mendaftar, termasuk riwayat akademik, data demografis, serta faktor sosial ekonomi. 
- [Students' Performance data](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance) 

### Setup Environment
Berikut langkah-langkah untuk menyiapkan dan menjalankan proyek di lingkungan lokal:
#### 1. Clone Repository
Clone repositori dari GitHub ke direktori lokal:

```bash
git clone https://github.com/nbilasals/student-dropout-predictor.git
```
#### 2. Masuk ke Direktori Proyek
Pindah ke directori proyek:
```
cd student-dropout-predictor
```
#### 3. Buat Virtual Environment
Buat environment Python terisolasi untuk menghindari konflik dependensi:
``` bash
virtualenv venv
```

#### 4. Aktifkan Virtual Environment
Aktifkan environment yang telah dibuat:
```
venv\Scripts\activate
```

#### 5. Install Dependencies
Instal semua dependensi yang dibutuhkan proyek:

```
pip install -r requirements.txt
```

## 📈 Business Dashboard

Dashboard dibuat menggunakan **Looker Studio**, menampilkan insight visual dari berbagai variabel yang memengaruhi status akademik siswa.

![image](https://github.com/user-attachments/assets/751212d0-70d5-47ac-be0e-8fe0fef3cba2)


### 🎯 Insight utama dalam dashboard:
- **Overview Akademik**:
  - Jumlah siswa
  - Rata-rata usia
  - Graduation rate
  - Dropout rate
  - Rata-rata admission grade
  - Rata-rata previous grade

- **Distribusi Status Siswa Berdasarkan**:
  - Gender
  - Status penerima beasiswa (scholarship)
  - Status debitur (debt)

- **Perbandingan Status Siswa (Graduate vs Dropout)**:
  - Berdasarkan gender
  - Berdasarkan beasiswa
  - Berdasarkan status debitur

- **Distribusi Usia saat Enrolment**:
  - Dilihat dari admission grade dan status akademik

---

## 🤖 Machine Learning Model

### 🧪 Model yang Dicoba:
- Decision Tree (`DecisionTreeClassifier`)
- Random Forest (`RandomForestClassifier`)
- Logistic Regression (`LogisticRegression`)
- K-Nearest Neighbors (`KNeighborsClassifier`)
- AdaBoost (`AdaBoostClassifier`)
- XGBoost (`XGBClassifier`)
- SVM (`svm.SVC`)

### ✅ Model Terbaik:
**Ensemble Voting Classifier**  
```python
VotingClassifier(estimators=[('rfc', rfc), ('lr', lr), ('abc', abc), ('xbc', xbc)], voting='hard')
```
📊 Performance:
Accuracy: 80.34%|

Model ini kemudian dikembangkan menjadi sistem prediksi untuk membantu institusi pendidikan dalam mengidentifikasi siswa yang berisiko tinggi mengalami dropout. Dengan adanya sistem ini, pihak institusi dapat melakukan intervensi secara lebih dini dan tepat sasaran guna meningkatkan keberhasilan akademik siswa.
![image](https://github.com/user-attachments/assets/30884fc4-14d2-4864-8131-2740d9f4644e)

Aplikasi ini dibangun menggunakan framework **Streamlit** sehingga mudah digunakan dan dapat dijalankan secara lokal. Untuk menjalankan aplikasi, gunakan perintah berikut pada terminal:

```bash
streamlit run app.py
```

Dapat diakses melalu Steamlit Community Cloud : [Students Performance Prediction](https://student-dropout-rcvv37srkuw2sv758cxjbr.streamlit.app/) 

## 🧠 Insight & Temuan Utama

- **Graduation Rate**: 49.9%
- **Dropout Rate**: 32.1% _(1421 siswa dari total 4424)_

### 🎓 Gender Distribution
- **Perempuan**: 2868 siswa (64.83%)
- **Laki-laki**: 1556 siswa (35.17%)

### 🎓 Status Akademik per Gender
- **Graduate**:
  - Perempuan: 1661
  - Laki-laki: 548
- **Dropout**:
  - Perempuan ≈ Laki-laki _(hampir setara)_

### 🎓 Beasiswa (Scholarship)
- Hanya **24.8%** siswa yang menerima beasiswa (1099 siswa)
- Dari penerima beasiswa:
  - **Graduate**: 835 siswa
  - **Dropout**: 134 siswa

### 💸 Status Keuangan (Debt)
- **503 siswa** (11.4%) memiliki utang
- Dari yang memiliki utang:
  - **Dropout**: 312 siswa
  - **Graduate**: 101 siswa
- 🔥 *Indikasi kuat bahwa faktor finansial memengaruhi tingkat dropout*

---

## ✅ Recommended Action Items

Berikut beberapa rekomendasi strategis untuk menurunkan tingkat dropout siswa:

### 💸 1. Perluasan Program Beasiswa
Fokus pada siswa dari latar belakang finansial rentan yang punya potensi akademik, untuk mencegah mereka dropout karena faktor biaya.

### 🧾 2. Opsi Pembayaran Cicilan
Sediakan skema pembayaran kuliah dengan cicilan bunga 0% atau penghapusan sebagian utang bagi siswa berprestasi tapi sedang kesulitan ekonomi.

### ⏳ 3. Program Gap Year & Orientasi Ulang
Sediakan program jeda kuliah (gap year) yang dilengkapi orientasi dan pendampingan khusus bagi siswa yang kembali studi agar mereka bisa menyesuaikan diri.

### 📚 4. Bimbingan Belajar Khusus
Tawarkan program remedial untuk siswa dengan nilai rendah (admission & previous grade), terutama untuk yang berusia lebih tua atau sudah menikah.

### 🧠 5. Layanan Psikologis & Konseling
Bangun pusat bantuan psikologis dan konseling finansial untuk mendukung siswa dalam menghadapi tekanan akademik dan ekonomi.

---

## 🧾 Kesimpulan

Tingkat kelulusan mahasiswa yang hanya mencapai **49.9%** dan dropout sebesar **32.1%** menunjukkan bahwa hampir separuh dari populasi mahasiswa belum berhasil menyelesaikan studinya. Temuan ini makin mengkhawatirkan saat dikaitkan dengan data beasiswa dan status keuangan:

- Mayoritas mahasiswa yang dropout tidak menerima beasiswa dan memiliki utang, yang menunjukkan bahwa **faktor ekonomi memainkan peran besar dalam keberhasilan studi mahasiswa**.
- **Mahasiswa perempuan lebih banyak yang lulus dibanding laki-laki**, tetapi jumlah dropout di kedua gender hampir setara.
- **Mahasiswa yang menerima beasiswa memiliki peluang kelulusan lebih tinggi**, sementara yang memiliki utang cenderung lebih banyak mengalami dropout.

Masalah ini tidak bisa diselesaikan hanya dengan solusi tunggal. Diperlukan pendekatan menyeluruh yang menggabungkan aspek finansial, akademik, dan psikologis agar institusi pendidikan dapat menciptakan lingkungan belajar yang lebih inklusif dan suportif.

Dengan menerapkan rekomendasi yang telah dipaparkan, diharapkan **tingkat kelulusan meningkat dan dropout menurun secara signifikan**, menciptakan ekosistem pendidikan yang lebih sehat dan berkelanjutan.

