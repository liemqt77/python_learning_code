import turtle

# Setup layar turtle
screen = turtle.Screen()
screen.bgcolor("black")  # Latar belakang hitam agar warna lingkaran lebih menonjol
screen.title("Lingkaran Penuh dengan Warna")

# Membuat turtle
pen = turtle.Turtle()
pen.speed(0)  # Menetapkan kecepatan maksimal
pen.width(2)  # Menetapkan ketebalan garis
pen.hideturtle()  # Menyembunyikan pen setelah menggambar

# Daftar warna yang ingin digunakan
colors = ["red", "yellow", "green", "blue", "purple", "orange", "pink", "cyan"]

# Ukuran lingkaran dan jarak antar lingkaran
radius = 30  # Radius lingkaran
spacing = 10  # Jarak antar lingkaran

# Fungsi untuk menggambar lingkaran dan mengisi layar
def draw_circles():
    pen.penup()
    # Menghitung berapa banyak lingkaran yang bisa digambar pada layar
    for x in range(-300, 300, radius * 2 + spacing):
        for y in range(-300, 300, radius * 2 + spacing):
            pen.goto(x, y)
            pen.pendown()
            pen.color(colors[(x + y) % len(colors)])  # Warna berganti setiap lingkaran
            pen.circle(radius)
            pen.penup()

    # Menunggu 3 detik setelah menggambar dan kemudian membersihkan layar
    screen.ontimer(clear_screen, 3000)  # Menunggu 3 detik

# Fungsi untuk menghapus gambar dan mengulang proses menggambar
def clear_screen():
    pen.clear()  # Menghapus semua gambar yang ada di layar
    # Memanggil lagi fungsi draw_circles setelah 3 detik
    screen.ontimer(draw_circles, 3000)  # Menunggu 3 detik sebelum menggambar lagi

# Mulai animasi
draw_circles()

# Menjaga layar tetap terbuka
turtle.done()
