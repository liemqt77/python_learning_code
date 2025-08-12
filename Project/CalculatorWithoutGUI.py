# Kalkulator Sederhana Python Tanpa GUI

def tambah(x, y):
    return x + y


def kurang(x, y):
    return x - y


def kali(x, y):
    return x * y


def bagi(x, y):
    if y == 0:
        return "Tidak dapat membagi dengan nol"
    else:
        return x / y


print("Pilihan operasi:")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

# Meminta input dari pengguna
while True:
    try:
        pilihan = input("Pilih operasi (1/2/3/4) atau 'exit' untuk keluar: ").strip().lower()
        if pilihan == 'exit':
            print("Keluar dari kalkulator.")
            break

        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))

        if pilihan == '1' or pilihan == 'tambah':
            print(f"{num1} + {num2} = {tambah(num1, num2)}")
        elif pilihan == '2' or pilihan == 'kurang':
            print(f"{num1} - {num2} = {kurang(num1, num2)}")
        elif pilihan == '3' or pilihan == 'kali':
            print(f"{num1} * {num2} = {kali(num1, num2)}")
        elif pilihan == '4' or pilihan == 'bagi':
            print(f"{num1} / {num2} = {bagi(num1, num2)}")
        else:
            print("Pilihan tidak valid. Silakan pilih operasi yang benar.")
    except ValueError:
        print("Input tidak valid. Masukkan angka yang benar.")
