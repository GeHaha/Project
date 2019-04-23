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
     
    
    def one_hour_data(self):
        self.__cursor.execute("select * from humiture where \
                             date  > datetime('now','-1 hour','localtime')");
#        for row in data:
#            print("Time = ",row[0])
#            print("illuminance = ",row[0])
#            print("temperature = ",row[0]) 
#            print("humidity = ",row[0])
#            print("windspeed = ",row[0]) 
        data = self.__cursor.fetchall()
        print(data)
        print("读了一小时数据")
    
    def three_hours_data(self):
        self.__cursor.execute("select * from humiture where \
                              date  > datetime('now','-3 hour','localtime')");
    
    
    def one_day_data(self):
        self.__cursor.execute("select * from humiture where \
                    date >= datetime('now','start of day','+0 day') and\
                    date < datetime('now','start of day','+1 day')");
        one_data = self.__cursor.fetchall()
        print(one_data)
    
                     
    def three_days_data(self):
        self.__cursor.execute("select * from humiture where \
                    date >= datetime('now','start of day','-3 day') and\
                    date < datetime('now','start of day','+0 day')")
        three_data = self.__cursor.fetchall()
        print(three_data)
    
    def senven_days_data(self):        
        # 这个时间取的是 周一到周日为一周
        self.__connect("data_base/humiture.db")
        self.__cursor.execute("select * from humiture where \
                 date >= datetime('now','start of day','-7 day','weekday 1') AND\
                 date < datetime('now','start of day','+0 day','weekday 1')");

        senven_data = self.__cursor.fetchall()
        print(senven_data)
        
    def fifteen_days_data(self):
        self.__cursor.execute("select * from humiture where \
                 date >= datetime('now','start of day','-15 day') AND\
                 date < datetime('now','start of day','+0 day')");
    
    
    def one_month_data(self):
        self.__cursor.execute("select * from humiture where \
                 date >= datetime('now','start of month','+0 month','-0 day') and \
                 date < datetime('now','start of month','+1 month','0 day')");
    
    
    def three_month_data(self):
        self.__cursor.execute("select * from humiture where \
                 date >= datetime('now','start of month','-3 month','-0 day') and \
                 date < datetime('now','start of month','+0 month','0 day')");
         
    def six_month_data(self):
        self.__cursor.execute("select * from humiture where \
                 date >= datetime('now','start of month','-6 month','-0 day') and \
                 date < datetime('now','start of month','+0 month','0 day')");
        
    def one_year_data(self):
        self.__cursor.execute("select * from humiture where\
                              date between () and ()");
    
    
    def total_changes_data(self):
        pass



