import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        # create a vertical box layout
        layout = QVBoxLayout()
        # add a widget with red color to layout
        layout.addWidget(Color("red"))

        # create a dummy widget
        widget = QWidget()
        # set layout for widget as above (layout with color red)
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
