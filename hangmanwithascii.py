import random

# Daftar kata-kata yang bisa dipilih dalam permainan
word_list = ['python', 'java', 'hangman', 'computer', 'programming', 'developer', 'keyboard']

# Memilih kata secara acak
word = random.choice(word_list)

# Menyiapkan list untuk menyimpan status setiap huruf yang ditebak
guessed_word = ['_'] * len(word)

# Menentukan jumlah kesempatan
attempts_left = 6

# Menyimpan huruf yang telah ditebak
guessed_letters = []

# Gambar ASCII untuk setiap kesempatan yang tersisa
hangman_graphics = [
    '''
     ------
     |    |
          |
          |
          |
          |
          |
    ============
    ''', '''
     ------
     |    |
     O    |
          |
          |
          |
          |
    ============
    ''', '''
     ------
     |    |
     O    |
     |    |
          |
          |
          |
    ============
    ''', '''
     ------
     |    |
     O    |
    /|    |
          |
          |
          |
    ============
    ''', '''
     ------
     |    |
     O    |
    /|\\   |
          |
          |
          |
    ============
    ''', '''
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
          |
    ============
    ''', '''
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
          |
    ============
    '''
]


# Fungsi untuk menampilkan gambar hangman
def display_hangman(attempts_left):
    print(hangman_graphics[6 - attempts_left])


# Fungsi untuk menampilkan status kata yang telah ditebak
def display_word():
    print(" ".join(guessed_word))


# Menampilkan instruksi permainan
print("Selamat datang di permainan Hangman!")
print("Coba tebak kata yang saya pikirkan.")

# Loop utama permainan
while attempts_left > 0:
    # Menampilkan gambar hangman dan status kata yang telah ditebak
    display_hangman(attempts_left)
    display_word()

    # Meminta pemain untuk menebak huruf
    guess = input(f"\nTebakanmu (Kamu punya {attempts_left} kesempatan): ").lower()

    # Cek apakah tebakan sudah pernah dilakukan
    if guess in guessed_letters:
        print(f"Kamu sudah menebak '{guess}' sebelumnya. Coba lagi!")
        continue

    # Menambahkan tebakan ke daftar huruf yang telah ditebak
    guessed_letters.append(guess)

    # Cek apakah tebakan benar
    if guess in word:
        print(f"Bagus! Huruf '{guess}' ada di dalam kata.")
        # Update status kata
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print(f"Sayang sekali! Huruf '{guess}' tidak ada di dalam kata.")
        attempts_left -= 1

    # Cek apakah kata sudah sepenuhnya tertebak
    if '_' not in guessed_word:
        print("\nSelamat! Kamu berhasil menebak kata dengan benar!")
        break

# Jika kesempatan habis
if attempts_left == 0:
    print(f"\nGame Over! Kata yang benar adalah '{word}'.")
