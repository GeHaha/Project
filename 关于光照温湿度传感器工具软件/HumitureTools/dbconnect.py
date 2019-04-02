# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:54:52 2019

@author: Gehaha
"""

import sqlite3
import communcate

class dbConnect:
    
    def __init__(self):
        self.conn = None
        self.cursor = None
        
    def connect(self):
        try:
            self.conn = sqlite3.connect("温湿度数据.db")
            self.cursor = self.conn.cursor()
            self.cursor.execute('''CREATE TABLE humiture
                                (Time        TEXT    NOT NULL,
                                Illuminance  INT    NOT NULL,
                                Temperature  FLOAT  NOT NULL,
                                Humidity     FLOAT  NOT NULL,
                                windspeed    FLOAT  NOT NULL);
                                ''')
            return self.cursor
        except Exception as e:
            print("连接失败！")
            
    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
   

    def insert(self,time,illuminance,temperature,humidity,windspeed):
        self.fetch_data = communcate.Communcate()
        self.fetch_illuminance = self.fetch_data.get_illuminance()        
        time = self.fetch_illuminance
        
        
        self.cursor = self.conn.connect()
        sql = "INSERT INRO humiture (Time,Illuminance,Temperature,Humidity,Windspeed)\
        VALUES(time,illuminance,temperature,humidity,windspeed)"
        self.cursor.execute(sql)
        

    def fetch(self):

        self.cursor = self.conn.connect()
        sql = "SELECT time,illuminance,temperature,humidity,windspeed FROM humiture"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.conn.close()
        return result     