# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication
from PyQt5.QtCore import QBasicTimer


# create a "Example" class.
class Example(QWidget):

    # initialization function.
    def __init__(self):
        # instantiate the "QWidget" class.
        super().__init__()
        # instantiate a "QProgressBar" class.
        self.progress_bar = QProgressBar(self)
        # instantiate a "QPushButton" class.
        self.btn_start = QPushButton("Start", self)
        # instantiate a "QBasicTimer" class.
        self.timer = QBasicTimer()
        # create a "step" variable.
        self.step = 0
        # call the "init_ui" function.
        self.init_ui()

    # define the "init_ui" function.
    def init_ui(self):
        # set the position of "progress_bar".
        self.progress_bar.setGeometry(30, 40, 200, 25)
        # set the position of "btn_start".
        self.btn_start.move(40, 80)
        # set the click function.
        self.btn_start.clicked.connect(self.do_action)
        # set the position of window.
        self.setGeometry(300, 300, 280, 170)
        # set the title of window.
        self.setWindowTitle('QProgressBar')
        # show the window.
        self.show()

    # create time event.
    def timerEvent(self, event):
        # judge the step >= 100.
        if self.step >= 100:
            # the show of time stop.
            self.timer.stop()
            # set the text of btn_start.
            self.btn_start.setText("Finished")
        # set the step
        self.step = self.step + 4
        # show the step in she "progress_bar".
        self.progress_bar.setValue(self.step)

    # create action event.
    def do_action(self):
        # judge the status of timer
        if self.timer.isActive():
            # the show of time stop.
            self.timer.stop()
            # set the text of "btn_start" to "Start".
            self.btn_start.setText('Start')
        else:
            # set the "timer" "start".
            self.timer.start(100, self)
            # set the text of btn_start to "Stop".
            self.btn_start.setText("Stop")


# main function.
if __name__ == '__main__':
    # instantiate a "app" class.
    app = QApplication(sys.argv)
    # instantiate a "ex" class.
    ex = Example()
    # quit the program.
    sys.exit(app.exec_())
