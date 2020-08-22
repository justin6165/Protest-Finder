from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


class NoticeDialog(QDialog):
    def __init__(self, message, is_error):
        super(QDialog, self).__init__()

        self.setMaximumWidth(300)
        self.message = message
        self.is_error = is_error

        if self.is_error:
            self.setWindowTitle("Error")
        else:
            self.setWindowTitle("Success")

        notice = QLabel(self.message)
        notice.setFont(QFont("Arial", 12))

        ok_btn = QDialogButtonBox.Ok

        btn_box = QDialogButtonBox()
        btn_box.addButton(ok_btn)
        btn_box.accepted.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(notice)
        layout.addWidget(btn_box)

        self.setLayout(layout)
        self.exec()

