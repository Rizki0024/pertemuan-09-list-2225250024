print("=" * 45)
print("LATIHAN 4: AGREGASI NILAI".center(45))
print("=" * 45)

# INPUT: Daftar nilai mahasiswa
nilai = [75, 80, 65, 90, 88]

# PROSES
total = sum(nilai)
banyak = len(nilai)
rata_rata = total / banyak
minimum = min(nilai)
maksimum = max(nilai)

# OUTPUT
print("\n" + "-" * 45)
print("RINGKASAN STATISTIK NILAI".center(45))
print("-" * 45)
print("Daftar nilai :", nilai)
print("Banyak data  :", banyak)
print("Total nilai  :", total)
print(f"Rata-rata    : {rata_rata:.2f}")
print("Nilai minimum:", minimum)
print("Nilai maksimum:", maksimum)
print("=" * 45)
print("PROGRAM SELESAI".center(45))
print("=" * 45)