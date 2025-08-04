import subprocess

# Langkah 1: Membuat file README.md dan menulis konten
with open('README.md', 'w') as f:
    f.write("# python_learning_code")

# Langkah 2: Inisialisasi repository git
subprocess.run(["git", "init"])

# Langkah 3: Menambahkan file README.md ke staging area
subprocess.run(["git", "add", "README.md"])

# Langkah 4: Commit pertama
subprocess.run(['git', 'commit', '-m', 'first commit'])

# Langkah 5: Mengubah nama branch menjadi 'main'
subprocess.run(["git", "branch", "-M", "main"])

# Langkah 6: Menambahkan remote origin
subprocess.run([
    "git", "remote", "add", "origin",
    "https://github.com/liemqt77/python_learning_code.git"
])

# Langkah 7: Push perubahan ke GitHub
subprocess.run(["git", "push", "-u", "origin", "main"])

