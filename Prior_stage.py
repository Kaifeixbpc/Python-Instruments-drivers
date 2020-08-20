# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 13:44:29 2020

@author: kaifei
"""
import time
import visa
rm=visa.ResourceManager()

class prior():
    
    def __init__(self,addr='ASRL5::INSTR'):
        self.addr=addr 
    
    def move_XY(self,x,y):
        self.set_value('G {},{}'.format(x,y))

    def move_X(self,x):
        self.set_value('GX {}'.format(x))
        
    def move_Y(self,y):
        self.set_value('GY {}'.format(y))
        
    def move_Z(self,z):
        self.set_value('GZ {}'.format(z))        

    def move_Xrel(self,x):
        self.set_value('GR {} 0,0,'.format(x))
    def move_Yrel(self,y):
        self.set_value('GR 0,{},0'.format(y))
    def move_Zrel(self,z):
        self.set_value('GR 0,0,{}'.format(z))
        
    def get_P(self):
        
        pos=self.get_value('PS?\r')+self.get_value('PS?\r')    
        try:
            return pos.strip('R')
        except:
            return(0,0)
            
    def set_value(self,command):
        
        self.inst=rm.open_resource(self.addr,baud_rate = 9600)
        self.inst.write_termination='\r'
        self.inst.read_termination='\r'  
        self.inst.write(command)
        self.inst.close()
        time.sleep(0.3)
        
    def get_value(self,command):
        
        self.inst=rm.open_resource(self.addr,baud_rate = 9600)
        self.inst.write_termination='\r'
        self.inst.read_termination='\r'  
        return self.inst.query(command)
        self.inst.close()

    
#P=prior()
#print(P.get_value('SKEW?'))