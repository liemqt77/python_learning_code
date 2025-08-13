import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import QTimer


class SleepTimerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Aplikasi Pengingat Waktu Tidur')
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel('Masukkan waktu tidur (detik):', self)
        self.layout.addWidget(self.label)

        self.time_input = QLineEdit(self)
        self.layout.addWidget(self.time_input)

        self.start_button = QPushButton('Mulai Timer', self)
        self.start_button.clicked.connect(self.start_timer)
        self.layout.addWidget(self.start_button)

        self.countdown_label = QLabel('Waktu tersisa: 0 detik', self)
        self.layout.addWidget(self.countdown_label)

        self.setLayout(self.layout)

    def start_timer(self):
        try:
            self.time_left = int(self.time_input.text())
            self.countdown_label.setText(f'Waktu tersisa: {self.time_left} detik')

            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_countdown)
            self.timer.start(1000)  # update setiap detik
        except ValueError:
            self.label.setText('Masukkan angka yang valid!')

    def update_countdown(self):
        self.time_left -= 1
        self.countdown_label.setText(f'Waktu tersisa: {self.time_left} detik')

        if self.time_left <= 0:
            self.timer.stop()
            self.countdown_label.setText('Waktu Tidur Tercapai!')
            self.show_reminder()

    def show_reminder(self):
        self.label.setText('Pengingat: Waktunya Tidur!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SleepTimerApp()
    window.show()
    sys.exit(app.exec_())
