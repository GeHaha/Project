# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 18:58:31 2018

@author: Gehaha
"""

import minimalmodbus
import serial
from Ui import Ui_MainWindow


class Communcate(QtWidgets.QMainWindow,Ui_MainWindow):
  
    def __new__(cls):
        if not cls.__instance:
            Communcate.__instance = super().__new__(cls)
        return cls.__instance  
    
    def __init__(self):
        super(Communcate,self).__init__()
        if not self.__isFirstInit:
            self.__connectState = False       
        else:
            pass
        self.setupUi(self)
        
    def connect(self):
        self.instrument.serial.port = 'COM4'
        self.instrument.serial.baudrate = 9600
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity = serial.PARITY_NONE
        self.instrument.serial.stopbits = 1
        self.address = 1     
        self.instrument.mode = minimalmodbus.MODE_RTU    
        self.instrument.serial.open()
        

    def close(self):
        self.minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True
  
    def single(self):
        pass
    
    def circle(self):
        pass
    
