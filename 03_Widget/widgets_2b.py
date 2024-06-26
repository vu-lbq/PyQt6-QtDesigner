# import os here to work with files, directory, folder...
# os.path common pathname manipulations
import os
import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow


basedir = os.path.dirname(__file__)
print("Current working folder:", os.getcwd())  # <1>
print("Paths are relative to:", basedir)  # <2>


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        # create a label called widget
        widget = QLabel("Hello")
        # setPixmap for the label using QPixmap
        widget.setPixmap(QPixmap(os.path.join(basedir, "otje.jpg")))
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
