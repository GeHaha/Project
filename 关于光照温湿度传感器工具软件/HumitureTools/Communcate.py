# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:46:25 2019

@author: Gehaha
"""
import crcmod
import minimalmodbus
import serial
from Ui import Ui_MainWindow
from PyQt5 import QtCore,QtGui,QtWidgets
import time

class Communcate(QtWidgets.QMainWindow,Ui_MainWindow):
    

    
    
    def __init__(self):
        super(Communcate,self).__init__()

        
        minimalmodbus.Instrument.__init__(self,'COM4',1)
        
        self.instrument = minimalmodbus.Instrument('COM4',1)
        self.instrument.serial.baudrate = 9600
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
        self.instrument.serial.stopbits = 1
        self.instrument.serial.timeout = 2
        self.instrument.debug = True
        
        # 串口在每次调用后关闭。
       # self.instrument.close_port_after_each_call = False
        
        
        #如果您的RS-485适配器启用了本地echo，则将其设置为True。
        #然后发送的消息将立即出现在RS-485适配器的接收行。
        #然后MinimalModbus将在从从属节点读取数据之前读取并丢弃这些数据。默认为False
        self.instrument.handle_local_echo =False
        
        
        
        
        #如果这是假的，串行端口将读取到超时，而不是只读取特定的字节数。默认值为True。
        self.instrument.precalculate_read_size = True
        
        """        
        self.request_data = ''
        self.send_data = ''
        self.raw_data = ''
        self.hex_data = ''
        """
        
    
    """   
    #使用_communication()方法。
    #使用_embedPayload()函数生成请求，
    #使用_extractPayload()函数完成响应的解析。
    """ 
         
           
    #构建一个请求命令从地址、功能码、和数据
    def slaveEmbedPayload(self):
        
        self.request_data = ''
        # 从slaveaddress、功能号和有效负载数据构建一个请求
        slaveaddress = 0x01
        mode = 'rtu'
        functioncode = 0x03
        #要发送到从服务器的字节字符串
        payloaddata = '\x00\x00\x00\x04'
        #self.request_data = minimalmodbus._embedPayload(slaveaddress,mode,functioncode,payloaddata)        
        #return self.request_data
        self.request_data =  minimalmodbus._embedPayload(slaveaddress,mode,functioncode,payloaddata)
        return self.request_data
    
    
    # 发送到pySerial和从pySerial发送的信息应该是字节类型的
    def slaveCommunicate(self):
        # request,number_of_bytes_read
        #要发送给从服务器的原始请求。request
        # recieve_data 从slave即设备发回来的数据
        self.raw_data = ''
        self.send_data= self.slaveEmbedPayload()
        
        #self.send_data = Communcate.slaveEmbedPayload()
        
      #  number_of_bytes_to_read = 13
        
        try:    
            self.raw_data = self.instrument._communicate(self.send_data,13)    
         #   return recieve_data
         #注意答案可能有奇怪的ASCII控制符号，这使得很难在print中打印它(有点混乱)。
         # 使用repr()使字符串可打印(显示控制符号的ASCII值)。
            if self.raw_data[0] == '\x01':
                #return self.raw_data
                return self.raw_data
                
            else:
                return self.slaveCommunicate()
            
                                 
        except ValueError :
           pass
   
        
    def get_illuminance(self):
        
       # self.illuminance_bytestring= self.hex_data[9:14]
       
        self.receive_data = self.slaveCommunicate()       
        #self.illuminance_bytestring = self.receive_data[3:5]
        self.illuminance_bytestring = self.receive_data
        #将一个双字节字符串转换为一个数值，可能会缩放它
        self.illuminance_data =  minimalmodbus._twoByteStringToNum(self.illuminance_bytestring[3:5],
                                                 numberOfDecimals = 0,signed = False)
        #return self.illuminance_data
       # self.illumation_lineEdit.setText(self.illuminance_data)
        print("illuminance:",self.illuminance_data)
        
       
    def get_temperature(self):
        self.receive_data = self.slaveCommunicate()
        #self.temperature_bytestring = self.receive_data[5:7]
        self.temperature_bytestring = self.receive_data
        self.temperature_data = minimalmodbus._twoByteStringToNum(self.illuminance_bytestring[5:7],
                                                 numberOfDecimals = 2,signed = False)
        #self.Temp_lineEdit.setText(self.temperature_data)
        print("temperature:",self.temperature_data)
        
        
    
    
    def get_humidity(self):
        self.receive_data = self.slaveCommunicate()
        #self.humidity_bytestring = self.receive_data[7:9]  
        self.humidity_bytestring = self.receive_data
        self.humidity_data = minimalmodbus._twoByteStringToNum(self.humidity_bytestring[7:9],
                                                 numberOfDecimals = 2,signed = False)
        
       # self.Humidity_lineEdit.setText(self.humidity_data)
        print("humidity:",self.humidity_data) 
        
    def get_windspeed(self):
        self.receive_data = self.slaveCommunicate()
       # self.windspeed_bytestring = self.receive_data[9:11]
        self.windspeed_bytestring = self.receive_data
        self.windspeed_data = minimalmodbus._twoByteStringToNum(self.windspeed_bytestring[9:11],
                                                 numberOfDecimals = 0,signed = False)
      
        #self.Airspped_lineEdit.setText(self.windspeed_data)
        print("windspeed_data:" ,self.windspeed_data)
        
    
    def close(self):
        self.instrument.serial.close()
    
    
    def send(self):
        self.slaveEmbedPayload() 
        
        
    def read_stop(self):
        self.instrument.serial.cancel_read()
        
    def read_data(self):
        self.get_illuminance()
        self.illumation_lineEdit.setText(self.illuminance_data)
        self.get_humidity()
        self.Humidity_lineEdit.setText(self.humidity_data)
        self.get_temperature()
        self.Temp_lineEdit(self.temperature_data)
        self.get_windspeed()
        self.Airspped_lineEdit(self.windspeed_data)
        

    
    

    

        
    

   