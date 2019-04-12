# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 14:07:33 2019

@author: Gehaha
"""
import sys

sys.path.append("../communcate")
from communcate import Communcate

sys.path.append("D:\Project\sensor-software\data_base")
from store_data import ManageData


def test():  
    sensorCommuncate = Communcate()
    sensorCommuncate.open_port()
    sensorCommuncate.set_modbus_config(0x01, 'rtu', 0x03)    
    data = ManageData()
    # get the data twice
    number = 2
    while (number):
        number = number - 1
        sensorCommuncate.request_data()
        sensorCommuncate.print_data()
        print("--------------")
        data.process_data()
        data.insert_data()
        data.select_all_data()
        print("~~~~~~~~~~~~~~~")
test()    

    
    