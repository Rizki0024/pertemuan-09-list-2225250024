print("=" * 45)
print("LATIHAN 5: FILTER KELULUSAN".center(45))
print("=" * 45)

# INPUT
nilai = [75, 55, 80, 60, 45, 90]
batas_lulus = 60
lulus = []

# PROSES
for angka in nilai:
    if angka >= batas_lulus:
        lulus.append(angka)

# OUTPUT
print("\n" + "-" * 45)
print("HASIL SELEKSI KELULUSAN".center(45))
print("-" * 45)
print("Daftar nilai     :", nilai)
print("Batas kelulusan  :", batas_lulus)
print("Nilai yang lulus :", lulus)
print("Jumlah lulus     :", len(lulus))
print("Belum lulus      :", len(nilai) - len(lulus))
print("=" * 45)
print("PROGRAM SELESAI".center(45))
print("=" * 45)