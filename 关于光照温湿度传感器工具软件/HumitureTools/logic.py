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
import time

#信号调用
class signal_ui(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(signal_ui,self).__init__()
        self.ser = serial.Serial()
        self.setupUi(self)
        self.Communcate= Communcate()        
        self.Close_pushButton.clicked.connect(self.port_close)
        self.Single_pushButton.clicked.connect(self.single) 
        self.Circle_pushButton.clicked.connect(self.circle)
        self.Stop_pushButton.clicked.connect(self.stop)
        
        
    def port_close(self):
        self.Communcate.close()
        self.Show_label.setText("关闭成功！")
        
        
    def single(self):
        self.Communcate.send()
        self.Show_label.setText("one send")
        
    def circle(self):
        while True:
            self.Communcate.send()
            time.sleep(int(self.Time_lineEdit.currentText()))
    
    def stop(self):
        pass
    
        
         
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = signal_ui()
    ui.show()
    sys.exit(app.exec_())
 
        