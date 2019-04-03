# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:19:30 2019

@author: Gehaha
"""

import sqlite3
import time

conn= sqlite3.connect('Temperature_Humidity.db')
cursor = conn.cursor()

class dbConnect():
      
    def __init__(self,local_time,illuminance,temperature,humidity,windspeed):
        super(DataBase,self).__init__()
        
        self.time = local_time
        self.illuminance,self.temperature = illuminance,temperature
        self.humidity,self.windspeed = humidity,windspeed
        
    """
    def connect(self):
        conn = sqlite3.connect('Temperature_Humidity.db')
        print('打开数据库成功！')
    """
    def create():        
       # cursor = conn.cursor()
        cursor.execute(''' CREATE TABLE temperature_humidity
                  local_time         str   NOT NULL,
                  illuminance  int   NOT NULL,
                  temperature  float NOT NULL,
                  humidity     float NOT NULL,
                  windspeed    float NOT NULL ''' )
        print('创建数据表成功！')
        
    def write(self):
        self.illuminance = 1234
        self.temperature = 23.8
        self.humidity = 23.5
        self.windspeed = 0.00
        cursor = conn.cursor()    
        self.local_time = time.strftime("%Y/%m/%d %H:%M:%S",time.localtime())
        
        cursor.execute("INSERT INTO temperature_humidity(local_time,illuminance,temperature,humidity,windspeed) \
                       VALUES(self.local_time,self.illuminance,self.temperature,self.humidity,self.windspeed)")  
        print("写入数据库成功！")
        
        #关闭cursor
        cursor.close()
        #提交事务
        conn.commit()
        #关闭连接
        conn.close()
        cursor.
    def read():
        get_cursor = cursor.execute("SELECT time,illuminance,temperature,humidity,windspeed from temperature_humidity")
        for row in get_cursor:
            print("time:",row[0])
            print("illuminance:",row[1])
            print("temperature:",row[2])
            print("humidity:",row[3])
            print("windspeed:",row[4])
        
        cursor.close()        
        conn.close()
        
    def update():
        pass
    