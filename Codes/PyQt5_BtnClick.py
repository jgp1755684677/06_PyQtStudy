# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


# create a class.
class Example(QMainWindow):

    # initialization function.
    def __init__(self):
        # inherits the "QMainWindow" class.
        super().__init__()
        # call the "init_ui" function.
        self.init_ui()

    # interface function.
    def init_ui(self):
        # instantiate a "btn1" object.
        btn1 = QPushButton("button1", self)
        # define the position of "btn1".
        btn1.move(30, 50)
        # instantiate a "btn2" object.
        btn2 = QPushButton("button2", self)
        # define the position of "btn2".
        btn2.move(150, 50)
        # "btn1" click function.
        btn1.clicked.connect(self.button_click)
        # "btn2" click function.
        btn2.clicked.connect(self.button_click)
        # define the statusBar.
        self.statusBar()
        # define the position of the window.
        self.setGeometry(1000, 300, 300, 300)
        # define the title of window.
        self.setWindowTitle("click function and signal")
        # shoe the window.
        self.show()

    def button_click(self):
        # create a "sender" object.
        sender = self.sender()
        # show the message.
        self.statusBar().showMessage(sender.text() + " is clicked.")


# main function
if __name__ == '__main__':
    # create a "app" object.
    app = QApplication(sys.argv)
    # instantiate a "ex" class.
    ex = Example()
    # quit the program.
    sys.exit(app.exec_())
