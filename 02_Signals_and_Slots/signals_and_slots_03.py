from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from random import choice

# List of random window title
window_titles = [
  "My App",
  "My App",
  "Still My App",
  "Still My App",
  "What on earth",
  "What on earth",
  "This is surprising",
  "This is surprising",
  "Something went wrong",
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.n_times_clicked = 0
        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")
        # when button clicked, it connected to the "the_button_was_clicked" method
        self.button.clicked.connect(self.the_button_was_clicked)
        # when window title is changed, it connect to the "the_window_title_changed" method
        self.windowTitleChanged.connect(
        self.the_window_title_changed
    ) 
        # Set the central widget of the Window.
        self.setCentralWidget(self.button)
    
    # method is hooked when button was click
    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)
        
    # method is hooked when the window title is changed    
    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title) 
        if window_title == "Something went wrong":
            self.button.setDisabled(True)
            
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()