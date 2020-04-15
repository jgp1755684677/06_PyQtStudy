# -*- coding: utf-8 -*-
import sys
from UI.RasterBand import Ui_Form
from PyQt5.QtWidgets import *
from Codes.RasterIO_TIFF import show_tiff


# create a "RasterBandForm" used to inherits Ui_Form.
class RasterBandForm(QWidget, Ui_Form):
    def __init__(self):
        super(RasterBandForm, self).__init__()
        self.setupUi(self)
        self.btn_ok.clicked.connect(self.func_btn_ok)
        self.btn_data_input.clicked.connect(self.func_btn_data_input)

    def func_btn_data_input(self):
        get_filename_path, ok = QFileDialog.getOpenFileName(self, "选取单个文件", "F:\\Classes\\空间数据库技术及应用\\作业\\05_RasterDataStudy\\RasterData", "All Files (*);;TIF Files (*.tif)")
        if ok:
            self.textBrowser.setText(str(get_filename_path))

    def closeEvent(self, QCloseEvent):
        res = QMessageBox.question(self, "消息", "是否关闭这个窗口？", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if res == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def func_btn_ok(self):
        print("OK")
        input_path = self.textBrowser.toPlainText()
        print("Input path:" + input_path)
        if input_path:
            show_tiff(input_path)
            print("to do!")
        else:

            msg_box = QMessageBox(QMessageBox.Warning, "Alert", "请输入路径!")
            msg_box.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show = RasterBandForm()
    show.show()
    sys.exit(app.exec_())
