# -*- coding: utf-8 -*-
"""
Created on Thu May 24 21:32:33 2018

@author: Kaifei Kang
"""

import visa
rm=visa.ResourceManager()
import time
import numpy as np
class Keithley2400():
    
    def __init__(self,address):
        self.inst=rm.open_resource(address)
        
    def set_volt(self,value):
#        self.inst.write(":SOUR:FUNC 'VOLT'")
        self.inst.write(":SOUR:VOLT:LEV "+str(value))

    def set_curr(self,value):
#        self.inst.write(":SOUR:FUNC 'CURR'")
        self.inst.write(":SOUR:CURR:LEV "+str(value))
        
    def get_volt(self):
        self.x=self.inst.query(":MEAS?")
        self.x=self.x.strip('\n').split(',')[0]
        return (float(self.x))
    
    def get_curr(self):      
        self.x=self.inst.query(":MEAS?")
        self.x=self.x.strip('\n').split(',')[1]
        return (float(self.x))

    def get_set_volt(self):
        self.x = self.inst.query(":SOUR:VOLT:LEV?")
        self.x=self.x.strip('\n').split(',')[0]
        return (float(self.x))
        
    def ramp_gate(self,end, num = 100, waittime = 0.1):
        
        self.curr_gate = self.get_set_volt()
        self.list=np.linspace(self.curr_gate, end, num)
        
        for i in range(len(self.list)):
            self.set_volt(self.list[i])
            time.sleep(waittime)
            
    def ramp_volt(self,volt,stepsize=0.05,waittime=0.1):
        self.voltnow=self.get_set_volt()
        steps=int(np.abs(self.voltnow-volt)/stepsize+2)
        DCV_back=np.linspace(self.voltnow,volt,steps)
        for i in range(len(DCV_back)):
            self.set_volt(DCV_back[i])
            time.sleep(waittime)
#            print(self.get_curr())
    
    def closeall(self):
        self.inst.close()
    
    
        