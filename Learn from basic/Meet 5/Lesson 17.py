import tkinter as tk

# Fungsi untuk menangani penekanan tombol keyboard
def on_keypress(event):
    label.config(text=f"Tombol '{event.char}' ditekan!")

# Membuat jendela utama
root = tk.Tk()
root.title("Event Handling: Keyboard")
root.geometry("400x300")

# Label untuk menampilkan pesan
label = tk.Label(root, text="Tekan tombol apapun", font=("Arial", 14))
label.pack(pady=50)

# Mengikat event penekanan tombol keyboard
root.bind("<Key>", on_keypress)  # Mengikat event untuk semua tombol keyboard

# Menjalankan aplikasi
root.mainloop()
