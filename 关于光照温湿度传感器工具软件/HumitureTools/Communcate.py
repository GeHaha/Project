# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 16:29:43 2018

@author: Gehaha
"""
import binascii
import serial
from SerialPack import DataPack
import DataBase
import struct
import time
from Ui import Ui_MainWindow
import serial
from PyQt5 import QtCore,QtGui,QtWidgets
import sys
import time


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
            self.Open_pushButton.setEnavled(False)  
            self.Show_label.setText("串口已打开")          
        else:
            self.Show_label.setText("请打开串口")
            
    def close(self):
        self.ser.close()
         
    def send(self,msg):
        msg = self.Send_lineEdit.setText()
        self.ser.write(msg)
        
    def receive(self):
        num = 0
        res_data = []
        while(self.ser.isOpen()):
            
            size = self.ser.inWaiting()
            if size:
                res_data = self.ser.read_all() #获取所有数据
                self.Recieve_plainTextEdit.append(binascii.b2a_hex(res_data).decode())
                self.Recieve_plainTextEdit.moveCursor(QtGui.QTextCursor.End)
                self.ser.flushInput()
                num  += 1
                self.Show_label.setText("接收数据 :" + str(num))
        
    
    
    