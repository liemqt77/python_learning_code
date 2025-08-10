import tkinter as tk

# Fungsi untuk menangani klik tombol
def on_click(event):
    label.config(text="Tombol ditekan!")

# Membuat jendela utama
root = tk.Tk()
root.title("Event Handling: Klik Tombol")
root.geometry("400x300")

# Membuat tombol
button = tk.Button(root, text="Klik Saya")
button.pack(pady=20)

# Mengikat event klik mouse ke tombol
button.bind("<Button-1>", on_click)  # <Button-1> adalah event untuk klik kiri mouse

# Label untuk menampilkan pesan
label = tk.Label(root, text="", font=("Arial", 14))
label.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
