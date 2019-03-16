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
import crcmod
 
from Ui import Ui_MainWindow
from PyQt5 import QtCore,QtGui,QtWidgets


instrument = minimalmodbus.Instrument('COM1',1)
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.address = 1
instrument.mode = minimalmodbus.MODE_RTU
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
        self.setupUi(self)
        
        
    def open(self):
        
        if self.ser.open():
            self.Show_label.setText("串口已打开！")
        else:
            self.Show_label.setText("串口未打开，请打开串口！")

    
    def closed(self):
        if self.ser.closed():
            self.Show_label.setText("串口已关闭！")
        else:
            self.Show_label.setText("串口未关闭,请关闭串口！")
            
            
    def send(self):
        self.write(msg.data())
        
    def write(self,data):
        self.ser.write(data)
        
                    
    def read(self):
        res_data = ()
        while(self.ser.isOpen()):
            size = self.ser.inWaiting()
            if size:
                print(size)
                res_data = self.ser.read_all()
                return res_data
                self.ser.flushInput()
        
    
    def receive(self):
        data = self.read()
        print("receive data",data)
        msg = DataPack()
        msg.setData(data)
        return msg
    
       
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
    # 发送请求  
    """
    def send(self):
        
        self.instrument.read_register(3,1)
    """
    
    
# CRC校验   
    def CalCRC16(self,data,length):
        
        crc = 0xFFFF
        if length == 0:
            length = 1
            
        # for j in data,crc ^= j
        j = 0
        while length != 0 :
            crc ^= list.__getitem__(data,j)
            #print('j = 0x%02x,length = 0x%02x,crc = 0x%04x' %(j,length,crc))
            for i in range(0,8):
                if crc &1:
                    crc >>= 1
                    crc ^= 0xA001
                else:
                    crc >>= 1
            length -= 1
            j += 1
            # if length == 0
            # break
        return crc
    
        
    
    def CheckCRC(self,data,length,crctype):
        
        if length <3:
            print('The data len(%d) is less than 3 !!!',length)
            return 0
        crc_res = 0
        tmp = [0,0,0,0]
        if crctype == 0:
            crc_res = CalCRC16(data,length-2)
            tmp[0] = crc_res & 0xFF
            tmp[1] = (crc_res >> 8) & 0xFF
            
            if data[length-2] == tmp[0] and data[length-1] == tmp[1]:
                return 1
        elif crctype == 1:
            print('CRC32 is not support')
            return 0
        
# 测试用
if __name__ == '__main__':
    crc16 = crcmod.mkCrcFun(0x18005,initCrc = 0xFFFF,REV = True,xorOut = 0x0000)
    crc_array = b'0xFE 0XFD'
    crc_calc = crc16(crc_array)
    
    a= hex(crc_calc)
    print(crc_calc,a)
    
    crc_value = [0x01, 0x04, 0x13, 0x87, 0x00, 0x30]
    crc_transformation = CalCRC16(crc_value, len(crc_value))
    crc_calculation = hex(crc_transformation)
    # print('crc_calculation:',crc_calculation)
    tasd = [0x00, 0x00]
    tasd[0] = crc_transformation & 0xFF
    tasd[1] = (crc_transformation >> 8) & 0xFF
    H = hex(tasd[0])
    L = hex(tasd[1])
    H_value = int(H, 16)
    L_value = int(L, 16)
    crc_value.append(H_value)
    crc_value.append(L_value)
    print(crc_value)  # calculation value   CRC

    # ========================================================
    print('\n')
    # crc_value2 = [0x01, 0x04, 0x13, 0x87, 0x00, 0x30,0x44,0xB3]
    # print('crc_value2:',crc_value2)
    # crc_cheak=CheckCRC(crc_value2,len(crc_value2),0)

    crc_check = CheckCRC(crc_value, len(crc_value), 0)
    if crc_check == 1:
        print('Right')
    else:
        print('wrong')

    print(crc_check)  # check calculation value

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    