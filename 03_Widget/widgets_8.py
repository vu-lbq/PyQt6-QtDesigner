import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QSlider, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        #create a slider name widget - example of slider is volume control
        # slider only provide integer changed
        widget = QSlider()
        
        # set the orientiation of slider - Vertical or Horizontal
        # this orientiation must be set before range setting or it will be override [0..99]
        widget = QSlider(Qt.Orientation.Horizontal)
        
        #set minimum and maximum for widget
        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or we can set range
        # widget.setRange(-10,3)

        # set single step - value when click on increase or decrease
        widget.setSingleStep(1)
        

        # hooked when value change to function
        # send the integer value
        widget.valueChanged.connect(self.value_changed)
        # hooked when slider is moved
        # send also the integer value
        widget.sliderMoved.connect(self.slider_position)
        # hooked when slider is pressed
        widget.sliderPressed.connect(self.slider_pressed)
        # hooked when slider is released 
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print("value changed", i)

    def slider_position(self, p):
        print("position", p)
        print(type(p))

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
