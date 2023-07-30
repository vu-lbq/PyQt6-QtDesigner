import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QDial, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        # create Dial named wwidget
        widget = QDial()
        # set range for dianl from -10 to 100
        widget.setRange(-10, 100)
        # set single step for dial as 1
        widget.setSingleStep(1)

        # hood the events with functions 
        # send the integer value
        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)
        #print(type(i))

    def slider_position(self, p):
        print("position", p)
        #print(type(p))

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
