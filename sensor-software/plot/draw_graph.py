# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 19:47:13 2019

@author: Gehaha
"""
import sys
sys.path.append("data_base")
#sys.path.append(communcate)

import time
import matplotlib

from data_pack import DataPack


class DrawGraph():
    
    def __init__(self,name):
        self.__name = name
        
        self.package = DataPack("draw_graph")
       
    def draw(self):
        pass
    

    def __sava_data(self):       
        data_list = []
        data_list[0] = self.time.strftime("%Y/%m/%d %H:%M:%S",time.localtime())
        data_list[1] = self.package.illuminance()
        data_list[2] = self.package.temperature()
        data_list[3] = self.package.humidity()
        data_list[3] = self.package.windspeed()

        return data_list
    
        
    def print_list(self,data):
        
        print(self.__sava_data)
                

    def __delet_data(self):
        pass
        
    def fetch_data(self):
        pass
    
    
def test():
    draw_graph = DrawGraph("draw_graph")
    draw_graph.sava_data()
test()
   