from PyQt5.QtWidgets import *
import user_data


class SetHomeDialog(QDialog):
    def __init__(self, home_address):
        super(QDialog, self).__init__()

        self.setMaximumWidth(300)
        self.setWindowTitle("Set your home address")

        prompt = QLabel("Enter your state, then city: ")
        response = QLineEdit()

        address = QFormLayout()
        address.addRow(prompt, response)

        ok_btn = QDialogButtonBox.Save
        cancel_btn = QDialogButtonBox.Close

        btn_box = QDialogButtonBox()
        btn_box.addButton(ok_btn)
        btn_box.addButton(cancel_btn)

        btn_box.accepted.connect(lambda: user_data.add_home_address(response.text(), home_address))
        btn_box.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addLayout(address)
        layout.addWidget(btn_box)

        self.setLayout(layout)
        self.exec()
