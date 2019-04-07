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

from ui import Ui_MainWindow
from PyQt5 import QtCore,QtGui,QtWidgets

import serial.tools.list_ports
import binascii
import time



# the name is too bad
class signal_ui(QtWidgets.QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        
        super(signal_ui,self).__init__()
        self.ser = serial.Serial()
        self.setupUi(self)
        self.Communcate = Communcate() 
        self.dataPack = DataPack()
        
        self.Open_pushButton.clicked.connect(self.Open)
        self.Close_pushButton.clicked.connect(self.Close)
        self.Signal_pushButton.clicked.connect(self.single) 
        self.Circle_pushButton.clicked.connect(self.circle)
        self.Stop_pushButton.clicked.connect(self.stopRead)
        #self.Curve_pushButton.clicked.connect(self.)
    
    def Open(self):
        self.Communcate.openPort()
        self.Show_label.setText("Open port success!")    
    
    def Close(self):
        self.Communcate.closePort()
    
        
    def single(self,msg):       
        self.Communcate.requestData()()   
        self.illumation_lineEdit.setText(self.dataPack.illuminance())
        self.Show_label.setText("Request to be send！")
        
        
    def circle(self,msg):
        while True:
            self.Communcate.requestData()
            #time.sleep(int(self.Time_lineEdit.currentText()))
        else:
            return 
      
    
    def stopRead(self):
        self.Communcate.pause()
        self.Show_label.setText('serial read is cancel')
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = signal_ui()
    ui.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
        