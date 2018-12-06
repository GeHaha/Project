# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:08:58 2018

@author: Gehaha
"""
DeviceId = [0X01]
FunctionCode =[0X03]
StartId= [0x00,0x00]
DataLen = [0x00,0x04]
CheckCrc= [0x44,0x09]

SerialPackage = [DeviceId,FunctionCode,StartId,DataLen,CheckCrc]  
  