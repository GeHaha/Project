import sqlite3
import time


class DataBaseHelper(object):
    def __init__(self):
      # self.__table_type

    def create_db(name):
    def connect(self, name):
    def close(self, Name):

    def create_table(self, name):
        self.cursor.execute("\
                         CREATE TABLE IF NOT EXISTS humiture(\
                         date TEXT,\
                         illuminance integer,\
                         temperature    real,\
                         humidity      real,\
                         windspeed    real\
                         )")
        print("create humiture table success.")

    def drop_table(self, name):

    def insert_data(self, data):
    
    def select_data(self, table_name):
    
    def delete_data(self, table_name, id):
      
    def update-data():
      pass

    def total_changes(self):


    def
