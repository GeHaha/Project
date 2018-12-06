# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 16:29:43 2018

@author: Gehaha
"""
import serial
from SerialPack import DataPack
import DataBase
import struct
import time
from Ui import Ui_MainWindow
import serial
from PyQt5 import QtCore,QtGui,QtWidgets
import sys


class Communcate(QtWidgets.QMainWindow,Ui_MainWindow):
    __instance = None
    __isFirstInit = False
    
    def __new__(cls):
        if not cls.__instance:
            Communcate.__instance = super().__new__(cls)
        return cls.__instance
    
    
    def __init__(self):
        super(Communcate,self).__init__()
        if not self.__isFirstInit:
            self.__connectState = False
            self.ser = serial.Serial()
        else:
            pass
        self.ser = serial.Serial()
        self.setupUi(self)
    
    def connect(self):
        self.ser.port = self.Port_comboBox.currentText()
        self.ser.baudrate = self.Baud_comboBox.currentText()
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.parity = serial.PARITY_NONE
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.open()
        if(self.ser.open()):
            self.Show_label.setText("串口已打开")
            return True
        else:
            self.Show_label.setText("请打开串口")
            return False
        
    def close(self):
        self.ser.close()
         
    def single(self):
        pass
    
    def circle(self):
        pass
    
    def receive(self):
        pass
    
    
    