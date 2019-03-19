# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:46:25 2019

@author: Gehaha
"""

import minimalmodbus

class RS485(minimalmodbus.Instrument):
    def __init__(self,port,slaveaddress):
        minimalmodbus.Instrument.__init__(self,'COM4',1)
        
        self.instrument = minimalmodbus.Instrument('COM4',1)
        self.instrument.serial.baudrate = 9600
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
        self.instrument.serial.stopbits = 1
        self.instrument.serial.timeout = 2
        self.instrument.debug = False 
        
    def slaveCommunicate(self):
        # request,number_of_bytes_read
        
        recieve_data = self.instrument._communicate(request,number_of_bytes_to_read)    
        return recieve_data
    
    def slaveEmbedPayload(self):
        pass
    
    def calculateCrcString(self):
        
        #一个双字节CRC字符串，其中最低的字节在第一个。
        input_data = ''
        crc_data =  minimalmodbus._calculateCrcString(input_data)
        return crc_data
    
        _checkString(inputstring, description='input CRC string')
       
        """
        register = OxFFFF
        for char in inputstring:
            register = (register >> 8) ^ _CRC16TABLE[(regitser ^ ord(char)) & 0xFF]
        return _numToTwoByteString(regitser,LsbFirst = True)
        """
        
        
    #Convert a byte string to a hex encoded string, with spaces for easier reading.
    #将字节字符串转换为十六进制编码的字符串，并使用空格以便阅读。
    def hexlify(self):
        
        bytestring = ''
        minimalmodbus._hexlify(bytestring,insert_spaces = True)
        
        
    #将一个双字节字符串转换为一个数值，可能会缩放它。    
    def twoByteStringToNum(self):
        
        num = []
        num =  minimalmodbus._twoByteStringToNum(bytestring,numberOfDecimals = 0,signed = False)
        return num
    
    def bytestringToValuelist(self):
        
        # bytestring 是采集到的数据
        
        Valuelist = []
        Valuelist = minimalmodbus._bytestringToValuelist(bytestring,numberofRegisters)
        return Valuelist
    
    def unpack(self):
        formatstring = 'formatstring (str): String for the packing. See the struct module for details.'
        packed = 'The bytestring to be unpacked.'
        
        # A value. The type depends on the formatstring.
        data = minimalmodbus._unpack(formatstring,packed)
        return data
    
        
        
    def portClose(self):
        pass
    
    
    
    def read_stop(self):
        pass
    
    
    def single(self):
        pass
    
    
    
    def loop(self):
        pass
    
    
   
    
    def get_illuminance(self):
        return self.read_register(40001,numberOfDecimals = 0,functioncode= 0x03,signed=False)
    
    
    
    def get_temperature(self):
        return self.read_register(40002,numberOfDecimals = 2,functioncode= 0x03,signed=False)
    
    
    def get_humidity(self):
        return self.read_register(4003,numberOfDecimals = 2,functioncode= 0x03,signed=False)
    
        
    def get_windspeed(self):
        return self.read_register(40004,numberOfDecimals = 2,functioncode= 0x03,signed=False)
    
    
    def checkCrc(self):
        pass
    

   