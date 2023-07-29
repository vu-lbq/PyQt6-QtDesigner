import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        # create label named widget
        widget = QLabel("Hello")
        # set variable name font for the font setup
        font = widget.font()
        # set font to size 30 
        font.setPointSize(30)
        # assign font setting to label
        widget.setFont(font)
        # set alignment for the label
        # alignmentflag - set label to be center of vertical and horizontal
        widget.setAlignment(
        Qt.AlignmentFlag.AlignHCenter
        | Qt.AlignmentFlag.AlignVCenter
        ) 
        self.setCentralWidget(widget)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
