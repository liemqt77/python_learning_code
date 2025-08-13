import tkinter as tk
from tkinter import messagebox
from tts_gui import text_to_speech  # Mengimpor fungsi text_to_speech dari tts_gui.py
from ai_gui import start_chatbot  # Mengimpor fungsi start_chatbot dari ai_gui.py
import threading


class ChatbotTTSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot & Text-to-Speech Application")
        self.root.geometry("700x600")  # Ukuran jendela lebih besar

        # Frame untuk input API Key dan Model
        self.config_frame = tk.LabelFrame(self.root, text="Konfigurasi API Key dan Model", padx=10, pady=10,
                                          font=("Arial", 12))
        self.config_frame.pack(fill="both", expand="true", padx=10, pady=10)

        # Input API Key
        self.api_key_label = tk.Label(self.config_frame, text="Masukkan Google API Key Anda:", font=("Arial", 12))
        self.api_key_label.pack()
        self.api_key_entry = tk.Entry(self.config_frame, width=50, font=("Arial", 12))
        self.api_key_entry.pack(pady=5)

        # Pilih Model
        self.model_label = tk.Label(self.config_frame, text="Pilih model yang akan digunakan:", font=("Arial", 12))
        self.model_label.pack()

        self.model_var = tk.StringVar()
        self.model_var.set("gemma-3n-e2b-it")  # Default model
        self.model_menu = tk.OptionMenu(self.config_frame, self.model_var, "gemma-3n-e2b-it", "gemini-1", "gemini-2")
        self.model_menu.config(font=("Arial", 12))
        self.model_menu.pack(pady=5)

        # Pilih Bahasa untuk TTS
        self.language_label = tk.Label(self.config_frame, text="Pilih Bahasa untuk TTS:", font=("Arial", 12))
        self.language_label.pack()

        self.languages = {
            'id': 'Bahasa Indonesia',
            'en': 'English',
            'es': 'Español',
            'fr': 'Français',
            'de': 'Deutsch',
            'it': 'Italiano',
            'ja': '日本語',
            'ko': '한국어',
            'pt': 'Português',
        }

        self.language_var = tk.StringVar()
        self.language_var.set('id')  # Default language
        self.language_menu = tk.OptionMenu(self.config_frame, self.language_var, *self.languages.keys())
        self.language_menu.config(font=("Arial", 12))
        self.language_menu.pack(pady=5)

        # Tombol untuk mengonfigurasi API Key dan Model
        self.config_button = tk.Button(self.config_frame, text="Konfigurasi", command=self.configure_and_start_chat,
                                       font=("Arial", 12))
        self.config_button.pack(pady=10)

        # Frame untuk Chatbot
        self.chatbot_frame = tk.LabelFrame(self.root, text="Chatbot", padx=10, pady=10, font=("Arial", 12))
        self.chatbot_frame.pack(fill="both", expand="true", padx=10, pady=10)

        # Chatbot Section
        self.chatbot_label = tk.Label(self.chatbot_frame, text="Mulai Chat dengan Chatbot:", font=("Arial", 12))
        self.chatbot_label.pack()

        # Memperbesar ukuran widget Text dan font untuk percakapan
        self.chatbot_text = tk.Text(self.chatbot_frame, height=15, width=70, font=("Arial", 10), wrap=tk.WORD)
        self.chatbot_text.pack(pady=5)

        self.chatbot_input = tk.Entry(self.chatbot_frame, width=70, font=("Arial", 10))  # Ukuran lebih besar
        self.chatbot_input.pack(pady=5)

        self.chatbot_button = tk.Button(self.chatbot_frame, text="Kirim", command=self.start_chat, font=("Arial", 10))
        self.chatbot_button.pack(pady=5)

        self.api_key = None
        self.model_name = None

    def configure_and_start_chat(self):
        """Fungsi untuk mengonfigurasi API Key dan model, lalu memulai chat."""
        self.api_key = self.api_key_entry.get()
        self.model_name = self.model_var.get()

        if not self.api_key:
            messagebox.showerror("Error", "API Key tidak boleh kosong!")
            return

        # Menyembunyikan frame konfigurasi dan menampilkan frame chatbot
        self.config_frame.pack_forget()
        self.chatbot_frame.pack(fill="both", expand="true", padx=10, pady=10)

    def start_chat(self):
        """Fungsi untuk memulai chat dengan chatbot dan mengonversi respons menjadi suara secara paralel."""
        user_input = self.chatbot_input.get()
        if not user_input:
            messagebox.showwarning("Input Kosong", "Tolong masukkan pesan untuk dikirim ke chatbot.")
            return

        # Menampilkan pesan pengguna dengan bold di widget Text
        self.chatbot_text.insert(tk.END, f"You: {user_input}\n", "bold")
        self.chatbot_input.delete(0, tk.END)

        # Memulai proses chatbot dan TTS dalam thread terpisah
        chat_thread = threading.Thread(target=self.chat_and_tts, args=(user_input,))
        chat_thread.start()

    def chat_and_tts(self, user_input):
        """Fungsi untuk memulai chat dengan chatbot dan mengonversi respons menjadi suara."""
        # Memulai chatbot dan mendapatkan respons
        response = start_chatbot(user_input, self.api_key, self.model_name)

        if response:
            # Mengganti tanda '*' dengan bold untuk tampilan dan menghapus tag HTML untuk TTS
            display_response, tts_response = self.replace_asterisks_with_bold(response)

            # Menampilkan chat dalam Text widget
            self.chatbot_text.insert(tk.END, f"Chatbot: {display_response}\n")

            # Mengonversi respons chatbot menjadi suara
            language = self.language_var.get()  # Mendapatkan bahasa yang dipilih
            text_to_speech(tts_response, language)

    def replace_asterisks_with_bold(self, response):
        """Mengganti tanda '*' dengan tag bold dalam respons chatbot dan menghapus tag HTML untuk TTS."""
        # Menghapus tag </b> atau <b> dan mengganti tanda '*' dengan teks biasa
        response = response.replace("</b>", "").replace("<b>", "")

        # Menghapus tanda '*' dari teks
        response = response.replace("*", "")  # Hapus semua tanda '*'

        # Tidak menambahkan tag HTML dalam TTS, hanya tampilkan teks biasa
        result_display = response  # Hasil untuk ditampilkan di Text widget
        result_tts = response  # Hasil untuk TTS (tanpa tag HTML dan tanda *)

        return result_display, result_tts


# Membuat jendela utama aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotTTSApp(root)
    root.mainloop()


#API: AIzaSyAoYFuKcqfX7huiEcSkgU9uEqcFnm_5lRI