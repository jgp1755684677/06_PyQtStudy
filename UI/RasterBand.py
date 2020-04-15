# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RasterBand.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(454, 147)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 41, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_data_input = QtWidgets.QPushButton(Form)
        self.btn_data_input.setGeometry(QtCore.QRect(360, 30, 75, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.btn_data_input.setFont(font)
        self.btn_data_input.setObjectName("btn_data_input")
        self.btn_ok = QtWidgets.QPushButton(Form)
        self.btn_ok.setGeometry(QtCore.QRect(360, 70, 75, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.btn_ok.setFont(font)
        self.btn_ok.setObjectName("btn_ok")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(80, 30, 271, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "文件打开"))
        self.label.setText(_translate("Form", "路径："))
        self.btn_data_input.setText(_translate("Form", "浏览"))
        self.btn_ok.setText(_translate("Form", "确定"))
