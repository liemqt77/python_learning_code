import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog, QHBoxLayout, QLabel
from PyQt5.QtCore import QFile, QTextStream


class NoteApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Aplikasi Catatan')
        self.setGeometry(100, 100, 600, 400)

        # Layout utama
        self.layout = QVBoxLayout()

        # Menambahkan teks edit untuk menulis catatan
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText('Tulis catatanmu di sini...')
        self.layout.addWidget(self.text_edit)

        # Layout tombol
        button_layout = QHBoxLayout()

        self.save_button = QPushButton('Simpan Catatan', self)
        self.save_button.clicked.connect(self.save_note)
        button_layout.addWidget(self.save_button)

        self.load_button = QPushButton('Buka Catatan', self)
        self.load_button.clicked.connect(self.load_note)
        button_layout.addWidget(self.load_button)

        # Tambahkan label untuk feedback kepada user
        self.feedback_label = QLabel('', self)
        button_layout.addWidget(self.feedback_label)

        self.layout.addLayout(button_layout)

        # Set Layout
        self.setLayout(self.layout)

    def save_note(self):
        # Menyimpan catatan ke file
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Simpan Catatan", "", "Text Files (*.txt);;All Files (*)", options=options)

        if file_name:
            with open(file_name, 'w') as file:
                text = self.text_edit.toPlainText()
                file.write(text)
            self.feedback_label.setText(f'Catatan disimpan di {file_name}')
            self.text_edit.clear()

    def load_note(self):
        # Memuat catatan dari file
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Buka Catatan", "", "Text Files (*.txt);;All Files (*)", options=options)

        if file_name:
            with open(file_name, 'r') as file:
                text = file.read()
                self.text_edit.setText(text)
            self.feedback_label.setText(f'Catatan dibuka dari {file_name}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NoteApp()
    window.show()
    sys.exit(app.exec_())
