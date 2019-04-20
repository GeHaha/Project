# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 19:47:13 2019

@author: Gehaha
"""
import sys
# sys.path.append("D:\Project\sensor-software\data_base")
#sys.path.append(communcate)
from store_data import ManageData


import time
import matplotlib.pyplot as plt
import numpy


class DrawGraph():
    
    def __init__(self):
        self.draw_data = ManageData()
        
        self.draw()

       
    def draw(self):
        pass
    

    def __sava_data(self):
        data = self.draw_data.process_data
        print(data)
        
    
    
def test():
    draw_graph = DrawGraph()
    draw_graph.sava_data()
test()
   