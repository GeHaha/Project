# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:42:41 2019

@author: Gehaha
"""

import sqlite3
import os
con = None

class SetupDB(object):
    
    def __init__(self):
        self.query()
        self.create_tables()
        
        
    def __del__(self):
        self.close_db()
        
        
    def query(self,db_name,sql,data):
        # access the sqlites data base
        db_name = 'humiture.db'
        with sqlite3.connect(db_name) as db:
            self.cursor = db.cursor()
            self.cursor.excute(sql,data)
            self.db.commit()       
#        
#    def setup_db_con(self):
#        self.con = sqlite3.connect()
#        self.cur = self.con.cursor()
            
    def close_db(self):
        self.db.close()
#        
    def create_tables(self,db_name,table_name,sql):
        self.create_humiture_table()
        
    
    def drop_tables(self,db_name,table_name,sql):       
        # drop table if it exists
        #self.cur.execute("DROP TABLE IF EXISTS humiture")
        sql = "DROP TABLE IF EXISTS {0}".format()
        self.query(db_name,table_name,sql,())
            
        
    def create_humiture_table(self,db_name,table_name,sql):
        table_name = "humiture"
        sql = """
            CREATE TABLE IF NOT EXISTS humiture(Time text,\
                            Illumilluminance int,\
                            Temperature    float,\
                            Humidity      float,\
                            Windspeed    float)
            """
        self.query(db_name,table_name,sql,()) 
               
#        
#    def process_item(self,item,spider):
#        self.store_in_db(item)
#        return item
#    


            
        
        