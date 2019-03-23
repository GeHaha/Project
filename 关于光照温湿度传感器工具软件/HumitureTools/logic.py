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
        self.Stop_pushButton.clicked.connect(self.stop)
        
    
    
    def portClose(self):
        self.Communcate.close()
    
        
    def single(self,msg):
        self.Communcate.send()
        self.Show_label.setText("one send")                           
        
    def circle(self,msg):
        while True:
            self.Communcate.send()
            time.sleep(int(self.Time_lineEdit.currentText()))
    
    def stop(self):
        self.ser.cancel_read()
        self.Show_label.setText('serial read is cancel')
      
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = signal_ui()
    ui.show()
    sys.exit(app.exec_())
 
        