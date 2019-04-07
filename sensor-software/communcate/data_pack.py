# -*- coding: utf-8 -*-

import minimalmodbus

def singletonDecorator(cls, *args, **kwargs):
    """
    the singleton decorator.
    """
    instance = {}

    def wrapperSingleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapperSingleton

@singletonDecorator
class DataPack():
    """
    sensor's data package
    """

    def __init__(self, name):
        self.__name = name
          
    def set_data(self, data):
        self.__set_illuminance(data)
        self.__set_humidity(data)
        self.__set_temperature(data)
        self.__set_windspeed(data)
    
    def illuminance(self):
        return self.__illuminance
    
    def temperature(self):
        return self.__temperature    
        
    def humidity(self):
        return self.__humidity
        
    def windspeed(self):
        return self.__windspeed
    
    def name(self):
        return self.__name

    # TODO(Gehaha)    
    # def __address(self):
    #     pass

    # def __set_functionCode(self):
    #     pass
    
    # def __datalen(self):
    #     pass
    
    # def __set_crc(self):
    #     pass
        
    def __set_illuminance(self, data):
        self.__illuminance = minimalmodbus._twoByteStringToNum(data[3:5],
                                                               numberOfDecimals = 0,signed = False)
    def __set_temperature(self, data):
        self.__temperature = minimalmodbus._twoByteStringToNum(data[5:7],
                                                               numberOfDecimals = 2,signed = False)
      
    def __set_humidity(self, data):
        self.__humidity = minimalmodbus._twoByteStringToNum(data[7:9],
                                                            numberOfDecimals = 2,signed = False)
      
    def __set_windspeed(self, data):
        self.__windspeed = minimalmodbus._twoByteStringToNum( data[9:11],
                                                             numberOfDecimals = 2,signed = False)

    def print_data(self):
        print("illuminace: ", self.__illuminance)
        print("temperature:", self.__temperature)
        print("humidity:   ", self.__humidity)
        print("windspeed:  ", self.__windspeed)
        print()
