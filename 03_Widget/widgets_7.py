import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QSpinBox, QDoubleSpinBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        # create a spinbox named label
        # spin box is for integer - double spin box is for float
        widget = QSpinBox()
        # Or: widget = QDoubleSpinBox()

        #set minimum and maximum value of spin box
        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: we can set a range as below
        # widget.setRange(-10,3)

        # set prefix and suffix value
        widget.setPrefix("$")
        widget.setSuffix("c")
        # set step for spinbox
        widget.setSingleStep(2)  
        # Or e.g. 0.5 for QDoubleSpinBox
        
        # hook when value change to function value_changed()
        # the value_changed() event will send the numeric value (integer or float) and remove the prefix and suffix 
        widget.valueChanged.connect(self.value_changed)
        # hook when text change tp function text_changed()
        # the text_changed() event will send the string included prefix and suffix
        widget.textChanged.connect(self.value_changed_str)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)
        print("numeric")

    def value_changed_str(self, s):
        print(s)
        print("string")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
