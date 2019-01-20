# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 20:37:49 2018

@author: Gehaha
"""
import Protocal

from Protocal import SerialPackage

DeviceId = [0X01]
FunctionCode =[0X03]
DataLen = [0x08]
Illuminance = [0x00,0x00]
Temperature = [0x00,0x00]
Humidity = [0x00,0x00]
Airspeed = [0x00,0x00]
Crc= [0x00,0x00]

class DataPack():
    def __init__(self):
        self.msg = Protocal.SerialPackage
    
    def get_data(self):
        return self.msg
        
    def get_DecieveID(self):
        return self.msg[0] 
        
    
    def get_FunctionCode(self):
        return self.msg[1] 
              
    def get_DataLen(self):
        return self.msg[2]

    def get_illuminance(self):
        return self.msg[3]
  
 
    def get_temperature(self):
        return self.msg[4]
         
    def get_humidity(self):
        return self.msg[5]
    
    def get_airspeed(self):
        return self.msg[6]
           
    def crc(self):
        return self.msg[7]
    
    def CheckCrc(self):
        self.msg[7] = self.msg[0]+self.msg[1]+ self.msg[2] + self.msg[3] + self.msg[4] + self.msg[5] +self.msg[6]
        
    def calculate_crc16(self,data):
        crc = 0xFFFF
        
        for char in data:
            crc = (crc >> 8)^ Const.CRC16_TABLE[((crc)^char) & 0xFF]
        
        return struct.pack('<H',crc)
    
            
            
            
            
            
            
            
            
            