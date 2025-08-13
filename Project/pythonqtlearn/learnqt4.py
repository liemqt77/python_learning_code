import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QHBoxLayout


class ChatApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Aplikasi Chat Sederhana')
        self.setGeometry(100, 100, 400, 300)

        # Layout utama
        self.layout = QVBoxLayout()

        # Text area untuk menampilkan pesan
        self.chat_display = QTextEdit(self)
        self.chat_display.setReadOnly(True)
        self.layout.addWidget(self.chat_display)

        # Input untuk mengetik pesan
        self.message_input = QLineEdit(self)
        self.layout.addWidget(self.message_input)

        # Tombol untuk mengirim pesan
        self.send_button = QPushButton('Kirim', self)
        self.send_button.clicked.connect(self.send_message)

        self.layout.addWidget(self.send_button)

        self.setLayout(self.layout)

    def send_message(self):
        message = self.message_input.text()
        if message:
            self.chat_display.append(f'Anda: {message}')
            self.message_input.clear()
            # Simulasi pesan masuk
            self.chat_display.append(f'System: Terima kasih, pesan Anda sudah diterima!')
            self.chat_display.ensureCursorVisible()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_window = ChatApp()
    chat_window.show()
    sys.exit(app.exec_())
