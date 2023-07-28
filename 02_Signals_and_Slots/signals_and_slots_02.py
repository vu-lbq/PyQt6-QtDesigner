from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!") 
        self.button.clicked.connect(self.the_button_was_clicked)
        # Set the central widget of the Window.
        self.setCentralWidget(self.button)
    def the_button_was_clicked(self):
        # Set/change text on the button
        self.button.setText("You already clicked me.")
        # change state button to false - you can not click on it anymore. 
        self.button.setEnabled(False) 
        # Also change the window title.
        self.setWindowTitle("My Oneshot App")
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
