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

## Cara Menjalankan

Buka terminal di direktori utama repositori ini, lalu jalankan program utama menggunakan perintah berikut:

```bash
python tugas/kalkulator_koordinat.py
python latihan/01_biodata.py
python latihan/02_persegi_panjang.py
python latihan/03_konversi_suhu.py
python latihan/04_nilai_akhir.py

## Hasil Pengujian Tugas Utama

Kasus,"Titik 1 (x1​,y1​)","Titik 2 (x2​,y2​)",Jarak,Titik Tengah
1,"(0,0)","(3,4)",5.00,"(1.50,2.00)"
2,"(1,2)","(4,6)",5.00,"(2.50,4.00)"
3,"(−2,3)","(4,−5)",10.00,"(1.00,−1.00)"
