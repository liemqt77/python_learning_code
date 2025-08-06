# Kasus 1: Mengecek kelulusan berdasarkan nilai ujian
nilai_ujian = float(input("Masukkan nilai ujian Anda: "))  # Input nilai ujian

# Mengecek apakah nilai lebih dari atau sama dengan 60 (misalnya, standar kelulusan)
if nilai_ujian >= 60:
    print("Selamat, Anda LULUS!")
else:
    print("Maaf, Anda TIDAK LULUS. Coba lagi tahun depan.")

# Kasus 2: Memeriksa kriteria untuk mengikuti ujian akhir
nilai_ujian = float(input("Masukkan nilai ujian Anda: "))
kehadiran = float(input("Masukkan persentase kehadiran Anda: "))  # Kehadiran dalam persen

# Memeriksa apakah nilai dan kehadiran memenuhi kriteria
if nilai_ujian >= 70 and kehadiran >= 80:
    print("Anda memenuhi syarat untuk mengikuti ujian akhir.")
else:
    print("Maaf, Anda tidak memenuhi syarat untuk mengikuti ujian akhir.")
# Kasus 3: Menentukan jenis pelajaran berdasarkan hari
hari = input("Masukkan hari (Senin, Selasa, Rabu, Kamis, Jumat): ").lower()

# Menggunakan if-else untuk menentukan pelajaran pada hari tertentu
if hari == "senin":
    print("Hari ini adalah pelajaran Matematika.")
elif hari == "selasa":
    print("Hari ini adalah pelajaran Bahasa Inggris.")
elif hari == "rabu":
    print("Hari ini adalah pelajaran Fisika.")
elif hari == "kamis":
    print("Hari ini adalah pelajaran Kimia.")
elif hari == "jumat":
    print("Hari ini adalah pelajaran Olahraga.")
else:
    print("Hari yang Anda masukkan tidak valid.")
