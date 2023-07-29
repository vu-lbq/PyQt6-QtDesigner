import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLineEdit, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        # create a line edit named widget
        widget = QLineEdit()
        # set maximum length for the line edit
        widget.setMaxLength(10)
        # set the place holdẻ text
        widget.setPlaceholderText("Enter your text")
        
        # widget.setReadOnly(True) # uncomment this to make readonly
        
        # hooked return pressed with the function
        widget.returnPressed.connect(self.return_pressed)
        # hooked the selection changed with the function
        widget.selectionChanged.connect(self.selection_changed)
        # hooked the text change with the function
        widget.textChanged.connect(self.text_changed)
        # hooked the text edited with the function
        widget.textEdited.connect(self.text_edited)

        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("boom!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
