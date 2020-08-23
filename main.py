from gui import *
import user_data


if __name__ == "__main__":
    check_reminders()
    check_new_protest()
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())