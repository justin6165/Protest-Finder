from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle("Protest Finder")

        self.top_layout = QHBoxLayout()  # Top level layout of the entire application
        self.main_layout()  # Create main layout of app

        self.search_layout()  # Layout for searching
        #self.search_results_layout()

    def main_layout(self):
        widget = QWidget()  # Central widget of the app
        widget.setLayout(self.top_layout)

        self.setCentralWidget(widget)

    def search_layout(self):
        search_layout = QFormLayout()

        city = QLineEdit()  # Field for user to enter in city
        search_layout.addRow(QLabel("City:"), city)

        state = QLineEdit()  # Field for user to enter in state
        search_layout.addRow(QLabel("State:"), state)

        search_btn = QPushButton("Search")  # Button to execute search
        search_layout.addWidget(search_btn)

        self.top_layout.addLayout(search_layout)

   # def search_results_layout(self):


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())






































