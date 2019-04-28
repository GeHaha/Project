# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(738, 300)
        self.time_comboBox = QtWidgets.QComboBox(Form)
        self.time_comboBox.setGeometry(QtCore.QRect(80, 10, 111, 31))
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
        self.que_pushButton.setGeometry(QtCore.QRect(10, 160, 81, 31))
        self.que_pushButton.setObjectName("que_pushButton")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(200, 10, 521, 271))
        self.widget.setObjectName("widget")
        self.select_time_label = QtWidgets.QLabel(Form)
        self.select_time_label.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.select_time_label.setObjectName("select_time_label")
        self.start_time_label = QtWidgets.QLabel(Form)
        self.start_time_label.setGeometry(QtCore.QRect(10, 60, 71, 31))
        self.start_time_label.setObjectName("start_time_label")
        self.end_time_label = QtWidgets.QLabel(Form)
        self.end_time_label.setGeometry(QtCore.QRect(10, 110, 71, 31))
        self.end_time_label.setObjectName("end_time_label")
        self.start_dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.start_dateTimeEdit.setGeometry(QtCore.QRect(80, 60, 111, 31))
        self.start_dateTimeEdit.setObjectName("start_dateTimeEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(80, 110, 111, 31))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
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
        self.select_time_label.setText(_translate("Form", " 查询时间："))
        self.start_time_label.setText(_translate("Form", " 起始时间："))
        self.end_time_label.setText(_translate("Form", " 结束时间："))

