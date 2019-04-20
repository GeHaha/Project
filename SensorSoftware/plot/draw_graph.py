# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 19:47:13 2019

@author: Gehaha
"""
import sys
sys.path.append("D:\Project\sensor-software\data_base")

#sys.path.append(communcate)


import time
import matplotlib.pyplot as plt
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
        
#        self.__get_data = DataBaseHelper()
        # Trun matplotlib interactive mode on
        plt.ion()
        
        # initial the plot variable
        self.timestampValue = []
        self.illuminanceValue = []
        self.temperatureValue = []
        self.humidityValue = []
        self.windspeedValue = []
        
                       
        # initial the figure
        global fig
        fig = plt.figure(figsize = (18,8),facecolor = "white")
        fig.subplots_adjust(left = 0.06,right = 0.70)
        self.actualValueGraph = fig.add_subplot(2,1,1)
#        self.actualValueGraph.xticks(rotation = 70)
        
    def draw_plot(self):
        # 传入参数
        self.process_data = DataBaseHelper()
        values = self.process_data.select_data()
        
        # handle time data
        timestamp = values[0][0]
        
        # handle illuminance data        
        illuminance = values[0][1]

        # handle temperature data
        temperature = values[0][2]
      
        # handle humidity data        
        humidity = values[0][3]
        
        # handle windspeed data
        windspeed = values[0][4]

        
        #update the plot value of the graph
        self.timestampValue.append(timestamp)
        self.illuminanceValue.append(illuminance)
        self.temperatureValue.append(temperature)
        self.humidityValue.append(humidity)
        self.windspeedValue.append(windspeed)
        
        
        # init four lines of the actualValueGraph
        self.illuminanceLine, = self.actualValueGraph.plot(self.timestampValue,self.illuminanceValue,'ro',
                                                                color = "red",label = " illuminance")
        self.temperatureLine, = self.actualValueGraph.plot(self.timestampValue,self.temperatureValue,'ro',
                                                                color = "blue",label = "temperature")
        self.humidityLine, = self.actualValueGraph.plot(self.timestampValue,self.humidityValue,'ro',
                                                             color = "green",label = "humidity")
        self.windspeedLine, = self.actualValueGraph.plot(self.timestampValue,self.windspeedValue,'ro',
                                                              color = "yellow",label = "windspeed")
        
        self.actualValueGraph.legend(loc = "upper right",frameon = False)
        self.actualValueGraph.grid(True)
        
        # set the title  x/y label of the graph
        self.actualValueGraph.set_xlabel("Datetime")
        self.actualValueGraph.set_ylabel("Value")
        self.actualValueGraph.set_title("Humiture")

        plt.legend()
        plt.pause(0.0001)
        plt.draw()
                
                   
    #define the output method
    def close(self):
        plt.ioff()
        plt.show()
        

            
    
