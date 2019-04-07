# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:54:52 2019

@author: Gehaha
"""

import sys
sys.path.append("communcate")

import sqlite3
from communcate import Communcate

class dbConnect:
    
    def __init__(self,i,t,h,w):
        self.illuminance = i
        self.temperature = t
        self.humidity = h
        self.windspeed = w
        
        self.conn = None
        self.cursor = None
        
    def connect(self):
        try:
            self.conn = sqlite3.connect("温湿度数据.db")
            self.cursor = self.conn.cursor()
            self.cursor.execute('''CREATE TABLE humiture
                                (Time        TEXT    NOT NULL,
                                Illuminance  INTEGER   NOT NULL,
                                Temperature  REAL  NOT NULL,
                                Humidity     REAL  NOT NULL,
                                windspeed    REAL  NOT NULL);
                                ''')
            return self.cursor
        except Exception as e:
            print("连接失败！")
            
    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
   
    
    def dataInsertDb(self):
        self.fetch_data = Communcate.Communcate()
        self.fetch_illuminance = self.fetch_data.get_illuminance()        
        self.illuminance = self.fetch_illuminance
        
        self.fetch_temperature = self.fetch_data.get_temperature()
        self.temperature = self.fetch_temperature
        
        self.fetch_humidity = self.fetch_data.get_humidity()
        self.humidity = self.fetch_humidity
        
        self.fetch_windspeed = self.fetch_data.get_windspeed()
        self.windspeed = self.fetch_windspeed
        
        return self.illuminance,self.temperature,self.humidity,self.windspeed
    
    
    
    def insert(self,time,illuminance,temperature,humidity,windspeed):
        self.data = self.dataInsertDb()
        self.illuminance = self.data[0]
        self.temperature = self.data[1]
        self.humidity = self.data[2]
        self.windspeed = self.data[3]
         
                
        self.cursor = self.conn.connect()
        sql = "INSERT INRO humiture (Time,Illuminance,Temperature,Humidity,Windspeed)\
        VALUES(time,self.illuminance,self.temperature,self.humidity,self.windspeed)"
        
        self.cursor.execute(sql)
        

    def fetch(self):

        self.cursor = self.conn.connect()
        sql = "SELECT time,illuminance,temperature,humidity,windspeed FROM humiture"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.conn.close()
        return result     