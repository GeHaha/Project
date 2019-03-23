# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 15:52:00 2019

@author: Gehaha
"""

import binascii
import serial
import struct
import time,sys
import minimalmodbus

from Ui import Ui_MainWindow
from PyQt5 import QtCore,QtGui,QtWidgets

"""
instrument = minimalmodbus.Instrument('COM1',1)
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.address = 1
instrument.mode = minimalmodbus.MODE_RTU
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True
"""

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
        self.setupUi(self)
        
        
    def open(self):
        self.instrument = minimalmodbus.Instrument('COM1',1)
        self.instrument.serial.baudrate = 9600
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity = serial.PARITY_NONE
        self.instrument.serial.stopbits = 1
        self.self.instrument.address = 1
        self.instrument.mode = minimalmodbus.MODE_RTU
        if self.ser.open():
            self.Show_label.setText("串口已打开！")
        else:
            self.Show_label.setText("串口未打开，请打开串口！")

    
    def closed(self):
        if self.ser.closed():
            self.Show_label.setText("串口已关闭！")
        else:
            self.Show_label.setText("串口未关闭,请关闭串口！")
    
    def receive(self):
        pass
    
        """
        num = 0
        if size:
            data_receive = self.ser.read_all()
            self.Show_label.setText("正在接收数据...")
            self.Recieve_plainTextEdit.append(data_receive.decode()
            
        else:
            self.Recieve_plainTextEdit.append(binascii.b2a_hex(data_receive).decode())
        self.Recieve_plainTextEdit.moveCursor(QtGui.QTextCursor.End)
        self.ser.flushInput()
        num += 1
        self.Show_label.setText("接收：" + str(num))
        
        """
    def send(self):
        self.instrument.read_register(3,1)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    