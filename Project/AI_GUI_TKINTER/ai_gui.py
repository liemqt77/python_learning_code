import google.generativeai as genai

def start_chatbot(user_input, api_key, model_name):
    try:
        # Menyiapkan API Key untuk Gemini
        genai.configure(api_key=api_key)

        # Mengonfigurasi model yang dipilih
        model = genai.GenerativeModel(model_name)
        chat = model.start_chat()

        # Mengirim pesan pengguna dan mendapatkan respons
        response = chat.send_message(user_input)

        # Menampilkan teks respons dari chatbot
        print(f"Chatbot Response: {response.text}")

        return response.text

    except Exception as e:
        print(f"❌ Error saat memulai chat dengan Gemini: {e}")
        return None
