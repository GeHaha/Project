# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot_4.30.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(738, 300)
        self.que_pushButton = QtWidgets.QPushButton(Form)
        self.que_pushButton.setGeometry(QtCore.QRect(10, 110, 81, 31))
        self.que_pushButton.setObjectName("que_pushButton")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(220, 10, 501, 271))
        self.widget.setObjectName("widget")
        self.start_time_label = QtWidgets.QLabel(Form)
        self.start_time_label.setGeometry(QtCore.QRect(10, 20, 71, 31))
        self.start_time_label.setObjectName("start_time_label")
        self.end_time_label = QtWidgets.QLabel(Form)
        self.end_time_label.setGeometry(QtCore.QRect(10, 60, 71, 31))
        self.end_time_label.setObjectName("end_time_label")
        self.start_dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.start_dateTimeEdit.setGeometry(QtCore.QRect(80, 20, 131, 31))
        self.start_dateTimeEdit.setObjectName("start_dateTimeEdit")
        self.end_dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.end_dateTimeEdit.setGeometry(QtCore.QRect(80, 60, 131, 31))
        self.end_dateTimeEdit.setObjectName("end_dateTimeEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.que_pushButton.setText(_translate("Form", "查询"))
        self.start_time_label.setText(_translate("Form", " 起始时间："))
        self.end_time_label.setText(_translate("Form", " 结束时间："))
        self.start_dateTimeEdit.setDisplayFormat("yyyy-MM-ddHH:mm:ss")
        self.end_dateTimeEdit.setDisplayFormat("yyyy-MM-ddHH:mm:ss")
