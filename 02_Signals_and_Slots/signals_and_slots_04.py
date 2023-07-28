from PyQt6.QtWidgets import (
  QApplication,
  QMainWindow,
  QLabel,
  QLineEdit,
  QVBoxLayout,
  QWidget,
)

import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        # create label named label
        self.label = QLabel()
        # create line edit named input
        self.input = QLineEdit()
        # when line edit change text will hook the setText method to label
        self.input.textChanged.connect(self.label.setText)
        # create QVBox layout named layout 
        layout = QVBoxLayout()
        # add input-line edit and label-label to layout  
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        # create widget called container 
        container = QWidget()
        # add layout to container-widget
        container.setLayout(layout)
        # Set the central widget of the Window.
        self.setCentralWidget(container)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()