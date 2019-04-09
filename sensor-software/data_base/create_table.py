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

        self.setup_db_con()
        self.create_tables()
     

    def __del__(self):
        self.db_close()
        
        
        
    def setup_db_con(self):
        con = None
        if con is None:            
            self.con = sqlite3.connect('humiture.db')
            self.cur = self.con.cursor()
            return self.cur
        else:
            print("connect database success!")
  

          
    def db_close(self):
        self.con.close()
        

        
    def create_tables(self):
        self.create_humiture_table()
        
        
        
    def drop_tables(self):       
        # drop table if it exists
        self.cur.execute("DROP TABLE IF EXISTS humiture")
    
    
    
    def create_humiture_table(self):
        self.cur.execute("\
                         CREATE TABLE IF NOT EXISTS humiture(\
                         id INTEGER PRIMART KEY NOT NULL,\
                         data TEXT,\
                         illumilluminance inter,\
                         temperature    real,\
                         humidity      real,\
                         windspeed    real\
                         )")        
    

        
        