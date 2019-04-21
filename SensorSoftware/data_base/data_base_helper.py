import sqlite3
import time

class DataBaseHelper(object):
    
    def __init__(self):             
      # self.__table_type
      self.__connect("data_base/humiture.db")
      
 
    def __del__(self):
        
        self.__connection.close()
        

    def create_db(self,name):        
        pass

    def __connect(self, db_name):
        self.__connection = sqlite3.connect(db_name,\
                                          check_same_thread = False)
        self.__cursor = self.__connection.cursor()
        
        
    
    def close(self, db_name):
        self.__connection.close()
        
        

    def create_table(self, table_name):
        self.__cursor.execute("\
                         CREATE TABLE IF NOT EXISTS humiture(\
                         date TEXT,\
                         illuminance integer,\
                         temperature    real,\
                         humidity      real,\
                         windspeed    real\
                         )")
        print("create humiture table success.")

    def drop_table(self, table_name):
        self.__cursor.execute("DROP TABLE IF EXISTS humiture")
        print("drop humiture success")
        

    def insert_data(self, table_name, data):
        date = time.strftime("%Y/%m/%d %H:%M:%S",time.localtime())
        values = (date,data.illuminance(), data.temperature(), data.humidity(), data.windspeed())
        sql = '''INSERT INTO humiture(date,illuminance,temperature,humidity,windspeed) VALUES(?,?,?,?,?)'''
        self.__cursor.execute(sql,values);        
        print('Data stored in Database success')
        self.__connection.commit()
        
        
    
    def select_data(self):
        self.__cursor.execute("SELECT date,illuminance,temperature,humidity,windspeed FROM humiture ORDER BY date DESC")        
        fetch_data = self.__cursor.fetchmany()
        return fetch_data
    
        timedate = fetch_data[0][0]
        print(timedate,"\n") 
    
    def delete_data(self, table_name):
        pass
      
    def update_data(self):
        pass

    def total_changes(self):
        pass



