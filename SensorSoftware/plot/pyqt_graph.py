# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 14:29:50 2019

@author: 86157
"""

import sys
sys.path.append("D:\Project\sensor-software\data_base")

import pyqtgraph as pg

#sys.path.append(communcate)
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib import style
import pyqtgraph as pg
style.use("ggplot")

import matplotlib
from data_base.data_base_helper  import DataBaseHelper

class DrawGraph(object):   
    def __init__(self):       
        # initial the plot variable
        self.timestampValue = []
        self.illuminanceValue = []
        self.temperatureValue = []
        self.humidityValue = []
        self.windspeedValue = []
     
        # initial the figure
        global fig
        fig = plt.figure(figsize = (60,8),dpi = 80,facecolor = "white")
        fig.subplots_adjust(left = 0.06,right = 0.70)
        self.actualValueGraph = fig.add_subplot(2,1,1)
        self.actualValueGraph.set_xlabel("Datetime")
        self.actualValueGraph.set_ylabel("Value")
        self.actualValueGraph.set_title("Humiture") 
#        self.actualValueGraph.xticks(rotation = 70)
        self.actualValueGraph.legend(loc = "upper right",frameon = False)
        plt.xticks(rotation = 90,fontsize = 5)
#        loc = plticker.MultipleLocator(base=1.0) # this locator puts ticks at regular intervals
#        self.actualValueGraph.xaxis.set_major_locator(loc)
     
        for label in self.actualValueGraph.get_xticklabels(): 
            label.set_visible(False) 
        for label in self.actualValueGraph.get_xticklabels()[::2]: 
            label.set_visible(True)
        plt.ion()
        
        
    def plot_line(self,values):
        # update the plot value of the graph
        self.timestampValue = [i[0] for i in values]
        self.illuminanceValue = [i[1] for i in values]
        self.temperatureValue = [i[2] for i in values]
        self.humidityValue = [i[3] for i in values]
        self.windspeedValue = [i[4] for i in values]
        print(self.timestampValue)
        
        self.illuminanceLine, = self.actualValueGraph.plot(self.timestampValue,self.illuminanceValue,
                                                           color = "red",linewidth = 0.5,label = " illuminance")
        self.temperatureLine, = self.actualValueGraph.plot(self.timestampValue,self.temperatureValue,
                                                           color = "blue",linewidth = 0.5,label = "temperature")
        self.humidityLine, = self.actualValueGraph.plot(self.timestampValue,self.humidityValue,
                                                        color = "green",linewidth = 0.5,label = "humidity")
        self.windspeedLine, = self.actualValueGraph.plot(self.timestampValue,self.windspeedValue,
                                                         color = "yellow",linewidth = 0.5,label = "windspeed")       
        self.actualValueGraph.legend(loc = "upper right",frameon = False)
        
        plt.draw()
        plt.show()
        plt.ioff()
        
        
    #define the output method
    def close(self):
        plt.ioff()