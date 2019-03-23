# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 20:31:21 2019

@author: Gehaha
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import serial
import struct
import sys
import time
import minimalmodbus
from Ui import Ui_MainWindow

_NUMBER_OF_BYTES_PER_REGISTER = 2
_SECONDS_TO_MILLISECONDS = 1000
_ASCII_HEADER = ':'
_ASCII_FOOTER = '\r\n'

# several instrument instances can share the same serialport
_SERIALPORTS = ['COM1','COM2','COM3','COM4','COM5']
_LATEST_READ_TIMES = {}

### default values
BAUDRATE = 9600

PARITY = serial.PARITY_NONE
BYTESIZE = 8
STOPBITS = 1
TIMEOUT = 0.05

# default value for port closure setting

CLOSE_PORT_AFTER_EACH_CALL = False

MODE_RTU = 'rtu'

class sensorInstrument(QtWidgets.QMainWindow,Ui_MainWindow):
    
    
    def __init__(self,port,slaveaddress,mode = MODE_RTU):
        
        self.instrument = minimalmodbus.Instrument('COM1',1)
        self.instrument.serial.baudrate = 9600
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity = serial.PARITY_NONE
        self.instrument.serial.stopbits = 1
        self.instrument.address = 1
        self.instrument.mode = minimalmodbus.MODE_RTU
        self.minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True 
               
        self.serial.open()
                
        # most often set by the constructor
        self.address = slaveaddress
        
        # can be mode_rtu or mode_ascii
        self.mode = MODE_RTU
        
        # set this to :const :'True' to print the communcation details. Defaults to :const "'False'
        self.debug = False
        
        # if this is : const 'True',the serial port will be closed after each call .
        #Defaults to :data:`CLOSE_PORT_AFTER_EACH_CALL`. To change it, set the value ``minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL=True`` ."""
        self.close_port_after_each_call =  minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True 
        
        # if this is const 'false',the serial port reads until timeout 
        #instead of just reading a specific number of bytes.Defaults to const'True'
        self.precalculate_read_size = True
        
        # Set to to :const:`True` if your RS-485 adaptor has local echo enabled. 
        #Then the transmitted message will immeadiately appear at the receive line of the RS-485 adaptor.
        # MinimalModbus will then read and discard this data, before reading the data from the slave.
        # Defaults to :const:`False`
        
        self.handle_local_echo = False
        
        def __repr__(self):
            """String representation of the :class:`.Instrument` object."""
            return "{}.{}<id=0x{:x}, address={}, mode={}, close_port_after_each_call={}, precalculate_read_size={}, debug={}, serial={}>".format(
                    self.__module__, self.__class__.__name__, id(self),
                    self.address, self.mode,self.close_port_after_each_call,self.precalculate_read_size,
                    self.debug,self.serial,)
            
        def get_illuminance(self):
            
            illuminance_data = []            
            illuminance_data = self.instrument.read_registers(40001,1,3,signed= False)
            
            print(illuminance_data)
         
                               
        def get_temperature(self):
            
            temperature_data  = []
            try:                  
                temperature_data =  self.instrument.read_registers(40002,2,3,signed= True)               
                print(temperature_data)
           # return temperature_data
            except IOError:
                print('Failed to read from instrument')
                
        def get_humidity(self):
            humidity_data = []
            humidity_data =  self.instrument.read_registers(40003,2,3,signed= False)
            
            print(humidity_data)
                  
    
        def close(self):
            if self.close_port_after_each_call:
                self.serial.close()
                
        
            