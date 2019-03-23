# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 19:08:48 2018

@author: Gehaha
"""

class DataBase(object):
    __instance = None
    __isFirstInit = False
    
    def __new__(cls):
        if not cls.__instance:
            DataBase.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            self.sendMsg = []
            self.feedbackMsg = []
            self.__isFirstInit = True    
        else:
            pass
        