# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 11:13:54 2018

@author: lenovo
"""

import visa
rm=visa.ResourceManager()
import time
import numpy as np
class Keithley6221():
    
    def __init__(self,address):
        self.inst=rm.open_resource(address)
    
    def delta_read(self):
        self.a=inst.query('sens:data:latest?')
        self.b=float(self.a.split(',')[0])
        return (self.b)