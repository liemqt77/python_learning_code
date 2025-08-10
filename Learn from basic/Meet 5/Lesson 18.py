import tkinter as tk

# Fungsi untuk menangani gerakan mouse
def on_motion(event):
    label.config(text=f"Mouse bergerak ke ({event.x}, {event.y})")

# Membuat jendela utama
root = tk.Tk()
root.title("Event Handling: Gerakan Mouse")
root.geometry("400x300")

# Label untuk menampilkan koordinat mouse
label = tk.Label(root, text="Gerakkan mouse di sini!", font=("Arial", 14))
label.pack(pady=50)

# Mengikat event gerakan mouse ke jendela
root.bind("<Motion>", on_motion)  # <Motion> adalah event gerakan mouse

# Menjalankan aplikasi
root.mainloop()
