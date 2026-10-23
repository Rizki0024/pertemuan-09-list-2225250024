print("=" * 50)
print("PRAKTIK: ANALISIS NILAI MAHASISWA".center(50))
print("=" * 50)


# FUNGSI 1: Menghitung rata-rata
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


# FUNGSI 2: Mengambil nilai yang lulus
def nilai_lulus(data, batas=60):
    hasil = []

    for angka in data:
        if angka >= batas:
            hasil.append(angka)

    return hasil


# INPUT: Data nilai mahasiswa
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
batas_lulus = 60

# PROSES
banyak_data = len(nilai)
total = sum(nilai)
rata = rata_rata(nilai)
minimum = min(nilai) if banyak_data > 0 else 0
maksimum = max(nilai) if banyak_data > 0 else 0

lulus = nilai_lulus(nilai, batas_lulus)
jumlah_lulus = len(lulus)
jumlah_belum_lulus = banyak_data - jumlah_lulus

# OUTPUT
print("\n" + "-" * 50)
print("DATA NILAI MAHASISWA".center(50))
print("-" * 50)
print("Daftar nilai       :", nilai)
print("Banyak data        :", banyak_data)

print("\n" + "-" * 50)
print("RINGKASAN STATISTIK".center(50))
print("-" * 50)
print("Total nilai        :", total)
print(f"Rata-rata          : {rata:.2f}")
print("Nilai minimum      :", minimum)
print("Nilai maksimum     :", maksimum)

print("\n" + "-" * 50)
print("HASIL KELULUSAN".center(50))
print("-" * 50)
print("Batas kelulusan    :", batas_lulus)
print("Daftar nilai lulus :", lulus)
print("Jumlah lulus       :", jumlah_lulus)
print("Belum lulus        :", jumlah_belum_lulus)

print("\n" + "=" * 50)
print("PROGRAM SELESAI".center(50))
print("=" * 50)