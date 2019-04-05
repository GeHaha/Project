# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:36:37 2019

@author: Gehaha
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("温湿度-曲线变化图")
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        
        self.stock_code = QtWidgets.QLineEdit()
        self.option_sel = QtWidgets.QComboBox()
        self.option_sel.addItem("近7天")
        self.option_sel.addItem("近30天")
        self.option_sel.addItem("近60天")
        self.option_sel.addItem("近180天")
        self.option_sel.addItem("近360天")
        self.que_btn = QtWidgets.QPushButton("查询")
        self.k_widget = QtWidgets.QWidget()
        self.k_layout = QtWidgets.QGridLayout()
        self.k_plt = pg.PlotWidget()
        self.k_layout.addWidget(self.k_plt)
        
        #将上述部件添加到布局中
        self.main_layout.addWidget(self.stock_code,0,0,1,1 )
        self.main_layout.addWidget(self.option_sel,0,1,1,1)
        self.main_layout.addWidget(self.que_btn,0,2,1,1)
        self.main_layout.addWidget(self.k_widget,1,0,3,3)
        
        
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainUi()
    ui.show()
    sys.exit(app.exec_())
         
