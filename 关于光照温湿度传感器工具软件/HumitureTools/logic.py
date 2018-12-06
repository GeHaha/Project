# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:08:58 2018

@author: Gehaha
"""

import sys
from Ui import Ui_MainWindow
from Ui import Ui_MainWindow
import serial
import serial.tools.list_ports
from PyQt5 import QtCore,QtGui,QtWidgets
import sys
import binascii

from Communcate import Communcate
from DataBase import DataBase


#信号调用
class signal_ui(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(signal_ui,self).__init__()
        self.ser = serial.Serial()
        self.setupUi(self)
        self.Communcate= Communcate() 
        
        self.Open_pushButton.clicked.connect(self.port_connect)
        self.Close_pushButton.clicked.connect(self.port_close)
        self.Single_pushButton.clicked.connect(self.single) 
        self.Circle_pushButton.clicked.connect(self.circle)
        
    def port_connect(self):
        self.communcate.connect()
        self.Show_label.setText('打开成功！')
        
    def port_close(self):
        self.communcate.close()
        self.Show_label.setText("关闭成功！")
        
    def single(self):
        pass
    
    def circle(self):
        pass


    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = signal_ui()
    ui.show()
    sys.exit(app.exec_())
 
        