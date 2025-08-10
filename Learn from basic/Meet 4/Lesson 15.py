#pip install pillow

import tkinter as tk
from PIL import Image, ImageTk

# Membuat jendela utama
root = tk.Tk()
root.title("Menambahkan Gambar di Tkinter")
root.geometry("500x400")

# Membuka gambar menggunakan PIL (Pillow)
image = Image.open("imagetester\\testerimg.png")  # Ganti dengan path gambar Anda
image = image.resize((300, 200))  # Resize gambar agar pas di jendela

# Mengonversi gambar ke format yang bisa diterima oleh Tkinter
photo = ImageTk.PhotoImage(image)

# Membuat label untuk menampilkan gambar
label_image = tk.Label(root, image=photo)
label_image.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
