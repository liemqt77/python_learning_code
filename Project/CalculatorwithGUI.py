import tkinter as tk

# Fungsi untuk mengupdate teks pada layar kalkulator
def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Fungsi untuk menghitung hasil ekspresi yang dimasukkan
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Fungsi untuk menghapus teks pada layar
def clear():
    entry.delete(0, tk.END)

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Sederhana")

# Membuat layar input (Entry widget)
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Membuat tombol-tombol kalkulator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Menambahkan tombol ke GUI
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda value=text: click_button(value)).grid(row=row, column=col, padx=5, pady=5)

# Tombol Clear
tk.Button(root, text="C", width=5, height=2, font=("Arial", 18), command=clear).grid(row=5, column=0, padx=5, pady=5)

# Menjalankan aplikasi
root.mainloop()
