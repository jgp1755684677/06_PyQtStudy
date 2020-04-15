# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtGui import QFont


# create a class.
class Example(QWidget):

    # initialization function
    def __init__(self):
        # inherits the "QWidget" class.
        super().__init__()
        # call the "init_ui" function.
        self.init_ui()

    # interface function.
    def init_ui(self):
        # create a button object.
        btn = QPushButton('Button', self)
        # set the font and font size of button.
        btn.setFont(QFont('Arial', 24))
        # set tooltip of button.
        btn.setToolTip('This is a button.')
        # resize button.
        btn.resize(btn.sizeHint())
        # define the position of button.
        btn.move(100, 50)
        # set the title of window.
        self.setWindowTitle('Tooltips')
        # show the window.
        self.show()


if __name__ == '__main__':
    # instantiate a "app" object.
    app = QApplication(sys.argv)
    # instantiate a "ex" object
    ex = Example()
    # quit the program.
    sys.exit(app.exec_())
