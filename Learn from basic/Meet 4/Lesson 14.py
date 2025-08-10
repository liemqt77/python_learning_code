import tkinter as tk

# Membuat instance dari Tk (jendela utama aplikasi)
root = tk.Tk()
root.title("Pengenalan Tkinter")  # Judul jendela
root.geometry("400x300")  # Ukuran jendela

# Menjalankan aplikasi
root.mainloop()

import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("Menambahkan Label")
root.geometry("400x300")

# Membuat label
label = tk.Label(root, text="Selamat datang di Tkinter!", font=("Arial", 14))
label.pack(pady=50)  # Menampilkan label dan memberi jarak atas-bawah

# Menjalankan aplikasi
root.mainloop()
"""

import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("Menambahkan Label")
root.geometry("400x300")

# Membuat label
label = tk.Label(root, text="Selamat datang di Tkinter!", font=("Arial", 14))
label.pack(pady=50)  # Menampilkan label dan memberi jarak atas-bawah

# Menjalankan aplikasi
root.mainloop()



"""

"""

import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("Menambahkan Entry")
root.geometry("400x300")

# Membuat label instruksi
label = tk.Label(root, text="Masukkan nama Anda:", font=("Arial", 12))
label.pack(pady=10)

# Membuat entry (kolom input)
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()


"""

"""

import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("Menambahkan Entry")
root.geometry("400x300")

# Membuat label instruksi
label = tk.Label(root, text="Masukkan nama Anda:", font=("Arial", 12))
label.pack(pady=10)

# Membuat entry (kolom input)
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()


"""


"""

import tkinter as tk

# Fungsi untuk menangani tombol klik
def greet():
    name = entry.get()  # Mengambil teks dari kolom input (Entry)
    label_result.config(text="Halo, " + name + "!")

# Membuat jendela utama
root = tk.Tk()
root.title("Menambahkan Tombol")
root.geometry("400x300")

# Membuat label instruksi
label = tk.Label(root, text="Masukkan nama Anda:", font=("Arial", 12))
label.pack(pady=10)

# Membuat entry untuk input nama
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

# Membuat tombol
button = tk.Button(root, text="Greet", font=("Arial", 12), command=greet)
button.pack(pady=10)

# Label untuk menampilkan hasil
label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()


"""


"""

import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("Menata dengan Grid")
root.geometry("400x300")

# Membuat label
label = tk.Label(root, text="Masukkan nama Anda:", font=("Arial", 12))
label.grid(row=0, column=0, padx=10, pady=10)

# Membuat entry untuk input nama
entry = tk.Entry(root, font=("Arial", 12))
entry.grid(row=0, column=1, padx=10, pady=10)

# Membuat tombol
button = tk.Button(root, text="Greet", font=("Arial", 12))
button.grid(row=1, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()


"""


"""

import tkinter as tk

# Fungsi untuk menangani klik menu
def new_file():
    print("New File Selected")

# Membuat jendela utama
root = tk.Tk()
root.title("Menambahkan Menu")
root.geometry("400x300")

# Membuat menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Membuat menu "File"
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Menjalankan aplikasi
root.mainloop()


"""