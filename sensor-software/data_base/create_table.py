# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:42:41 2019

@author: Gehaha
"""


import sqlite3
import os



def singletonDecorator(cls, *args, **kwargs):
    """定义一个单例装饰器"""
    instance = {}

    def wrapperSingleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapperSingleton     


   
@singletonDecorator
class SetupDB(object):
    
    def __init__(self):
   
        self.connection = None
        self.cursor = None
        self.db_connect()
        self.create_tables()
     


    def __del__(self):
        self.db_close()
        
   
             
    def db_connect(self):
        if self.connection is None:            
            self.connection = sqlite3.connect('humiture.db',timeout=3,isolation_level=None,check_same_thread=False)          
            self.cursor = self.connection.cursor()
            print("database connect")
            return self.connection        
        else:
            print("connect database success!")
  
    
    
    def db_close(self):
        self.connection.close()
        print("close database success!")


    
    def db_commit(self):
        self.connection.commit()
 
       
        
    def create_tables(self):
        self.create_humiture_table()
    
        
        
    def drop_tables(self):       
        # drop table if it exists
        self.cursor.execute("DROP TABLE IF EXISTS humiture")
        print("drop humiture success")
    
    
    
    def create_humiture_table(self):
        self.cursor.execute("\
                         CREATE TABLE IF NOT EXISTS humiture(\
                         date TEXT,\
                         illuminance integer,\
                         temperature    real,\
                         humidity      real,\
                         windspeed    real\
                         )")        
        print("creat humiture table success")

        
        