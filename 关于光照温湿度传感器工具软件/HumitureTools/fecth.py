# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:04:50 2019

@author: Gehaha
"""

import dbconnect
import communcate

def insert(self,time,illuminance,temperature,humidity,windspeed):
    self.m = communcate.Communcate()
    
    
    self.conn = dbconnect.dbConnect()
    self.cursor = self.conn.connect()
    sql = "INSERT INRO humiture (time,illuminance,temperature,humidity,windspeed)\
    VALUES()"
    

def fetch(self):
    self.conn = dbconnect.dbConnect()
    self.cursor = self.conn.connect()
    sql = "SELECT time,illuminance,temperature,humidity,windspeed FROM humiture"
    self.cursor.execute(sql)
    result = self.cursor.fetchall()
    self.conn.close()
    return result

    