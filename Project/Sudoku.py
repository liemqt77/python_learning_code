import tkinter as tk
from tkinter import messagebox


class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game")
        self.grid = [[0] * 9 for _ in range(9)]
        self.entries = [[None] * 9 for _ in range(9)]
        self.create_widgets()
        self.generate_sudoku()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.grid(row=0, column=0, padx=10, pady=10)

        # Membuat grid Sudoku menggunakan Entry dengan garis pembatas tebal
        for i in range(9):
            for j in range(9):
                # Tambahkan border pada setiap blok 3x3
                if (i % 3 == 0) and (j % 3 == 0):
                    frame_entry = tk.Frame(frame, bd=2, relief="solid")
                else:
                    frame_entry = tk.Frame(frame, bd=1, relief="solid")

                frame_entry.grid(row=i, column=j, padx=(2 if j % 3 == 0 else 0, 2), pady=(2 if i % 3 == 0 else 0, 2))

                entry = tk.Entry(frame_entry, width=2, font=("Arial", 18), justify="center")
                entry.pack()
                self.entries[i][j] = entry

        # Tombol untuk validasi dan reset
        validate_button = tk.Button(self.root, text="Check", command=self.validate_sudoku)
        validate_button.grid(row=1, column=0, pady=5)

        reset_button = tk.Button(self.root, text="Reset", command=self.reset_sudoku)
        reset_button.grid(row=2, column=0, pady=5)

    def generate_sudoku(self):
        # Membuat puzzle Sudoku dasar (seed)
        self.grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                     [6, 0, 0, 1, 9, 5, 0, 0, 0],
                     [0, 9, 8, 0, 0, 0, 0, 6, 0],
                     [8, 0, 0, 0, 6, 0, 0, 0, 3],
                     [4, 0, 0, 8, 0, 3, 0, 0, 1],
                     [7, 0, 0, 0, 2, 0, 0, 0, 6],
                     [0, 6, 0, 0, 0, 0, 2, 8, 0],
                     [0, 0, 0, 4, 1, 9, 0, 0, 5],
                     [0, 0, 0, 0, 8, 0, 0, 7, 9]]

        # Menampilkan grid di GUI
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != 0:
                    self.entries[i][j].insert(0, str(self.grid[i][j]))
                    self.entries[i][j].config(state="disabled")

    def reset_sudoku(self):
        # Reset grid dan entry
        for i in range(9):
            for j in range(9):
                self.entries[i][j].config(state="normal")
                self.entries[i][j].delete(0, tk.END)
                if self.grid[i][j] != 0:
                    self.entries[i][j].insert(0, str(self.grid[i][j]))
                    self.entries[i][j].config(state="disabled")

    def validate_sudoku(self):
        # Validasi apakah Sudoku yang diisi benar
        try:
            user_grid = [[int(self.entries[i][j].get()) if self.entries[i][j].get() else 0 for j in range(9)] for i in
                         range(9)]
            if self.is_valid_sudoku(user_grid):
                messagebox.showinfo("Sudoku", "Congratulations! Sudoku is correct.")
            else:
                messagebox.showwarning("Sudoku", "Sudoku is incorrect. Try again.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    def is_valid_sudoku(self, board):
        # Fungsi untuk memvalidasi Sudoku
        for i in range(9):
            row = [num for num in board[i] if num != 0]
            if len(row) != len(set(row)):
                return False
        for j in range(9):
            col = [board[i][j] for i in range(9) if board[i][j] != 0]
            if len(col) != len(set(col)):
                return False
        for x in range(3):
            for y in range(3):
                block = [board[i][j] for i in range(x * 3, (x + 1) * 3) for j in range(y * 3, (y + 1) * 3) if
                         board[i][j] != 0]
                if len(block) != len(set(block)):
                    return False
        return True


# Inisialisasi aplikasi
root = tk.Tk()
app = SudokuGUI(root)
root.mainloop()
