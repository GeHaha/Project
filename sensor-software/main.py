# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(levelname)s- %(message)s')

"""
Created on Thu Dec  6 15:08:58 2018

@author: Gehaha
"""

import sys
from Ui import Ui_MainWindow
import serial
import serial.tools.list_ports
from PyQt5 import QtCore,QtGui,QtWidgets

import binascii
import dbconnect
import time
from Communcate import Communcate
import dbconnect
from dataPack import dataPack



#信号调用
class signal_ui(QtWidgets.QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        
        super(signal_ui,self).__init__()
        self.ser = serial.Serial()
        self.setupUi(self)
        self.sensorCommuncate= Communcate() 
        self.dataPack = dataPack()
        
        self.Open_pushButton.clicked.connect(self.Open)
        self.Close_pushButton.clicked.connect(self.Close)
        self.Signal_pushButton.clicked.connect(self.single) 
        self.Circle_pushButton.clicked.connect(self.circle)
        self.Stop_pushButton.clicked.connect(self.stopRead)
        #self.Curve_pushButton.clicked.connect(self.)
    
    def Open(self):
        self.sensorCommuncate.openPort()
        self.Show_label.setText("Open port success!")    
    
    def Close(self):
        self.sensorCommuncate.closePort()
    
    
    
        
    def single(self,msg):  
        self.sensorCommuncate.setRequstConfig(0x01,'rtu',0x03)
        self.sensorCommuncate.requestData()
        self.showData()
        
#        self.illumation_lineEdit.setText(str(self.dataPack.illuminance()))
#        self.Temp_lineEdit.setText(str(self.dataPack.temperature()))
#        self.Humidity_lineEdit.setText(str(self.dataPack.humidity()))
#        self.windSpeed_lineEdit.setText(str(self.dataPack.windspeed()))
        self.Show_label.setText("Request to be send！")
        
        
    def circle(self,msg):
        while True:
            time.sleep(int(self.Time_lineEdit.setText()))
            self.sensorCommuncate.setRequstConfig(0x01,'rtu',0x03)
            self.sensorCommuncate.requestData()
            self.showData()
            #time.sleep(int(self.Time_lineEdit.currentText()))
        else:
            pass
        
        
    def showData(self):
        self.illumation_lineEdit.setText(str(self.dataPack.illuminance()))
        self.Temp_lineEdit.setText(str(self.dataPack.temperature()))
        self.Humidity_lineEdit.setText(str(self.dataPack.humidity()))
        self.windSpeed_lineEdit.setText(str(self.dataPack.windspeed()))
    
    def stopRead(self):
        self.sensorCommuncate.pause()
        self.Show_label.setText('serial read is cancel')
        

    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = signal_ui()
    ui.show()
    sys.exit(app.exec_())
 
        