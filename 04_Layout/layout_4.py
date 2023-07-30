import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        # create horizontal layout for layout 1, vertical layout for layout 2,3 
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        # add 3 widgets color to layout 2
        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("yellow"))
        layout2.addWidget(Color("purple"))
        # add layout 2 to layout 1
        layout1.addLayout(layout2)
        # add green widget to layout 1
        layout1.addWidget(Color("green"))
        # add red and purple widget to layout 3
        layout3.addWidget(Color("red"))
        layout3.addWidget(Color("purple"))
        # add layout 3 to layout 1
        layout1.addLayout(layout3)
        # set margin to content
        layout1.setContentsMargins(10,10,10,10)
        # spacing between widget/layout
        layout1.setSpacing(5)
        # create dummy widget and add to layout 1
        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
