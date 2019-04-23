# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("温湿度曲线图")
        Form.resize(705, 300)
        self.time_comboBox = QtWidgets.QComboBox(Form)
        self.time_comboBox.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.time_comboBox.setObjectName("time_comboBox")
        self.time_comboBox.addItem("")
        self.time_comboBox.addItem("")
        self.time_comboBox.addItem("")
        self.time_comboBox.addItem("")
        self.time_comboBox.addItem("")
        self.time_comboBox.addItem("")
        self.time_comboBox.addItem("")
        self.time_comboBox.addItem("")
        self.time_comboBox.addItem("")
        self.time_comboBox.addItem("")
        self.que_pushButton = QtWidgets.QPushButton(Form)
        self.que_pushButton.setGeometry(QtCore.QRect(10, 120, 81, 31))
        self.que_pushButton.setObjectName("que_pushButton")
        self.stop_pushButton = QtWidgets.QPushButton(Form)
        self.stop_pushButton.setGeometry(QtCore.QRect(10, 230, 81, 31))
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(120, 10, 571, 271))
        self.widget.setObjectName("widget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "温湿度曲线图"))
        self.time_comboBox.setItemText(0, _translate("Form", "1小时"))
        self.time_comboBox.setItemText(1, _translate("Form", "3小时"))
        self.time_comboBox.setItemText(2, _translate("Form", "1天"))
        self.time_comboBox.setItemText(3, _translate("Form", "3天"))
        self.time_comboBox.setItemText(4, _translate("Form", "7天"))
        self.time_comboBox.setItemText(5, _translate("Form", "15天"))
        self.time_comboBox.setItemText(6, _translate("Form", "1月"))
        self.time_comboBox.setItemText(7, _translate("Form", "3月"))
        self.time_comboBox.setItemText(8, _translate("Form", "6月"))
        self.time_comboBox.setItemText(9, _translate("Form", "1年"))
        self.que_pushButton.setText(_translate("Form", "查询"))
        self.stop_pushButton.setText(_translate("Form", "暂停"))

