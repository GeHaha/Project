# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:46:25 2019

@author: Gehaha
"""
import crcmod
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
        
        # 串口在每次调用后关闭。
        self.instrument.close_port_after_each_call = True
        
    
    """   
    #使用_communication()方法。
    #使用_embedPayload()函数生成请求，
    #使用_extractPayload()函数完成响应的解析。
    """ 
         
    # 发送到pySerial和从pySerial发送的信息应该是字节类型的
    def slaveCommunicate(self):
        # request,number_of_bytes_read
        #要发送给从服务器的原始请求。request
        # recieve_data 从slave即设备发回来的数据
        request = request_data        
        try:    
            raw_data = self.instrument._communicate(request,number_of_bytes_to_read)    
         #   return recieve_data
         #注意答案可能有奇怪的ASCII控制符号，这使得很难在print中打印它(有点混乱)。
         # 使用repr()使字符串可打印(显示控制符号的ASCII值)。
            print(repr(recieve_data))
            return raw_data
        
        except ValueError :
           pass
           
    #构建一个请求命令从地址、功能码、和数据
    def slaveEmbedPayload(self):
        # 从slaveaddress、功能号和有效负载数据构建一个请求
        slaveaddress = 0x01
        mode = MODE_RTU
        functioncode = 0x03
        #要发送到从服务器的字节字符串
        payloaddata = '\x01\x03\x00\x00\x00\x04\x44\x09'
        request_data = mininmalmodbus._embedPayload(slaveaddress,mode,functioncode,paylaoddata)        
        return request_data
    
    #从响应中提取有效数据部分
    def extractPayload(self):        
        #来自于相应的原始字符串        
        response = raw_data
        slaveaddress = 0x01
        mode = MODE_RTU
        functioncode = 0x03
        
        #响应字符串的有效负载部分,接收到的响应格式应该是:* 
        #RTU模式:slaveaddress byte + functioncode byte + payloaddata + CRC(两个字节)
        try:            
            payload_data = mininmalmodbus._extractPayload(response,slaveaddress,mode,functioncode)
            return payload_data
        
        except ValueError:
            print('there is any problem with received address,functioncode,crc')
     
        
     #执行带有功能码的的命令。
    def performCommand(self):
        functioncode = 0x03
        # 要传输给slave的数据(将嵌入slaveaddress、CRC等),是字符串
        payloadToSlave(str) = '\x01\x03\x00\x00\x00\x04'
        
        extracted_data = self.instrument._performCommand(functioncode,payloadToSlave)
        #从slave(字符串)提取的数据有效负载。它已被删除CRC等。
        return extracted_data            
    
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
    
    
  
    
    def get_illuminance(self):
        return self.read_register(40001,numberOfDecimals = 0,functioncode= 0x03,signed=False)
    
    
    
    def get_temperature(self):
        return self.read_register(40002,numberOfDecimals = 2,functioncode= 0x03,signed=False)
    
    
    def get_humidity(self):
        return self.read_register(4003,numberOfDecimals = 2,functioncode= 0x03,signed=False)
    
        
    def get_windspeed(self):
        return self.read_register(40004,numberOfDecimals = 2,functioncode= 0x03,signed=False)
    
    
    def CalcuCrc(self):       
        #input string 是接收到的数据(不包含crc),
        #return 一个双字节CRC字符串，低位的字节在前。       
        inputstring = ''
        calCRC_string =  minimalmodbus._calculateCrcString(inputstring)
        return calCRC_string
    
    
    def portClose(self):
        pass
    
    
    
    def read_stop(self):
        pass
    
    
    def single(self):
        pass
    
    
    
    def loop(self):
        pass
        
    
        
    

   