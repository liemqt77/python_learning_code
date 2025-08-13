import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QTableWidget, QTableWidgetItem

class BudgetApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Aplikasi Pengelolaan Keuangan')
        self.setGeometry(100, 100, 500, 300)

        self.layout = QVBoxLayout()

        self.balance_label = QLabel('Saldo: 0', self)
        self.layout.addWidget(self.balance_label)

        # Input untuk transaksi
        self.amount_input = QLineEdit(self)
        self.amount_input.setPlaceholderText('Masukkan jumlah transaksi')
        self.layout.addWidget(self.amount_input)

        self.type_input = QLineEdit(self)
        self.type_input.setPlaceholderText('Masukkan jenis transaksi (Pemasukan/Pengeluaran)')
        self.layout.addWidget(self.type_input)

        # Tombol untuk menambah transaksi
        self.add_button = QPushButton('Tambah Transaksi', self)
        self.add_button.clicked.connect(self.add_transaction)
        self.layout.addWidget(self.add_button)

        # Tabel untuk menampilkan transaksi
        self.transaction_table = QTableWidget(self)
        self.transaction_table.setColumnCount(3)
        self.transaction_table.setHorizontalHeaderLabels(['Jumlah', 'Jenis', 'Total'])
        self.layout.addWidget(self.transaction_table)

        self.setLayout(self.layout)

        self.balance = 0

    def add_transaction(self):
        amount = self.amount_input.text()
        transaction_type = self.type_input.text()

        if amount and transaction_type:
            try:
                amount = float(amount)
                if transaction_type.lower() == 'pemasukan':
                    self.balance += amount
                elif transaction_type.lower() == 'pengeluaran':
                    self.balance -= amount

                self.balance_label.setText(f'Saldo: {self.balance}')
                row_position = self.transaction_table.rowCount()
                self.transaction_table.insertRow(row_position)

                self.transaction_table.setItem(row_position, 0, QTableWidgetItem(str(amount)))
                self.transaction_table.setItem(row_position, 1, QTableWidgetItem(transaction_type))
                self.transaction_table.setItem(row_position, 2, QTableWidgetItem(str(self.balance)))

                self.amount_input.clear()
                self.type_input.clear()

            except ValueError:
                pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BudgetApp()
    window.show()
    sys.exit(app.exec_())
