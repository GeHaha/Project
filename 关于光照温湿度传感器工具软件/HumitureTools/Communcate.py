# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:46:25 2019

@author: Gehaha
"""
import crcmod
import minimalmodbus
import dbconnect
from dataPack import dataPack

class Communcate():
    """
    """
    def __init__(self):
        self.__package = dataPack("sensor of modbus")
         
    def openPort(self):
        minimalmodbus.Instrument.__init__(self,'COM4',1)
        self.__instrument = minimalmodbus.Instrument('COM4',1)
        self.__instrument.serial.baudrate = 9600
        self.__instrument.serial.bytesize = 8
        self.__instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
        self.__instrument.serial.stopbits = 1
        self.__instrument.serial.timeout = 2
        self.__instrument.debug = False
        self.__instrument.handle_local_echo =False
        self.__instrument.precalculate_read_size = True
    
    def closePort(self):
        self.__instrument.serial.close()
        
    def pause(self):
        self.__instrument.serial.cancel_read()
    
    """      
    构建一个请求命令从地址、功能码、和数据
    """
    def setRequstConfig(self, address, mode, function_code):
        
        self.__request_data = ''
        # 从slaveaddress、功能号和有效负载数据构建一个请求
        slaveaddress = address
        mode = mode
        functioncode = function_code
        #要发送到从服务器的字节字符串
        payloaddata = '\x00\x00\x00\x04'
        #self.request_data = minimalmodbus._embedPayload(slaveaddress,mode,functioncode,payloaddata)        
        #return self.request_data
        self.__request_data =  minimalmodbus._embedPayload(slaveaddress,mode,functioncode,payloaddata)     
    
        
    def requestData(self):
        data = self.__instrument._communicate(self.__request_data, 13)
        
        if data[0] == '\x01':
            self.__package.setData(data)
        else:
            self.requestData()
          
    def printData(self):
        print ("illuminance", self.__package.illuminance())
        print ("temperature", self.__package.temperature())
        print ("humidity", self.__package.humidity())
        print ("windspeed", self.__package.windspeed())
        print ()
    
#    def fetchDataBase(self):
#        self.get_data = dbconnect.dbConnect()
#        self.data = self.get_data.fetch()
        
        

def test():  
    sensorCommuncate = Communcate()
    sensorCommuncate.openPort()
    sensorCommuncate.setRequstConfig(0x01, 'rtu', 0x03)
    sensorCommuncate.requestData()
    
    sensorCommuncate.printData()


while True:   
    test()  

    

        
    

   