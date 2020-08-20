# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 21:19:38 2019

@author: lenovo
"""

import time
import matplotlib.pyplot as plt
import socket

class itc():
    
    def __init__(self):
        self.HOST = '192.168.1.3'    # The remote host
        self.PORT = 7020              # The same port as used by the server  

######acquire info    
        
    def get_info(self):

        self.command='READ:SYS:CAT?\n'
        return self.query_command(self.command)

    def VTI_T(self, value = None):
        if value is None:
            self.command="READ:DEV:MB1.T1:TEMP:SIG:TEMP\n"
            self.data=self.query_command(self.command)
            return self.data 
        else:
            self.command="SET:DEV:MB1.T1:TEMP:LOOP:TSET:"+str(value)+'\n'
            self.set_command(self.command)            
    
    def probe_T(self, value = None):
        if value is None:
            self.command="READ:DEV:DB8.T1:TEMP:SIG:TEMP\n"
            self.data=self.query_command(self.command)
            return self.data 
        else:
            self.command="SET:DEV:MB1.T1:TEMP:LOOP:TSET:"+str(value)+'\n'
            self.set_command(self.command)
    
    def get_VTIT(self):
        self.command="READ:DEV:MB1.T1:TEMP:SIG:TEMP\n"
        self.data=self.query_command(self.command)
        return self.data 
    
    def get_ProbeT(self):
        self.command="READ:DEV:DB8.T1:TEMP:SIG:TEMP\n"
        self.data=self.query_command(self.command)
        return self.data 

#####set parameters


    def set_Prob_temp(self,value):
        self.command="SET:DEV:DB8.T1:TEMP:LOOP:RENA:OFF\n"
        self.set_command(self.command)
        time.sleep(0.1)
        
        self.command="SET:DEV:DB8.T1:TEMP:LOOP:TSET:"+str(value)+'\n'
        self.set_command(self.command)
        
    def set_VTI_temp(self,value):
        self.command="SET:DEV:MB1.T1:TEMP:LOOP:RENA:OFF\n"
        self.set_command(self.command)
        time.sleep(0.1)
        
        self.command="SET:DEV:MB1.T1:TEMP:LOOP:TSET:"+str(value)+'\n'
        self.set_command(self.command)
        
    def ramp_prob_temp(self, setT, rate):
        self.command = "SET:DEV:DB8.T1:TEMP:LOOP:RSET:" + str(rate)+'\n'
        self.x = self.query_command(self.command)
        print(self.x)
                
        self.CurrentT = self.get_ProbeT()
        print(self.CurrentT)
        time.sleep(0.1)
        
        self.command = "SET:DEV:DB8.T1:TEMP:LOOP:TSET:"+str(self.CurrentT)+'\n'
        self.x = self.query_command(self.command)
        print(self.x)
                
        self.command = "SET:DEV:DB8.T1:TEMP:LOOP:RENA:ON\n"
        self.x = self.query_command(self.command)
        print(self.x)
                
        self.command = "SET:DEV:DB8.T1:TEMP:LOOP:TSET:"+str(setT)+'\n'
        self.x = self.query_command(self.command)
        print(self.x)
                
        self.command = "SET:DEV:MB1.T1:TEMP:LOOP:RSET:" + str(rate)+'\n'
        self.x = self.query_command(self.command)        
        print(self.x)
                
        self.command = "SET:DEV:MB1.T1:TEMP:LOOP:TSET:"+str(float(self.CurrentT)-0.2)+'\n'
        self.x = self.query_command(self.command)
        print(self.x)
                
        self.command = "SET:DEV:MB1.T1:TEMP:LOOP:RENA:ON\n"
        self.x = self.query_command(self.command)
        print(self.x)
                
        self.command = "SET:DEV:MB1.T1:TEMP:LOOP:TSET:"+str(float(setT)-0.2)+'\n'
        self.x = self.query_command(self.command)
        print(self.x)

    def ramp_off(self):
        self.command = "SET:DEV:DB8.T1:TEMP:LOOP:RENA:OFF\n"
        self.x = self.query_command(self.command)
        print(self.x)
        
        self.command = "SET:DEV:MB1.T1:TEMP:LOOP:RENA:off\n"
        self.x = self.query_command(self.command)
        print(self.x)
####################### universal command
    
    def query_command(self,command):
        while True:
            try:
                HOST=self.HOST
                PORT=self.PORT
                
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect((HOST,PORT))
                self.s.sendall(str.encode(command))
                data=self.s.recv(1024)
                self.s.close()
                
                data=data.decode('utf-8').strip('\n')
                data=data.split(':')[6].strip('K')
                return(data)
                
                time.sleep(0.1)
                break
                
            except Exception as e:
                print(e)
                time.sleep(0.1)
                self.s.close()
                continue
        
        
    def to_set(self):
        while True:
            try:
                self.set_command(b"SET:DEV:GRPZ:PSU:ACTN:HOLD\n")
                self.set_command(b"SET:DEV:GRPZ:PSU:ACTN:RTOS\n")
                break
            except socket.error as msg:
                continue
            
        
    def set_command(self,command):
        
        self.HOST = '192.168.1.3'    # The remote host
        self.PORT = 7020              # The same port as used by the server

        while True:
            try:
                command1=command.encode('utf-8')
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect((self.HOST,self.PORT))
                self.s.sendall(command1)
                self.data=self.s.recv(1024)
                self.data=self.data.decode('utf-8').strip('\n')
                self.s.close()
                time.sleep(0.1)
                break
            except Exception as e:
                print(e)
                time.sleep(0.1)
                self.s.close()
                continue
#        self.s.close()