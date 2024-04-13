import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QMainWindow, QHeaderView, QAbstractItemView
from PyQt5.uic import loadUi
import sqlite3

class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('main.ui', self)
        self.setWindowTitle('Информация о кофе из базы данных')
        self.showDataButton.clicked.connect(self.show_all_data)
        self.closeButton.clicked.connect(self.close_app)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def close_app(self):
        self.close()
    def load_data(self):
        connection = sqlite3.connect('coffee.sqlite')
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM coffee')
        data = cursor.fetchall()

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(7)
        column_headers = ['ID', 'Sort Name', 'Roast Degree', 'Ground or Whole', 'Taste Description', 'Price', 'Package Volume']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        column_widths = [30, 170, 110, 130, 180, 50, 130]
        for col_num, width in enumerate(column_widths):
            self.tableWidget.setColumnWidth(col_num, width)

        for row_num, row_data in enumerate(data):
            for col_num, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tableWidget.setItem(row_num, col_num, item)

        connection.close()

    def show_all_data(self):
        self.load_data()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec_())
