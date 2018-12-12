# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 20:37:49 2018

@author: Gehaha
"""
import Protocal

from Protocal import SerialPackage
DeviceId = [0X01]
FunctionCode =[0X03]
StartId= [0x00,0x00]
DataLen = [0x00,0x04]
Crc= [0x44,0x09]

class DataPack():
    def __init__(self):
        self.msg = Protocal.SerialPackage
    
    def data(self):
        return self.msg
        
    def setDecieveID(self):
        return self.msg[0] 
        
    
    def setFunctionCode(self):
        return self.msg[1] 
        
    def setStartId(self):
        return self.msg[2]
        
    def setDataLen(self):
        return self.msg[3] 
         
    def crc(self):
        return self.msg[4]
    
    
        