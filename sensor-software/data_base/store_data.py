# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:28:25 2019

@author: Gehaha
"""

import sqlite3

class ManageData(object):
    db_name = "humiture.db"
    table_name = "humiture"
    
    def __init__(self):
        pass

    
    def query(self,db_name,sql,data):
        with sqlite3.connect(db_name) as db:
            self.cursor = db.cursor()
            self.cursor.execute(sql,data)
            self.ressult = self.cursor.fetchall()
            db.commit()
            return self.result
        
        
        
    def show_all_data(self,db_name,table_name):
        #show all the data of table from db
        sql = " SELECT * FROM {0}".format(table_name)
        return self.query(db_name,sql,())
    
    
        
    def insert_data(self,db_name,table_name,time,illuminance,temperature,humidity,windspeed):
        
        # show all the data of table from db
        sql = """
            INSERT INTO {0}(Time,Illuminance,Temperature,Humidity,Windspeed)\
            VALUES(?,?,?,?,?)""".format(table_name) 
          
        self.query(db_name,sql,(time,illuminance,temperature,humidity,windspeed,))
        print('Data stored in Database')
               
    
    
    def updata_data(self,Id,db_name,table_name,time,illuminance,temperature,humidity,windspeed):
        
        sql = """
                UPDATE {0} SET Time = ?,Illuminance = ?,Temperature = ?,Humidity= ?,Windspeed=?
                WHERE ID = ? """.format(table_name)
        self.query(db_name,sql,(time,illuminance,temperature,humidity,windspeed,Id))
    
  
    
    def delete_data(self,db_name,table_name,Id):
        
        sql = """
                DELETE FROM {0} WHERE ID = ? 
             """.format(table_name)
        self.query(db_name,sql,(Id,))
    
        
        
    