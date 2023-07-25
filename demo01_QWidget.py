import sys
from PyQt6.QtWidgets import QApplication, QWidget
#The main modules for Qt are QtWidgets, QtGui and QtCore.

app = QApplication(sys.argv)
# If you know you won’t be using command line arguments to control Qt 
# you can pass in an empty list instead, e.g.
# app = QApplication([])

# Next we create an instance of a QWidget using the variable name window.
window = QWidget()
window.show()
app.exec()

## EVENT LOOP - QApplication object to function that holds the event loop
# the core loop which governs all user interaction with the UI
# ONE QApplication is required
# Only ONE Evnet loop at any time
# your application sits waiting in the event loop until an action is taken

