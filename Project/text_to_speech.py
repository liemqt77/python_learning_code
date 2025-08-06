from gtts import gTTS
import pygame
import os
import time

print("🔊 Program Text-to-Speech Bahasa Indonesia")
print("Ketik 'keluar' untuk mengakhiri.\n")

while True:
    teks = input("📝 Masukkan teks: ")

    if teks.lower() in ['keluar', 'exit', 'quit']:
        print("👋 Program selesai.")
        break

    try:
        # Simpan suara ke file sementara
        tts = gTTS(text=teks, lang='id')
        tts.save("temp_id.mp3")

        # Inisialisasi dan putar
        pygame.mixer.init()
        pygame.mixer.music.load("temp_id.mp3")
        pygame.mixer.music.play()

        # Tunggu sampai suara selesai
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        # Matikan mixer untuk melepaskan file
        pygame.mixer.music.unload()
        pygame.mixer.quit()

        # Hapus file setelah diputar
        os.remove("temp_id.mp3")

    except Exception as e:
        print(f"⚠️ Terjadi kesalahan: {e}")
