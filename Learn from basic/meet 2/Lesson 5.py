print(5 < 10) #belajar pembanding, hasilnya adalah benar
print(5 > 10) #hasilnya adalah salah
#dalam pembanding, jawaban yang digunakan biasanya menggunakan tipe data Boolean
print("Apakah benar jika nilai dari 2 < (lebih kecil) dari 3? ")
contoh = 2 < 3
print(f"jawabannya adalah {contoh}")

# Kasus 1: Membandingkan dua angka
angka_1 = float(input("masukkan angka 1: "))
angka_2 = float(input("masukkan angka 2: "))

# Perbandingan
if angka_1 > angka_2:
    print("Hasil: Benar, angka pertama lebih besar dari angka kedua.")
else:
    print("Hasil: Salah, angka pertama tidak lebih besar dari angka kedua.")
