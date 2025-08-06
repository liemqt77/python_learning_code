import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menambah task baru
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)  # Tambahkan task ke listbox
        task_entry.delete(0, tk.END)  # Bersihkan entry
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

# Fungsi untuk menghapus task yang dipilih
def delete_task():
    try:
        task_index = task_listbox.curselection()  # Dapatkan task yang dipilih
        task_listbox.delete(task_index)  # Hapus task yang dipilih
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Fungsi untuk menandai task sebagai selesai
def mark_done():
    try:
        task_index = task_listbox.curselection()  # Dapatkan task yang dipilih
        task = task_listbox.get(task_index)  # Ambil task yang dipilih
        task_listbox.delete(task_index)  # Hapus task lama
        task_listbox.insert(task_index, f"{task} - Done")  # Masukkan task dengan label "Done"
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

# Setup window utama
root = tk.Tk()
root.title("To-Do List")

# Entry untuk input task baru
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Tombol untuk menambah task
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

# Listbox untuk menampilkan task
task_listbox = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

# Tombol untuk menghapus task
delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

# Tombol untuk menandai task selesai
mark_done_button = tk.Button(root, text="Mark as Done", width=20, command=mark_done)
mark_done_button.pack(pady=5)

# Mulai aplikasi
root.mainloop()
