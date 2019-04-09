# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(levelname)s- %(message)s')

"""
Created on Thu Dec  6 15:08:58 2018

@author: Gehaha
"""

import sys
sys.path.append("communcate")
sys.path.append("ui")
sys.path.append("data_base")


from communcate import Communcate
from data_pack import DataPack


from Ui import Ui_MainWindow
from PyQt5 import QtCore,QtGui,QtWidgets


import serial.tools.list_ports
import binascii
import time


# the name is too bad
class SignalUi(QtWidgets.QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        
        super(SignalUi,self).__init__()
        self.ser = serial.Serial()
        self.setupUi(self)

        self.sensorCommuncate= Communcate() 
        self.dataPack = DataPack()

        
        self.Open_pushButton.clicked.connect(self.port_open)
        self.Close_pushButton.clicked.connect(self.port_close)
        self.Signal_pushButton.clicked.connect(self.single) 
        self.Circle_pushButton.clicked.connect(self.circle)
        self.Stop_pushButton.clicked.connect(self.stop_read)
        #self.Curve_pushButton.clicked.connect(self.)
    
    def port_open(self):
        self.sensorCommuncate.open_port()
        self.Show_label.setText("Open port success!")    
    
    def port_close(self):
        self.sensorCommuncate.close_port()

        
    def single(self,msg):  
        self.sensorCommuncate.set_modbus_config(0x01,'rtu',0x03)
        self.sensorCommuncate.request_data()
        self.__show_data()
        self.Show_label.setText("Request to be send！")
        
        
    def circle(self,msg):
        while True:           
            self.sensorCommuncate.set_modbus_config(0x01,'rtu',0x03)
            self.sensorCommuncate.request_data()
            self.__show_data()
            time.sleep(1000)
        else:
            pass
    
    def stop_read(self):
        self.sensorCommuncate.pause()
        self.Show_label.setText('serial read is cancel')
        
        
    def __show_data(self):      
        self.illumation_lineEdit.setText(str(self.dataPack.illuminance()))
        self.Temp_lineEdit.setText(str(self.dataPack.temperature()))
        self.Humidity_lineEdit.setText(str(self.dataPack.humidity()))
        self.Airspped_lineEdit.setText(str(self.dataPack.windspeed()))



def main():
    app = QtWidgets.QApplication(sys.argv)
   # MainWindow = QtWidgets.QMainWindow()
    ui = SignalUi()
    ui.show()
    sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()
    
        