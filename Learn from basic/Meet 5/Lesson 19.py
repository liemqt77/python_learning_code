import tkinter as tk

# Fungsi untuk menangani klik tombol
def greet():
    label.config(text="Halo, Selamat datang!")

# Membuat jendela utama
root = tk.Tk()
root.title("Widget Button")
root.geometry("400x300")

# Membuat tombol
button = tk.Button(root, text="Klik Saya", font=("Arial", 14), command=greet)
button.pack(pady=20)

# Label untuk menampilkan pesan
label = tk.Label(root, text="", font=("Arial", 14))
label.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
