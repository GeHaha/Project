# -*- coding: utf-8 -*-

@author: Gehaha
"""

import minimalmodbus
from data_pack import DataPack

class Communcate(object):
    """
    communcate with the modbus sensor
    """

    def __init__(self):
        self.__package = DataPack("sensor of modbus")
         
    def open_port(self):
        # TODO fix param
        minimalmodbus.Instrument.__init__(self,'COM4',1)
        self.__instrument = minimalmodbus.Instrument('COM4',1)
        self.__instrument.serial.baudrate = 9600
        self.__instrument.serial.bytesize = 8
        self.__instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
        self.__instrument.serial.stopbits = 1
        self.__instrument.serial.timeout = 2
        self.__instrument.debug = True
        self.__instrument.handle_local_echo = False
        self.__instrument.precalculate_read_size = True
        print("port open")
        
    def close_port(self):
        self.__instrument.serial.close()
        
    def pause(self):
        self.__instrument.serial.cancel_read()
    
    def open_modbus_log(self):
        self.__instrument.debug = True
    
    def close_modbus_log(self):
        self.__instrument.debug = False
    
    # TODO
    def set_modbus_config(self, address, mode, function_code):
        
        self.__request_data = ''
        # 从slaveaddress、功能号和有效负载数据构建一个请求
        slaveaddress = address
        mode = mode
        functioncode = function_code
        #要发送到从服务器的字节字符串
        payloaddata = '\x00\x00\x00\x04'
        self.__request_data =  minimalmodbus._embedPayload(slaveaddress,mode,functioncode,payloaddata)     

    def request_data(self):
        """request sensor's data utill get the right data.""" 

        data = self.__instrument._communicate(self.__request_data, 13)
        
        if (data[0] == '\x01'):
            self.__package.set_data(data)
        else:
            self.request_data()
          
    def print_data(self):
        print ("illuminance", self.__package.illuminance())
        print ("temperature", self.__package.temperature())
        print ("humidity", self.__package.humidity())
        print ("windspeed", self.__package.windspeed())
        
    



        
    

   