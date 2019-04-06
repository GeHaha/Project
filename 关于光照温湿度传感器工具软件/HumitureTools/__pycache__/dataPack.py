# -*- coding: utf-8 -*-

import minimalmodbus


def singletonDecorator(cls, *args, **kwargs):
    """定义一个单例装饰器"""
    instance = {}

    def wrapperSingleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapperSingleton

@singletonDecorator
class dataPack():
    
    def __init__(self, name):
        self.__name = name
          
    def setData(self,data):
        self.__setIlluminance(data)
        self.__setHumidity(data)
        self.__setTemperature(data)
        self.__setWindspeed(data)
    
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
    
    def __setFunctionCode(self):
        pass
    
    def __setCrc(self):
        pass
        
    def __setIlluminance(self,data):
        self.__illuminance = minimalmodbus._twoByteStringToNum(data[3:5],
                                                               numberOfDecimals = 0,signed = False)
    def __setTemperature(self,data):
        self.__temperature = minimalmodbus._twoByteStringToNum(data[5:7],
                                                               numberOfDecimals = 2,signed = False)
      
    def __setHumidity(self,data):
        self.__humidity = minimalmodbus._twoByteStringToNum(data[7:9],
                                                            numberOfDecimals = 2,signed = False)
      
    def __setWindspeed(self,data):
        self.__windspeed = minimalmodbus._twoByteStringToNum( data[9:11],
                                                             numberOfDecimals = 2,signed = False)

def test():
    package = dataPack("sensor of modbus")
    package.setData("\x01\x03\x08\x00Ä\t?\x13Ö\x00\x00áû")
    
    print (package.illuminance())
    print (package.temperature())
    print (package.humidity())
    print (package.windspeed())
    print ('\n')
    
    package2 = dataPack()
    package2.setData("\x01\x03\x08\x00Ä\tB\x13½\x00\x00ü-")
    print (package.illuminance())
    print (package.temperature())
    print (package.humidity())
    print (package.windspeed())

TEST = True

if TEST:
    test() 
    
