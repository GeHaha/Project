# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 19:47:13 2019

@author: Gehaha
"""
import sys
sys.path.append("D:\Project\sensor-software\data_base")

#sys.path.append(communcate)


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib import style
style.use("ggplot")

import matplotlib
from data_base.data_base_helper  import DataBaseHelper

import os
import csv
import datetime
from matplotlib.animation import FuncAnimation
from matplotlib.dates import DateFormatter
import matplotlib.ticker as ticker
import matplotlib.animation as animation


class DrawGraph(object):
    
    def __init__(self):
        # Trun matplotlib interactive mode on
        plt.ion()        
        # initial the plot variable
        self.timestampValue = []
        self.illuminanceValue = []
        self.temperatureValue = []
        self.humidityValue = []
        self.windspeedValue = []
        
#        self.illuminanceValueRange = [0,1]
#        self.humidityValueRange = [0,1]
#        self.temperatureValueRange = [0,1]
#        self.windspeedValueRange = [0,1]
        self.timestampValueRange = [0,1]
        
        
        # initial the figure
        global fig
        fig = plt.figure(figsize = (12,8),dpi = 80,facecolor = "white")
        fig.subplots_adjust(left = 0.06,right = 0.70)
        self.actualValueGraph = fig.add_subplot(2,1,1)
#        self.actualValueGraph.xticks(rotation = 70)
        
        plt.ion()
        
        
    def update_data(self,values):
        timestamp = values[0][0]   
        illuminance = values[0][1]
        temperature = values[0][2]      
        humidity = values[0][3]
        windspeed = values[0][4]
        
        # update the plot value of the graph
        self.timestampValue.append(timestamp)
        self.illuminanceValue.append(illuminance)
        self.temperatureValue.append(temperature)
        self.humidityValue.append(humidity)
        self.windspeedValue.append(windspeed)
    
        #update the x/y axis limits
#        self.actualValueGraph.set_xlim(self.timestampValueRange[1] - datetime.timedelta(days = 1),
#                                      self.timestampValueRange[1])
        
        # update the four lines of the actualValueGraph
#        self.illuminanceLine.set_ydata(self.timestampValue)
#        self.humidityLine.set_ydata(self.humidityValue)
#        self.temperatureLine.set_ydata(self.temperatureValue)
#        self.windspeedLine.set_ydata(self.windspeedValue)
#        
#        plt.pause(0.001)
#        self.actualValueGrapht.draw()
        
    
    def init_plot(self):
        
        self.actualValueGraph.legend(loc = "upper right",frameon = False)
        self.actualValueGraph.grid(True)
        #set the title  x/y label of the graph
        self.actualValueGraph.set_xlabel("Datetime")
        self.actualValueGraph.set_ylabel("Value")
        self.actualValueGraph.set_title("Humiture")
#        self.actualValueGraph.set_xticks(rotation = 90)
#        
             
        # init four lines of the actualValueGraph
        self.illuminanceLine, = self.actualValueGraph.plot(self.timestampValue,self.illuminanceValue,
                                                           color = "red",linewidth = 0.5,label = " illuminance")
        self.temperatureLine, = self.actualValueGraph.plot(self.timestampValue,self.temperatureValue,
                                                           color = "blue",linewidth = 0.5,label = "temperature")
        self.humidityLine, = self.actualValueGraph.plot(self.timestampValue,self.humidityValue,
                                                        color = "green",linewidth = 0.5,label = "humidity")
        self.windspeedLine, = self.actualValueGraph.plot(self.timestampValue,self.windspeedValue,
                                                         color = "yellow",linewidth = 0.5,label = "windspeed")       

#        self.actualValueGraph.draw() 
        plt.draw()
        
    #define the output method
    def close(self):
        plt.ioff()
        plt.show()
        