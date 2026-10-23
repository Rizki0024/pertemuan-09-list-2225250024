print("=" * 45)
print("LATIHAN 3: MANIPULASI LIST".center(45))
print("=" * 45)

# INPUT: Daftar nilai awal
nilai = [75, 80, 65]

print("\nDaftar nilai awal :", nilai)

# PROSES: Mengubah elemen indeks 1
nilai[1] = 82
print("Setelah diubah    :", nilai)

# PROSES: Menambahkan nilai di akhir
nilai.append(90)
print("Setelah append    :", nilai)

# PROSES: Menyisipkan nilai pada indeks 1
nilai.insert(1, 70)
print("Setelah insert    :", nilai)

# PROSES: Menghapus nilai 65
nilai.remove(65)
print("Setelah remove    :", nilai)

print("\n" + "=" * 45)
print("HASIL AKHIR LIST".center(45))
print("=" * 45)
print("Daftar nilai akhir:", nilai)
print("=" * 45)
print("PROGRAM SELESAI".center(45))
print("=" * 45)