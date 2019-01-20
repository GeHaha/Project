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
import minimalmodbus


instrument = minimalmodbus.Instrument('COM1',1)
instrument.serial.baudrate = 9600
instrument.serial.byteszie = 8
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.address = 1   # this is the slave address number
instrument.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True

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


    def close(self):
        self.ser.close()
               
    def send(self):
        self.ser.write(binascii.a2b_hex(self.Send_lineEdit)
        
    def receive(self):      
        res_data = ''
        while(self.ser.isOpen()):
            size = self.ser.inWaiting()
            if size:
                res_data = self.ser.read_all()
                self.Recieve_plainTextEdit.append(res_data.decode())
                      
                msg = DataPack()
                msg.setData()
                return msg
                self.ser.flushInput()
               
               # self.Recieve_plainTextEdit.append(res_data.decode())       
               # self.Recieve_plainTextEdit.moveCursor(QtGui.QTextCursor.End)
               # self.ser.flushInput()
               # self.Show_label.setText("接收成功")
                
    #read the register 1 data,光照度
    def get_illuminance(self):
        illuminance = instrument.read_register(1,1,3,signed = True)
        print(illuminance)
    
    
    #read the register 2 data 温度
    def get_temperature(self):
        temperature = instrument.read_register(2,2,3,signed = True)
        print(temperature)
    
    #read the register 3 data 湿度
    def get_humidity(self):
        humidity = instrument.read_register(3,2,3,signed = False)
        print(humidity)
        
   
    #read the register 4 data 风 
    def get_airspeed(self): 
        airspeed = instrument.read_register(4,1,3,signed = False)   
        print(airspeed)
   
    def show_illuminance(self):
        pass
        
    
    def show_temperature(self):
        pass
    
    def show_humidity(self):
        pass
    
    def show_airspeed(self):
        pass
    
    
        
    
    
    