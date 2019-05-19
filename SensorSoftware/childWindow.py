# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 20:48:46 2019

@author: Gehaha
"""
import sys
# sys.path.append("communcate")
sys.path.append("ui")
sys.path.append("data_base")
sys.path.append("plot")

from PyQt5.QtCore import QDate,   QDateTime , QTime,Qt
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from plot_ui import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import serial.tools.list_ports
from ui import Ui_MainWindow 
from draw_graph import DrawGraph
from data_holder import DataHolder
from data_base_helper import DataBaseHelper
from communcate import Communcate
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s- %(message)s')

#画图窗口
class childWindow(QWidget,Ui_Form):    
    def __init__(self):
        super(childWindow, self).__init__()
        QWidget.__init__(self)  
        
        self.__db_get = DataBaseHelper()
        self.graph = DrawGraph()
        self.setupUi(self)        
        self.que_pushButton.clicked.connect(self.plot_histroy_data)

              
    def set_button(self):
        self.que_pushButton.setEnabled(True)
        self.que_pushButton.setText("查询")
        
    def read_start_time(self):
        start_time = self.start_dateTimeEdit.dateTime()
        #将时间2000-01-01T00:00:00 转换成2000-01-01 00 :00:00
        start_time = start_time.toString(Qt.ISODate)
        start_time = start_time.replace('T','')
        return start_time
    
    def read_end_time(self):
       end_time = self.end_dateTimeEdit.dateTime()
       end_time = end_time.toString(Qt.ISODate)
       end_time = end_time.replace('T','')
       return end_time


    def plot_histroy_data(self):
        self.que_pushButton.setEnabled(False)
        self.que_pushButton.setText("查询中")
        startdate = self.read_start_time()
        enddate = self.read_end_time()
        values = self.__db_get.select_any_time(startdate,enddate)
        self.graph.plot_line(values)
        self.set_button()
        
        
#    def plot_histroy_data(self):
#        self.que_pushButton.setEnabled(False)
#        self.que_pushButton.setText("查询中")
#        self.select_time()
#        self.set_button()
#        
#    def select_time(self):
#        if self.time_comboBox.currentIndex() == 0:
#            values = self.__db_get.select_one_hour() 
#            self.graph.plot_line(values)
#            self.set_button()
#           
#        if self.time_comboBox.currentIndex() == 1:           
#            values = self.__db_get.select_three_hour() 
#            self.graph.plot_line(values)
#            self.set_button()
#            
#        if self.time_comboBox.currentIndex() == 2:
#            self.set_button()
#            values = self.__db_get.select_six_hours() 
#            self.graph.plot_line(values)
#            
#        elif self.time_comboBox.currentIndex() == 3:
#            values = self.__db_get.select_one_day()
#            self.graph.plot_line(values)
#            self.set_button()
#            
#        elif self.time_comboBox.currentIndex() == 4:
#            self.set_button()
#            values = self.__db_get.select_three_days()
#            self.graph.plot_line(values)
#            
#        elif self.time_comboBox.currentIndex() == 5:
#            self.set_button()
#            values = self.__db_get.select_senven_days()
#            self.graph.plot_line(values)           
#            
#        elif self.time_comboBox.currentIndex()== 6:
#            self.set_button()
#            values = self.__db_get.select_fifteen_days()
#            self.graph.plot_line(values)
#                     
#        elif self.time_comboBox.currentIndex()== 7:
#           self.set_button()
#           values = self.__db_get.select_one_month()
#           self.graph.plot_line(values)
#                     
#        elif self.time_comboBox.currentIndex()== 8:
#            self.__db_get.select_three_month()
#            self.set_button()
#            
#        elif self.time_comboBox.currentIndex() == 9:
#            self.set_button()
#            values = self.__db_get.select_six_month()
#            self.graph.plot_line(values)
#                       
#        elif self.time_comboBox.currentIndex()== 10:
#            self.set_button()
#            values = self.__db_get.select_one_year()
#            self.graph.plot_line(values)
#        
#        