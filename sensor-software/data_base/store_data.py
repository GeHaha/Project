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
        self.setup_db_con()
        self.create_tables()
        
    def __del__(self):
        self.close_db()
        
        
    def setup_db_con(self):
        self.con = sqlite3.connect()
        self.cur = self.con.cursor()
        
    def create_tables(self):
        self.drop_tables()
        self.create_tables()
        
    
    def drop_tables(self):
        # drop table if it exists
        self.cur.execute("DROP TABLE IF EXISTS humiture")
        
    def close_db(self):
        self.con.close()
        
    def create_humiture_table(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS humiture(Time text,\
                            Illumilluminance int,\
                            Temperature    float,\
                            Humidity      float,\
                            Windspeed    float)")
        
#    def process_item(seif,item,spider):
#        self.store_in_db(item)
#        return item
#    

    def store_in_db(self,item):
        self.cur.execute("INSERT INTO humiture(\
                        Time,\
                        Illumilluminance,\
                        Temperature,\
                        Humidity,\
                        Windspeed)\
            VALUES(?,?,?,?,?)",\
            (\
            item.get('',''),
            item.get('','')
            item.get('','')
            item.get('','')
            ))
        print('Data stored in Database')
        self.con.commit()
        
        
        