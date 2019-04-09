# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:28:25 2019

@author: Gehaha
"""
import sys
sys.path.append("communcate")

import sqlite3
import time



from create_table import  SetupDB
from communcate.data_pack import DataPack



class ManageData(object):
#    db_name = "humiture.db"
#    table_name = "Humiture"

#    
    def __init__(self):
#        self.__name = name
           
        self.get_data = DataPack()
        self.setup = SetupDB()
        self.setup.setup_db_con()
        self.setup.create_tables()
        
        
        self.con = sqlite3.connect("humiture.db")
        self.cur = self.con.cursor()
           


    def insert_data(self):  
        # show all the data of table from db
        self.get_data = DataPack()        
        self.cur.execute( "\
            INSERT INTO humiture (date,illuminance,temperature,humidity,windspeed)\
            VALUES(?,?,?,?,?)",\
                     (time.strftime("%Y/%m/%d %H:%M:%S",time.localtime()),\
                      self.get_data.illuminance(),self.get_data.temperature,\
                      self.get_data.humidity(),self.get_data.windspeed()\
                      ))        
        print('Data stored in Database')
        self.con.commit()
        

        
    def updata_data(self):        
        self.cur.execute("\
                UPDATE humiture SET date = ?,illuminance = ?,temperature = ?,humidity= ?,windspeed=?\
                WHERE ID = ?",\
                         (time.strftime("%Y/%m/%d %H:%M:%S",time.localtime()),\
                          self.get_data.illuminance(),self.get_data.temperature,\
                          self.get_data.humidity(),self.get_data.windspeed()\
                          ))
        self.con.commit()
        
  
            
    def delete_data(self):
        
        self.cur.execute( "DELETE data ,illuminance,temperature,humidity,windspeed\
                          FROM humiter" )
        self.con.commit()
        
    
    
    def select_data(self):
        self.cur.execute(" SELECT data ,illuminance,temperature,humidity,windspeed\
                          FROM humiture WHERE data = ?",\
                         ())        
        data = self.cur.fetchall()
        return data
    
    
    
    def select_all_data(self):
        self.cur.execute(" SELECT *\
                           FROM humiture")
        print("hahaha")
        for row in self.cur:
            print("Date：",row[0])
            print("illuminance:",row[1])
            print("temperture:",row[2])
            print("humidity:",row[3])
            print("windspeed",row[4],"\n")
    
   
def test():    
    
    setup = SetupDB()
    data = ManageData()
    setup.create_tables()
    data.insert_data()
    data.select_all_data()

test()    

