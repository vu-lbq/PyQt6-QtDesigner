import sys
# Import Qpixmap - handling image data
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        # create a label named widget with text "Hello"
        widget = QLabel("Hello")
        # set the image to the label
        widget.setPixmap(QPixmap("otje.jpg"))
        
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
