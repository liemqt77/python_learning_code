import tkinter as tk

# Membuat instance dari Tk
root = tk.Tk()
root.title("Aplikasi Tkinter Sederhana")
root.geometry("400x300")  # Ukuran jendela aplikasi

# Fungsi untuk menangani event ketika tombol ditekan
def greet():
    label_result.config(text="Halo, " + entry_name.get() + "! Selamat datang di Tkinter!")

# Label untuk instruksi
label_instruction = tk.Label(root, text="Masukkan nama Anda:", font=("Arial", 12))
label_instruction.pack(pady=10)

# Entry (kolom input) untuk nama
entry_name = tk.Entry(root, font=("Arial", 12))
entry_name.pack(pady=10)

# Tombol untuk menjalankan fungsi greet()
button_greet = tk.Button(root, text="Greet", font=("Arial", 12), command=greet)
button_greet.pack(pady=10)

# Label untuk menampilkan hasil
label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
