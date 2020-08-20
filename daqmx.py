# -*- coding: utf-8 -*-
"""
Created on Fri May 25 21:17:04 2018

@author: lenovo
"""
import nidaqmx

class daqmx():
    
    def __init__(self):
        self.reading=[]
            
    def readout(self, channel):
        with nidaqmx.Task() as self.task:
            self.task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
            self.task.ai_channels.add_ai_voltage_chan("Dev1/ai1")
            self.task.ai_channels.add_ai_voltage_chan("Dev1/ai2")
            self.task.ai_channels.add_ai_voltage_chan("Dev1/ai3")
            self.reading=self.task.read()
        return self.reading[int(channel)]
    
    def ao0(self,value):
        with nidaqmx.Task() as self.task:
            self.task.ao_channels.add_ao_voltage_chan('Dev1/ao0')
            self.task.write(value, auto_start=True)
            
    def ao1(self,value):
        with nidaqmx.Task() as self.task:
            self.task.ao_channels.add_ao_voltage_chan('Dev1/ao1')
            self.task.write(value, auto_start=True)
        
    

