import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QApplication
from PyQt5.QtGui import QColor


# create a class.
class RGBSquareExample(QWidget):

    # initialization function
    def __init__(self):
        # inherits "QWidget" class.
        super().__init__()
        # define default color.
        self.col = QColor(0, 0, 0)
        # create a "square" to show color.
        self.square = QFrame(self)
        # call the "init_ui" function.
        self.init_ui()

    # interface function.
    def init_ui(self):

        # create red button.
        red_btn = QPushButton("Red", self)
        # set the button check to "True".
        red_btn.setCheckable(True)
        # set the position of "red_btn".
        red_btn.move(10, 10)
        # set button click function.
        red_btn.clicked[bool].connect(self.set_color)
        # create green button.
        green_btn = QPushButton('Green', self)
        # set the button check to "True".
        green_btn.setCheckable(True)
        # set the position of "green_btn".
        green_btn.move(10, 60)
        # set button click function.
        green_btn.clicked[bool].connect(self.set_color)
        # create blue button.
        blue_btn = QPushButton('Blue', self)
        # set the button check to "True".
        blue_btn.setCheckable(True)
        # set the position of "blue_btn".
        blue_btn.move(10, 110)
        # set button click function.
        blue_btn.clicked[bool].connect(self.set_color)
        # set the position and size of the "square"
        self.square.setGeometry(150, 30, 200, 100)
        # the style of the "square" change.
        self.square.setStyleSheet("QWidget {background-color: %s } " % self.col.name())
        # set the size of window.
        self.setGeometry(300, 300, 400, 300)
        # set the title of window.
        self.setWindowTitle("Toggle button")
        # show the window.
        self.show()

    # change color function.
    def set_color(self, pressed):
        # create(instantiate) a "sender" object.
        sender = self.sender()
        # define the pressed "value".
        if pressed:
            val = 255
        else:
            val = 0
        # judge which button is clicked.
        if sender.text() == "Red":
            self.col.setRed(val)
        elif sender.text() == "Green":
            self.col.setGreen(val)
        elif sender.text() == "Blue":
            self.col.setBlue(val)
        # set the style of "square" change.
        self.square.setStyleSheet("QFrame { background-color: %s } " % self.col.name())


# main function.
if __name__ == '__main__':
    # instantiate a "app" object.
    app = QApplication(sys.argv)
    # instantiate a "ex" object.
    ex = RGBSquareExample()
    # quit the program.
    sys.exit(app.exec_())
