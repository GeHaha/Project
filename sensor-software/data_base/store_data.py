# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:28:25 2019

@author: Gehaha
"""
import sys
sys.path.append("D:\Project\sensor-software\communcate")

from communcate import Communcate

#from communcate.data_pack import DataPack
from data_pack import DataPack


import sqlite3
import time


from create_table import  SetupDB



class ManageData(object):
#    db_name = "humiture.db"
#    table_name = "Humiture"   
    def __init__(self):
           
        self.get_data = DataPack()
        self.setup = SetupDB()
        self.setup.db_connect()
        self.setup.create_tables()
           
        self.connection = sqlite3.connect("humiture.db",check_same_thread = False)
        self.cursor = self.connection.cursor()
#        self.insert_data()   
        
        
               
    def process_data(self):
        self.get_data = DataPack()      
        self.receive_data = []
        self.receive_data.insert(0,self.get_data.illuminance())
        self.receive_data.insert(1,self.get_data.temperature())
        self.receive_data.insert(2,self.get_data.humidity())
        self.receive_data.insert(3,self.get_data.windspeed())
        print(type(self.receive_data[0]))
        print(type(self.receive_data[1]))
        print(type(self.receive_data[2]))
        print(type(self.receive_data[3]))
        print(type(time.strftime("%Y/%m/%d %H:%M:%S",time.localtime())))
        print(self.receive_data)
        return self.receive_data
  

      
    def insert_data(self):  
        # insert all the data of table from db 
        #self.cursor.execute( """INSERT INTO humiture (date,illuminance,temperature,humidity,windspeed) VALUES(?,?,?,?,?)""",time.strftime("%Y/%m/%d %H:%M:%S",time.localtime()), self.receive_data[0],self.receive_data[1],self.receive_data[2],self.receive_data[3]);
        
#        self.cursor.execute("INSERT INTO humiture (date,illuminance,temperature,humidity,windspeed) VALUES('2019/4/11',13,23.4,33.2,0.0)");
        self.date = time.strftime("%Y/%m/%d %H:%M:%S",time.localtime())
        self.illuminance = self.receive_data[0]
        self.temperature = self.receive_data[1]
        self.humidity = self.receive_data[2]
        self.windspeed = self.receive_data[3]
        values = (self.date,self.illuminance,self.temperature,self.humidity,self.windspeed)
        sql = '''INSERT INTO humiture(date,illuminance,temperature,humidity,windspeed) VALUES(?,?,?,?,?)'''
        self.cursor.execute(sql,values);
        
        self.setup.db_commit()
      
        print('Data stored in Database success')
        

        
    def update_data(self): 
        # update the select data
        self.cursor.execute("\
                UPDATE humiture SET date = ?,illuminance = ?,temperature = ?,humidity= ?,windspeed=?\
                WHERE ID = ?",\
                         (time.strftime("%Y/%m/%d %H:%M:%S",time.localtime()),\
                          self.get_data.illuminance(),self.get_data.temperature,\
                          self.get_data.humidity(),self.get_data.windspeed()\
                          ))
            
        self.setup.db_commit()
  
      
                    
    def delete_data(self): 
        # delete data from database
        self.cursor.execute( "DELETE date ,illuminance,temperature,humidity,windspeed\
                          FROM humiter" )
        self.setup.db_commit()
        
    
    
    def select_data(self):
        self.cursor.execute(" SELECT date ,illuminance,temperature,humidity,windspeed\
                          FROM humiture WHERE data = ?",\
                         ())        
        self.fetch_data = self.cursor.fetchall()
        return self.fetch_data
        
    
    
    def select_all_data(self):
        
        
        # select all the data from database
        self.cursor.execute(" SELECT * from humiture")        
        for row in self.cursor:
            print(row)
            print("date:",row[0])
            print("illuminance:",row[1])
            print("temperture:",row[2])
            print("humidity:",row[3])
            print("windspeed",row[4],"\n")
 

              
