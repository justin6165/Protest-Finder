from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        widget = QWidget()  # Central widget of app
        top_layout = QHBoxLayout()  # Top level layout of entire app

        name = QLabel("this is where the protest name goes")
        location = QLabel("protest location")
        desc = QLabel("protest description / info")

        infBox = QHBoxLayout
        infBox.setLayout(name)
        infBox.addLayout(location)
        infBox.addLayout(desc)

        widget.setLayout(top_layout)
        self.setCentralWidget(widget)

        side = QHBoxLayout()
        bot = QVBoxLayout()
        space = QGridLayout()

        widget.addLayout(side)
        widget.addLayout(space)
        widget.addLayout(bot)


        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.show()
    sys.exit(app.exec())
