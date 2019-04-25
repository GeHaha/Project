# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:08:58 2018

@author: Gehaha
"""
import sys
# sys.path.append("communcate")
sys.path.append("ui")
sys.path.append("data_base")
sys.path.append("plot")


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

# sys.path.append("D:\Project\sensor-software\plot")


# TODO the name is too bad
#class SignalUi(QtWidgets.QMainWindow, Ui_MainWindow):
class parentWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):

        super(parentWindow, self).__init__()
        self.setupUi(self)

        self.__sensorCommuncate = Communcate()
        self.__sensorCommuncate.set_modbus_config(0x01, 'rtu', 0x03)
        self.__dataHolder = DataHolder("modbus sensor")
        self.__db_helper = DataBaseHelper()
        self.graph = DrawGraph()
        
        self.__timer = QTimer(self)
        self.__timer.timeout.connect(self.single)

        self.Open_pushButton.clicked.connect(self.port_open)
        self.Close_pushButton.clicked.connect(self.port_close)
        self.Signal_pushButton.clicked.connect(self.single)
        self.Circle_pushButton.clicked.connect(self.circle)
        self.Stop_pushButton.clicked.connect(self.stop_read)


    def port_open(self):
        if self.__sensorCommuncate.open_port():
            self.Show_label.setText("Open port success!")
        else: 
            self.Show_label.setText("Open port failed!")

    def port_close(self):
        self.__sensorCommuncate.close_port()

    def single(self):
        data = self.__sensorCommuncate.request_data()
        self.__dataHolder.set_data(data)
        self.__db_helper.insert_data("humiture", self.__dataHolder) 
        self.__show_data() 
    
    def circle(self):
        self.__timer.start(15000)

            
    def stop_read(self):
        self.__sensorCommuncate.pause()
        self.__timer.stop()
        self.__clear_data()


    def __clear_data(self):
        self.illumation_lineEdit.clear()
        self.Temp_lineEdit.clear()
        self.Humidity_lineEdit.clear()
        self.Airspped_lineEdit.clear()
        
        
    def __show_data(self):
        self.illumation_lineEdit.setText(str(self.__dataHolder.illuminance()))
        self.Temp_lineEdit.setText(str(self.__dataHolder.temperature()))
        self.Humidity_lineEdit.setText(str(self.__dataHolder.humidity()))
        self.Airspped_lineEdit.setText(str(self.__dataHolder.windspeed()))


#画图窗口
class childWindow(QWidget,Ui_Form):
    
    def __init__(self):
        super(childWindow, self).__init__()
        QWidget.__init__(self)  
        self.__db_get = DataBaseHelper()
        self.graph = DrawGraph()
        self.setupUi(self)        
        self.que_pushButton.clicked.connect(self.plot_histroy_data)
        self.stop_pushButton.clicked.connect(self.stop_draw)
        
    def set_button(self):
        self.que_pushButton.setEnabled(True)
        self.que_pushButton.setText("查询")
        
    def plot_histroy_data(self):
        self.que_pushButton.setEnabled(False)
        self.que_pushButton.setText("查询中")
        self.select_time()

       
    def select_time(self):
            
        if self.time_comboBox.currentIndex() == 0:
            self.set_button()
            values = self.__db_get.six_hours_data() 
            self.graph.plot_line(values)
            
        elif self.time_comboBox.currentIndex() == 1:
            self.set_button()
            values = self.__db_get.one_day_data()
            self.graph.plot_line(values)

            
        elif self.time_comboBox.currentIndex() == 2:
            self.set_button()
            values = self.__db_get.three_days_data()
            self.graph.plot_line()

            
        elif self.time_comboBox.currentIndex() == 3:
            self.set_button()
            values = self.__db_get.senven_days_data()
            self.graph.plot_line()
            
            
        elif self.time_comboBox.currentIndex()== 4:
            self.set_button()
            values = self.__db_get.fifteen_days_data()
            self.graph.plot_line()
            
            
        elif self.time_comboBox.currentIndex()== 5:
           self.set_button()
           values = self.__db_get.one_month_data()
           self.graph.plot_line(values)
           
           
        elif self.time_comboBox.currentIndex()== 6:
            self.__db_get.three_month_data()
            self.set_button()
            
        elif self.time_comboBox.currentIndex() == 7:
            self.set_button()
            values = self.__db_get.six_month_data()
            self.graph.plot_line(values)
            
            
        elif self.time_comboBox.currentIndex()== 8:
            self.set_button()
            values = self.__db_get.one_year_data()
            self.graph.plot_line(values)
        
        
    def stop_draw(self):
        pass
    
   

def main():
    app=QtWidgets.QApplication(sys.argv)
    window = parentWindow()
    child = childWindow()    
    plt_btn = window.curve_pushButton
    plt_btn.clicked.connect(child.show)      
    window.show()
    sys.exit(app.exec_())   

if __name__ == '__main__':
    main()

