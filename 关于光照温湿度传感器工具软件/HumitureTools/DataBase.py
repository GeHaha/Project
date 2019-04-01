# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:19:30 2019

@author: Gehaha
"""

import sqlite3

conn = sqlite3.connect('Temperature_Humidity.db')

c = conn.cursor()
c.execute(''' CREATE TABLE Temperature_Humidity
          (ID INT PRIMARY KEY     NOT NULL,
          ILLUMINANCE      INT    NOT NULL,
          TEMPERATURE      FLOAT  NOT NULL,
          HUMIDITY         FLOAT  NOT NULL,
          WINDSPEED        FLOAT  NOT NULL;''')

c.execute("INSERT INTO Temperature_Humidity(ID,ILLUMINANCE,TEMPERATURE,HUMIDITY,WINDSPEED)\
          VALUES()")
          
conn.commit()
conn.close()
