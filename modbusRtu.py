# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 21:32:31 2019

@author: Gehaha
"""

import serial 
import struct
import sys
import time
import mininmalmodbus



BAUDRATE = 9600

PARITY = serial.PARITY_NONE
BYTESIZE = 8
STOPBITS = 1
TIMEOUT = 0.05
