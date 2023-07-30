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
        # create Box Horizontal layout to layout 1, vertical layout to layout 2,3
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        # set margins to content
        layout1.setContentsMargins(5, 5, 5, 5)
        # set spacing for layout 1s
        layout1.setSpacing(10)
        # add color widgets to layout 2 
        layout2.addWidget(Color("blue"))
        layout2.addWidget(Color("green"))
        layout2.addWidget(Color("yellow"))
        layout2.addWidget(Color("orange"))
        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("pink"))
        layout2.addWidget(Color("purple"))
        # add layout 2 to layout 1
        layout1.addLayout(layout2)
        # add green widget to layout 1
        layout1.addWidget(Color("white"))
        # add red and purple widgets to layout 3
        layout3.addWidget(Color("black"))
        layout3.addWidget(Color("pink"))
        # add layout 3 to layout 1
        layout1.addLayout(layout3)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
