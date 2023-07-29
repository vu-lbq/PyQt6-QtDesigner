import sys

from PyQt6.QtWidgets import QApplication, QListWidget, QMainWindow, QAbstractItemView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        # add a listwidget (same as combobox but can show and select muptiple items)
        widget = QListWidget()
        # items are stored in a list
        widget.addItems(["One", "Two", "Three"])
        # set selectionmode to multiselection
        widget.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        # Hooked item changed to index_change function
        widget.currentItemChanged.connect(self.index_changed)
        # Hooked text changed to text_change function
        widget.currentTextChanged.connect(self.text_changed)
        self.setCentralWidget(widget)

    def index_changed(self, i):  # Not an index, i is a QListItem
        print(i.text())

    def text_changed(self, s):  # s is a str
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
