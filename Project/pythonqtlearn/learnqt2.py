import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Kalkulator Sederhana')
        self.setGeometry(100, 100, 250, 300)

        # Layout dan input
        self.layout = QVBoxLayout()

        self.result_display = QLineEdit(self)
        self.layout.addWidget(self.result_display)

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]

        for row in buttons:
            button_row = []
            for text in row:
                button = QPushButton(text, self)
                button.clicked.connect(self.on_button_click)
                button_row.append(button)
            for button in button_row:
                self.layout.addWidget(button)

        self.setLayout(self.layout)

    def on_button_click(self):
        sender = self.sender()
        button_text = sender.text()

        if button_text == '=':
            try:
                result = str(eval(self.result_display.text()))
                self.result_display.setText(result)
            except Exception:
                self.result_display.setText("Error")
        elif button_text == 'C':
            self.result_display.clear()
        else:
            self.result_display.setText(self.result_display.text() + button_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
