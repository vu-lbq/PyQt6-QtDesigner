import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
)

# Create sub dialog named custom dialog
class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        # set window title for sub dialog
        self.setWindowTitle("HELLO!")
        # create button for OK and cancel inside dialog
        buttons = (
            QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Cancel
        )
        # add button box to sub dialog
        self.buttonBox = QDialogButtonBox(buttons)
        # two events - accept and reject - connect to functions
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        # add label to dialog
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        # add button box
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        # add push button 
        button = QPushButton("Press me for a dialog!")
        # connect to function button_click
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    # tag::button_clicked[]

    def button_clicked(self, s):
        print("click", s)
        # create the CustomDialog 
        dlg = CustomDialog()
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

    # end::button_clicked[]


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
