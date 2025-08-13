import os
import tempfile
from gtts import gTTS
import pygame

def text_to_speech(text, language='id'):
    try:
        # Gunakan direktori sementara yang dikelola sistem
        temp_dir = tempfile.gettempdir()  # Sistem akan memilih direktori yang tepat
        audio_file = os.path.join(temp_dir, 'response.mp3')

        # Menggunakan gTTS untuk mengubah teks menjadi suara
        tts = gTTS(text=text, lang=language)  # Bahasa sesuai pilihan
        tts.save(audio_file)  # Menyimpan suara dalam file temporer

        # Memutar file suara menggunakan pygame
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

        # Menunggu hingga suara selesai diputar
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        # Tidak menghapus file setelah diputar, hanya menunggu hingga pemutaran selesai
        print("Suara selesai diputar, file tetap ada.")

        pygame.mixer.quit()

    except Exception as e:
        print(f"❌ Error saat mengonversi teks menjadi suara: {e}")
