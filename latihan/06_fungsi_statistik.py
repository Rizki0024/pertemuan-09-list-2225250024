print("=" * 45)
print("LATIHAN 6: FUNGSI STATISTIK".center(45))
print("=" * 45)

# FUNGSI: Menghitung rata-rata
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


# INPUT
nilai = [75, 80, 65, 90, 88]

# OUTPUT
print("\n" + "-" * 45)
print("HASIL PERHITUNGAN".center(45))
print("-" * 45)
print("Daftar nilai :", nilai)
print(f"Rata-rata    : {rata_rata(nilai):.2f}")
print("List kosong  :", rata_rata([]))
print("=" * 45)
print("PROGRAM SELESAI".center(45))
print("=" * 45)