# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:10:51 2019

@author: Gehaha
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import curve_Ui

class CandlestickItem(pg.GraphicsObject):
    
    def __init__(self,data):
        pg.GraphicsObject.__init__(self)
        self.data = data
        self.generatePicture()
        
    def generatePicture(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        w = (self.data[1][0]-self.data[0][0])/3.
        for(t,open,close,min,max) in self.data:
            print(t,open,close,min,max)
            p.drawLine(QtCore.QPointF(t,min),QtCore.QPointF(t,max))
            if open > close:
                p.setBrush(pg.mkBrush('g')) #设置画刷颜色为绿
            else:
                p.setBrush(pg.mkBrush('r')) #设置画刷颜色为红
                
            p.drawRect(QtCore.QRectF(t,-w,open,w*2,close - open))
            
        p.end()
        
                
    def paint(self,p,*args):
        p.drawPicture(0,0,self.picture)
         
    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())
    
    
    
    def plot_k_line(self,code = None,start = None,end = None):
        self.data = ts.get_hist_data(code = code,start = start,end = end).sort_index()
        y_min = self.data['low'].min()
        y_max = self.data['high'].max()
        
        data_list = []
        d = 0
        
        for dates ,row in self.data.interrows():
            
            #将时间转换为数字
            date_time = datetime.datetime.strptime(dates,'%Y-%m-%d')
            
            open,high,close,low = row[:4]
            datas = (d,open,close,low,high)
            data_list.append(datas)
            print(datas)
            d += 1
            
        self.axis_dict = dict(enumerate(self.data.index))
        
        axis_1 = [(i, list(self.data.index)[i]) for i in range(0, len(self.data.index), 3)]  # 获取日期值
        axis_2 = [(i, list(self.data.index)[i]) for i in range(0, len(self.data.index), 5)]
        axis_3 = [(i, list(self.data.index)[i]) for i in range(0, len(self.data.index), 8)]
        axis_4 = [(i, list(self.data.index)[i]) for i in range(0, len(self.data.index), 10)]
        axis_5 = [(i, list(self.data.index)[i]) for i in range(0, len(self.data.index), 30)]

        
    
        stringaxis = pg.AxistItem(orientation = 'bottom')
        stringaxis.setTicks([axis_5,axis_4,axis_3,axis_a,axis_1])
        self.axis_dict.items()
                
        self.k_plt.plotItem.clear()
        item = CandlestickItem(data_list)
        self.k_plt.addItem(item,)
        self.k_plt.showGrid(x= True,y= True)
        self.k_plt.setLabel(axis = 'left',text = '指数')
        self.k_plt.setLabel(axis = 'bottom',text = '日期')
        self.label = pg.TextItem()
        self.k_plt.addItem(self.label)
        
        self.vLine = pg.InfiniteLine(angle = 90,movable = False,)
        self.hLine = pg.InfiniteLine(angle = 0,movable = False,)
        self.k_plt.addItem(self.vLine,ignoreBounds = True)
        self.k_plt.addItem(self.hLine,ignoreBounds = True)
        
        
        
        
    def query_slot(self):
        try:
            self.que_btn.setEnabled(False)
            self.que_btn.setText("查询中...")
            code = self.stock_code.text()
            
            data_sel = self.option_sel.currentText()[1:-1]
            start_date = datetime.datetime.today() - datetime.timedelta(days=1)
            start_date_str = datetime.datetime.strftime(start_date,"%Y-%m-%d")
            end_date = datetime.datetime.today() - datetime.timedelta(days= 1)
            end_date_str = datetime.datetime.strftime(end_date,"%Y-%m-%d")
            print(code,start_date_str,end_date_str)
            self.plot_k_line(code = code,start = start_date_str,end = enda_date_str)
            self.que_btn.setEnabled(True)
            self.que_btn.setText("查询")
            
        except Exception as e:
            print(traceback.print_exc())
            
            
            
    def print_slot(self,event = None):
        if event is None:
            print("事件为空")
        else:
            pos = event[0]
            
            try:
                if self.k_plt.sceneBoundingRect().contains(pos):
                    mousePoint = self.k_plt.plotItem.vb.mapSceneToView(pos)
                    
                    index = int(mousePoint.x())
                    pos_y = int(mousePoint.y())
                    if -1 < index < len(self.data.index):
                        self.label.setHtml(
                            "<p style='color:white'><strong>日期：{0}</strong></p><p style='color:white'>开盘：{1}</p><p style='color:white'>收盘：{2}</p><p style='color:white'>最高价：<span style='color:red;'>{3}</span></p><p style='color:white'>最低价：<span style='color:green;'>{4}</span></p>".format(
                                self.axis_dict[index], self.data['open'][index], self.data['close'][index],
                                self.data['high'][index], self.data['low'][index]))
                        self.vLine.setPos(mousePoint.x())
                        self.hLine.setPos(mousePoint.y())
                        
            except Exception as e:
                
                print(traceback.print_exc())
                    
                    
                    
                    