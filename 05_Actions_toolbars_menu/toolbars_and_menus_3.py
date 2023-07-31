import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        # create label
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)
        # add toolbar
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)
        # add action 
        button_action = QAction("Your button", self)
        # set action status tip
        button_action.setStatusTip("This is your button")
        # when action is triggered, will connect to the function named onMyToolBarButtonClick
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        # add the action to toolbar
        toolbar.addAction(button_action)
        # add status bar and passing the result by set status bar
        # status bar show the status tip for the action
        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
