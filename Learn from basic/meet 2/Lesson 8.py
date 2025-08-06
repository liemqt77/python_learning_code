# Fungsi untuk menghitung BMI
def hitung_bmi(berat_badan, tinggi_badan):
    # Menghitung BMI
    bmi = berat_badan / (tinggi_badan ** 2)

    # Menentukan kategori BMI
    if bmi < 18.5:
        kategori = "Kekurangan berat badan"
    elif 18.5 <= bmi < 24.9:
        kategori = "Berat badan normal"
    elif 25 <= bmi < 29.9:
        kategori = "Kelebihan berat badan"
    else:
        kategori = "Obesitas"

    return bmi, kategori


# Input data dari pengguna
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan menggunakan desimal contoh 1.6 untuk 160 cm (meter): "))

# Hitung BMI dan kategori
bmi, kategori = hitung_bmi(berat, tinggi)

# Tampilkan hasil
print(f"\nBMI Anda adalah: {bmi:.2f}")
print(f"Kategori: {kategori}")
