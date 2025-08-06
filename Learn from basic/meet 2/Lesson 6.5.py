# Kasus 1: Menggunakan operator 'and'
umur = 25
tinggi = 1.75

# Mengecek apakah umur lebih dari 18 dan tinggi lebih dari 1.6
if umur > 18 and tinggi > 1.6:
    print("Kamu dewasa dan cukup tinggi!")
else:
    print("Kamu belum memenuhi kriteria.")

# Kasus 2: Menggunakan operator 'or'
nilai_ujian = 75
kehadiran = 80

# Mengecek apakah nilai ujian lebih dari 70 atau kehadiran lebih dari 85
if nilai_ujian > 70 or kehadiran > 85:
    print("Kamu memenuhi kriteria.")
else:
    print("Kamu tidak memenuhi kriteria.")

# Kasus 3: Menggunakan operator 'not'
is_hujan = False

# Mengecek apakah bukan hujan
if not is_hujan:
    print("Cuaca cerah, ayo keluar!")
else:
    print("Bawa payung, hujan!")

# Kasus 1.1: Menggunakan 'and' operator
umur = int(input("Masukkan umur Anda: "))  # Mengambil input umur dari pengguna
tinggi = float(input("Masukkan tinggi badan Anda (dalam meter): "))  # Mengambil input tinggi badan

# Mengecek apakah umur lebih dari 18 dan tinggi lebih dari 1.6
if umur > 18 and tinggi > 1.6:
    print("Kamu dewasa dan cukup tinggi!")
else:
    print("Kamu tidak memenuhi kriteria.")

# Kasus 2.1: Menggunakan 'or' operator
nilai_ujian = float(input("Masukkan nilai ujian Anda: "))  # Mengambil input nilai ujian
kehadiran = float(input("Masukkan persentase kehadiran Anda: "))  # Mengambil input persentase kehadiran

# Mengecek apakah nilai ujian lebih dari 70 atau kehadiran lebih dari 80
if nilai_ujian > 70 or kehadiran > 80:
    print("Kamu memenuhi kriteria.")
else:
    print("Kamu tidak memenuhi kriteria.")

# Kasus 3.1: Menggunakan 'not' operator
is_hujan = input("Apakah sedang hujan? (yes/no): ").lower()  # Input apakah sedang hujan

# Membalikkan nilai kondisi menggunakan 'not'
if not is_hujan == "yes":
    print("Cuaca cerah, ayo keluar!")
else:
    print("Bawa payung, hujan!")



