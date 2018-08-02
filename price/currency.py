# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 23:17:03 2018

@author: HP
"""
class currency (object):
    def __init__(self):
        self._name = None
        self._price = None
        
    @property   
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        self._name = value
        
       
  