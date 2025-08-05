from flask import Flask, render_template

# Membuat objek Flask
app = Flask(__name__)

# Definisikan route untuk halaman utama
@app.route('/')
def home():
    return render_template('index.html')

# Menjalankan server
if __name__ == '__main__':
    app.run(debug=True)
