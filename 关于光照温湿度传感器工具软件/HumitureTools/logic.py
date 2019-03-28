# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(levelname)s- %(message)s')

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

#from Communcate import Communcate
#from Communcate_1 import sensorInstrument
from Communcate import Communcate


import time


#信号调用
class signal_ui(QtWidgets.QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        
        super(signal_ui,self).__init__()
        self.ser = serial.Serial()
        self.setupUi(self)
        self.Communcate= Communcate()        
        self.Close_pushButton.clicked.connect(self.portClose)
        self.Single_pushButton.clicked.connect(self.single) 
        self.Circle_pushButton.clicked.connect(self.circle)
        self.Stop_pushButton.clicked.connect(self.stopRead)
        
    
    
    def portClose(self):
        self.Communcate.close()
    
        
    def single(self,msg):
        self.Communcate.read_data()
        self.Show_label.setText("命令已发送！")
                                
       
    def circle(self,msg):
        while True:
            self.Communcate.read_data()
            time.sleep(int(self.Time_lineEdit.currentText()))
    
    def stopRead(self):
        self.Communcate.read_stop()
        self.Show_label.setText('serial read is cancel')
      

    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = signal_ui()
    ui.show()
    sys.exit(app.exec_())
 
        