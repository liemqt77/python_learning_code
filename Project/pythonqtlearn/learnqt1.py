from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
import sys
class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Aplikasi dengan Tombol')
        self.setGeometry(100, 100, 280, 120)

        self.label = QLabel('Tekan tombol untuk mengubah teks', self)

        # Tombol
        button = QPushButton('Klik Saya', self)
        button.clicked.connect(self.change_text)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(button)

        self.setLayout(layout)

    def change_text(self):
        self.label.setText('Tombol telah ditekan!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
