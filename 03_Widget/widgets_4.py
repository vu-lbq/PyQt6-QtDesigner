import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        # create a combobox (dropdown list) called widget
        widget = QComboBox()
        # add three value in order for selecting
        widget.addItems(["One", "Two", "Three"])
        # hook to method index_changed() when index is changed in combobox
        # note that index start from 0
        widget.currentIndexChanged.connect(self.index_changed)
        # hook to method text_changed()
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):  # i is an int
        print(i)

    def text_changed(self, s):  # s is a str
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
