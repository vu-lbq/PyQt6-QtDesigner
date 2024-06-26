import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QCheckBox, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        # create a checkbox called widget
        widget = QCheckBox("This is a checkbox")
        
        # add checkState properties to checkbox 
        # below is two states - check or not check - true or false - 0 or 2
        widget.setCheckState(Qt.CheckState.Checked)
        
        # For tristate: widget.setCheckState(Qt.PartiallyChecked)
        # Or: widget.setTristate(True)
        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)
        
    # a slot method to show the state of checkbox
    def show_state(self, s):
        print(Qt.CheckState(s) == Qt.CheckState.Checked)
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
