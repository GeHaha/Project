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

from PyQt5.QtCore import QDate, QDateTime , QTime,Qt
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import logging
from parentWindow import parentWindow
from childWindow import childWindow
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s- %(message)s')


   

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

