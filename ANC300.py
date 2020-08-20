# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:55:11 2019

@author: kaife
"""

import visa
rm= visa.ResourceManager()

class ANC300():
    
    def __init__(self, addr='ASRL4::INSTR'):
        self.inst = rm.open_resource(addr)
        
        
    def increase(self, channel,steps):
        command='stepu {} {} '.format(channel,steps)
        self.inst.query(command)

    def decrease(self, channel,steps):
        command='stepd {} {} '.format(channel,steps)
        self.inst.query(command)
        
    def set_step_size(self,channel,setp):
        
        command='setv {} {}\n'.format(channel,setp)
        self.inst.query(command)
        
    def set_offset(self,channel,setp):
        
        command='seta {} {}\n'.format(channel,setp)
        self.inst.query(command)
        
    def get_step_size(self,channel):
        command = 'getv {}\n'.format(channel)
        return self.inst.query(command)

    def get_offset(self,channel):
        command = 'geta {}\n'.format(channel)
        return self.inst.query(command)

    def disconnect(self):
        self.inst.close()