import sys
sys.path.append("ui")
import sqlite3
import time
#from childWindow import childWindow

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
                         storedate TEXT primary key,\
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
        storedate = time.strftime("%Y-%m-%d%H:%M:%S",time.localtime())
        values = (storedate,data.illuminance(), data.temperature(), data.humidity(), data.windspeed())
        sql = '''INSERT INTO humiture(storedate,illuminance,temperature,humidity,windspeed) VALUES(?,?,?,?,?)'''
        self.__cursor.execute(sql,values);        
        print('Data stored in Database success')
        self.__connection.commit()
        
        
        
    def select_any_time(self,startdate,enddate):
        print(startdate)
        value = []
        sql=  "select * from humiture where storedate \
         between '%s' and '%s';"%(str(startdate),str(enddate))       
        cursor = self.__cursor.execute(sql)
        for row in cursor:
            value.append(row)
            print(value)
        return value

     
#    def select_data(self):
#        self.__cursor.execute("SELECT storedate,illuminance,temperature,humidity,windspeed FROM humiture ORDER BY storedate DESC")        
#        fetch_data = self.__cursor.fetchmany()
#        return fetch_data    
#        timedate = fetch_data[0][0]
#        print(timedate,"\n") 
    
    def select_one_hour(self):
        value = []
        cursor = self.__cursor.execute("select * from humiture where \
                              storedate  > datetime('now','-1 hour','localtime')");
        for row in cursor:
            value.append(row)
            print(row)
        return value
    
    
    def select_three_hour(self):
        value = []
        cursor = self.__cursor.execute("select * from humiture where \
                                       storedate > datetime('now','-3 hour','localtime')");
        for row in cursor:
            value.append(row)
        return value
    
    
    def select_six_hours(self):
        value = []
        cursor = self.__cursor.execute("select * from humiture where \
                              storedate  > datetime('now','-1 hour','localtime')");
        for row in cursor:
            value.append(row)
            print(row)
        return value
            
    
    def select_one_day(self):
        value = []
        cursor = self.__cursor.execute("select * from humiture where \
                    storedate >= datetime('now','start of day','+0 day') and\
                    storedate < datetime('now','start of day','+1 day')");
        for row in cursor:
            value.append(row)
        return value
        
    
    def select_three_days(self):
        value = []
        cursor = self.__cursor.execute("select * from humiture where \
                    storedate >= datetime('now','start of day','-2 day') and\
                    storedate < datetime('now','start of day','+1 day')")
        for row in cursor:
           value.append(row)
        return value
             
                
    def select_senven_days(self):        
        # 这个时间取的是 周一到周日为一周
        value = []
        cursor = self.__cursor.execute("select * from humiture where \
                 storedate >= datetime('now','start of day','-7 day','weekday 1') AND\
                 storedate < datetime('now','start of day','+0 day','weekday 1')");
        for row in cursor:
            value.append(row)
        return row
             
        
    def select_fifteen_days(self):
        value = []
        cursor = self.__cursor.execute("select * from humiture where \
                 storedate >= datetime('now','start of day','-15 day') AND\
                 storedate < datetime('now','start of day','+0 day')");
        for row in cursor:
            value.append(row)
        return value
            
    
    def select_one_month_data(self):
        #获取当月的数据
        value = []
        cursor = self.__cursor.execute("select * from humiture where \
                 storedate >= datetime('now','start of month','+0 month','-0 day') and \
                 storedate < datetime('now','start of month','+1 month','0 day')");
        for row in cursor:
            value.append()
        return value
            
    
    def select_three_month(self):  
        # 获取的是最近三个月数据，包括当月
        value = []
        cursor = self.__cursor.execute("select * from humiture where \
                 storedate >= datetime('now','start of month','-3 month','-0 day') and \
                 storedate < datetime('now','start of month','+0 month','0 day')");
        for row in cursor:
            value.append(row)           
        return value
            
            
    def select_six_month(self):
        value = []
        cursor = self.__cursor.execute("select * from humiture where \
                 storedate >= datetime('now','start of month','-6 month','-0 day') and \
                 storedate < datetime('now','start of month','+0 month','0 day')");
        for row in cursor:
            value.append(row)
        return value
            
    
    def select_one_year(self):
        value = []
        cursor = self.__cursor.execute("select * from humiture where\
                              date between () and ()");
        for row in cursor:
            value.append(row)
        return value
     

    def total_changes_data(self):
        pass



