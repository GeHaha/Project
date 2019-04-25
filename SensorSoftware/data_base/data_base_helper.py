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
        date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
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
     
#        
#    def one_hour_data(self):
#        value = []
#        cursor = self.__cursor.execute("select * from humiture where \
#                              date  > datetime('now','-1 hour','localtime')");
#        for row in cursor:
#            value.append(row)
#            print(row)
#        return value
    
    
    def six_hours_data(self):
        value = []
        cursor = self.__cursor.execute("select * from humiture where \
                              date  > datetime('now','-6 hour','localtime')");
        for row in cursor:
            value.append(row)
            print(row)
        return value
            
    
    def one_day_data(self):
        value = []
        cursor = self.__cursor.execute("select * from humiture where \
                    date >= datetime('now','start of day','+0 day') and\
                    date < datetime('now','start of day','+1 day')");
        for row in cursor:
            value.append(row)
        return value
        
    def three_days_data(self):
        cursor = self.__cursor.execute("select * from humiture where \
                    date >= datetime('now','start of day','-2 day') and\
                    date < datetime('now','start of day','+1 day')")
        for row in cursor:
           print(row)
        
            
    
    def senven_days_data(self):        
        # 这个时间取的是 周一到周日为一周
        cursor = self.__cursor.execute("select * from humiture where \
                 date >= datetime('now','start of day','-7 day','weekday 1') AND\
                 date < datetime('now','start of day','+0 day','weekday 1')");
        for row in cursor:
            return row
             
        
    def fifteen_days_data(self):
        cursor = self.__cursor.execute("select * from humiture where \
                 date >= datetime('now','start of day','-15 day') AND\
                 date < datetime('now','start of day','+0 day')");
        for row in cursor:
            print(row)
            print('\n')
            
    
    def one_month_data(self):
        #获取当月的数据
        cursor = self.__cursor.execute("select * from humiture where \
                 date >= datetime('now','start of month','+0 month','-0 day') and \
                 date < datetime('now','start of month','+1 month','0 day')");
        for row in cursor:
            print(row)
            print('\n')
            
    
    def three_month_data(self):  
        # 获取的是最近三个月数据，包括当月
        cursor = self.__cursor.execute("select * from humiture where \
                 date >= datetime('now','start of month','-3 month','-0 day') and \
                 date < datetime('now','start of month','+0 month','0 day')");
        for row in cursor:
            print(row)
            print('\n')
            
            
    def six_month_data(self):
        cursor = self.__cursor.execute("select * from humiture where \
                 date >= datetime('now','start of month','-6 month','-0 day') and \
                 date < datetime('now','start of month','+0 month','0 day')");
        for row in cursor:
            print(row)
            print('\n')
            
    def one_year_data(self):
        cursor = self.__cursor.execute("select * from humiture where\
                              date between () and ()");
        for row in cursor:
            print(row)
            print('\n')
            
    
    def total_changes_data(self):
        pass



