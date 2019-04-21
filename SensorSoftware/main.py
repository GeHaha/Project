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
class SignalUi(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):

        super(SignalUi, self).__init__()
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
        self.curve_pushButton.clicked.connect(self.drawing)

        # self.Curve_pushButton.clicked.connect(self.)

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
        values = self.__db_helper.select_data()
        self.graph.update_data(values)
        self.graph.init_plot()   
        
        
        
        self.__show_data()
    
    
    def circle(self):
        self.__timer.start(5000)
#        values = self.__db_helper.select_data()
#        self.graph.get_data(values)
#        self.graph.draw_plot()
#        
        
        
    def stop_read(self):
        self.__sensorCommuncate.pause()
        self.__timer.stop()
        self.__clear_data()

    def drawing(self):
        pass
    
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


def main():
    app = QtWidgets.QApplication(sys.argv)
   # MainWindow = QtWidgets.QMainWindow()
    ui = SignalUi()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
