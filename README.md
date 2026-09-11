# pertemuan-02-dasar-python-2225250002

## Identitas
* **Nama**: [Nasywaa Zaafarani Kurniawan]
* **NIM**: [2225250002]
* **Kelas**: [3A]

---

## Tujuan Repositori
Repositori ini dibuat untuk memenuhi tugas praktikum Pertemuan 2 mata kuliah Algoritma dan Pemrograman. Repositori ini berisi latihan penggunaan sintaks dasar Python, seperti manipulasi *variable*, *input/output*, konversi tipe data, serta pembuatan program sederhana seperti perhitungan geometri, konversi suhu, penentuan nilai akhir, dan kalkulator koordinat.

---

## Daftar dan Fungsi Berkas

### Folder `latihan/`
* **`01_biodata.py`**: Meminta input identitas dan tahun lahir pengguna untuk menampilkan kartu biodata terformat serta menghitung perkiraan umur di tahun 2026.
* **`02_persegi_panjang.py`**: Menerima input panjang dan lebar (float) untuk menghitung serta menampilkan luas ($cm^2$) dan keliling ($cm$) dengan format 2 angka desimal.
* **`03_konversi_suhu.py`**: Menerima input suhu dalam Celsius (float) lalu mengonversikannya ke Fahrenheit dan Kelvin.
* **`04_nilai_akhir.py`**: Menghitung nilai akhir mahasiswa berdasarkan input nilai Tugas (20%), UTS (30%), dan UAS (50%).

### Folder `tugas/`
* **`kalkulator_koordinat.py`**: Program utama untuk menghitung jarak antara dua titik koordinat $(x_1, y_1)$ dan $(x_2, y_2)$ serta mencari titik tengahnya.

---

## Hasil Pengujian Tugas Utama

## Tabel Hasil Pengujian (`kalkulator_koordinat.py`)

| Kasus | Titik 1 (x1, y1) | Titik 2 (x2, y2) | Jarak | Titik Tengah |
| :---: | :---: | :---: | :---: | :---: |
| 1 | (0, 0) | (3, 4) | 5.00 | (1.50, 2.00) |
| 2 | (1, 2) | (4, 6) | 5.00 | (2.50, 4.00) |
| 3 | (-2, 3) | (4, -5) | 10.00 | (1.00, -1.00) |

---

## Cara Menjalankan

Buka terminal di direktori utama repositori ini, lalu jalankan program utama menggunakan perintah berikut:

```bash
python tugas/kalkulator_koordinat.py
python latihan/01_biodata.py
python latihan/02_persegi_panjang.py
python latihan/03_konversi_suhu.py
python latihan/04_nilai_akhir.py
```

## Refleksi Singkat dan Sumber

### Refleksi
Dalam praktikum ini, saya mempelajari konsep dasar pemrosesan *input* dan *output* pada Python, casting tipe data, serta penggunaan *f-string* untuk format desimal (`:.2f`). 

Hal yang paling mudah saya pahami adalah logika rumus matematikanya (seperti penjumlahan, pengurangan, perkalian, dan pembagian). Namun, kendala yang sering saya hadapi adalah penulisan sintaks/perintah Python (seperti lupa nama fungsi bawaan) serta kesalahan ketik (*typo*) pada penulisan nama variabel. Ketika menemukan kendala atau kode yang belum dipahami, saya dibantu oleh AI Gemini untuk menjelaskannya kembali.

### Sumber yang Digunakan
1. Modul Praktikum Algoritma dan Pemrograman Pertemuan 02.
2. Channel YouTube **Bro Code** (Materi dasar pemrograman Python).
3. Bantuan Asisten AI Gemini (untuk penjelasan konsep, solusi kendala kode, dan bantuan penulisan dokumen).
