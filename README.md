# Pertemuan 09 — List dan Pengolahan Data Numerik

**Nama:** Rizki Ramadan 
**NIM:** 2225250024
**Kelas:** 3F

## 1. Tujuan

Mempelajari penggunaan list Python untuk menyimpan dan mengolah kumpulan data numerik, termasuk mengakses elemen, memodifikasi data, menghitung statistik, memfilter nilai kelulusan, dan menggunakan fungsi.

## 2. Struktur Program

- `latihan/01_buat_list.py` — membuat list dan menghitung banyak elemen.
- `latihan/02_indeks_slicing.py` — mengakses elemen dengan indeks dan slicing.
- `latihan/03_manipulasi_list.py` — mengubah, menambah, menyisipkan, dan menghapus elemen.
- `latihan/04_agregasi_nilai.py` — menghitung total, rata-rata, minimum, dan maksimum.
- `latihan/05_filter_kelulusan.py` — memilih nilai yang memenuhi batas kelulusan.
- `latihan/06_fungsi_statistik.py` — menghitung rata-rata dengan fungsi.
- `praktik/analisis_nilai_mahasiswa.py` — menganalisis nilai mahasiswa dan merangkum hasil kelulusan.

## 3. Cara Menjalankan

Buka folder proyek di VS Code, lalu buka terminal. Jalankan program utama dengan:

```bash
python praktik/analisis_nilai_mahasiswa.py
```

Jika perintah `python` tidak dikenali, coba `python3 praktik/analisis_nilai_mahasiswa.py`.

Untuk menjalankan latihan, ganti nama file sesuai latihan yang ingin diuji, misalnya:

```bash
python latihan/01_buat_list.py
```

## 4. Test Case

| Data atau kondisi | Hasil yang diharapkan | Hasil aktual | Status |
|---|---|---|---|
| `[60, 70, 80]` — rata-rata | `70.00` | Isi setelah diuji | Belum diuji |
| `[60, 70, 80]` — minimum/maksimum | `60 / 80` | Isi setelah diuji | Belum diuji |
| `[60, 70, 80]` — jumlah lulus | `3` | Isi setelah diuji | Belum diuji |
| `[59, 60, 61]` — batas lulus 60 | `2` nilai lulus | Isi setelah diuji | Belum diuji |
| `[]` — rata-rata list kosong | `0`, tidak error | Isi setelah diuji | Belum diuji |

## 5. Refleksi

**Hal yang saya pahami:**  
List memungkinkan banyak nilai disimpan dalam satu variabel dan diolah menggunakan indeks, perulangan, serta fungsi seperti `sum()`, `len()`, `min()`, dan `max()`.

**Kesalahan yang berhasil diperbaiki:**  
[Tuliskan kesalahan yang benar-benar kamu alami dan cara memperbaikinya.]

**Kesimpulan:**  
List memudahkan pengolahan kumpulan data numerik. Pengujian dengan data normal, nilai batas, dan list kosong membantu memastikan program berjalan sesuai kebutuhan.

## 6. Sumber Referensi

1. Modul Pertemuan 09 — List/Array dan Pengolahan Data Numerik Sederhana. Materi perkuliahan yang menjadi acuan pengerjaan latihan, praktik analisis nilai mahasiswa, dan kuis formatif.
2. OpenAI. (2026). ChatGPT [Alat bantu kecerdasan buatan]. https://chatgpt.com/.

Bantuan AI digunakan untuk membantu memahami materi dan menyusun contoh solusi. Kode, pengujian, dan penjelasan akhir akan diperiksa kembali agar dapat dipahami dan dipertanggungjawabkan.
