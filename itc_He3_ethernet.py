# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:22:58 2019

@author: lenovo
"""

# -*- coding: utf-8 -*-
"""
Created on May 24 21:13:51 2018 by Kaifei Kang
Updated on Dec 05 2018 by Egon Sohn



## Need to test iTC 1 & 2. Check all the daughter board assignment and test one by one


"""

import time
import socket

class Mercury():

    def __init__(self):
        self.HOST = '192.168.1.6'    # The remote host
        self.PORT = 7020   
        print(self.get_info())
## COMMANDS TO READ VALUE
        
        
    def get_info(self):
        HOST=self.HOST
        PORT=self.PORT
        command="READ:SYS:CAT"+'\n'
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST,PORT))
        self.s.sendall(str.encode(command))
        data=self.s.recv(1024)
        self.s.close() 
        return data
## iTC 
        
        
    def get_He3_status(self):
        purpose='status'
        command="READ:DEV:HelioxX:HEL:SIG:STAT"
        return(self.query_command(command,purpose))     
        
    def get_VTI_temp(self):
        purpose='temperature'
        command="READ:DEV:DB6.T1:TEMP:SIG:TEMP"
        return(self.query_command(command,purpose))

    def get_He3_temp(self):
        purpose='temperature'
        command="READ:DEV:HelioxX:HEL:SIG:TEMP"
        return(self.query_command(command,purpose))
    
    def get_He3_Sorb_temp(self):
        purpose='temperature'
        command="READ:DEV:MB1.T1:TEMP:SIG:TEMP"
        return(self.query_command(command,purpose))
        
    def get_He3_1Kplate_temp(self):
        purpose='temperature'
        command="READ:DEV:DB5.T1:TEMP:SIG:TEMP"
        return(self.query_command(command,purpose))

    def get_He3_Rutemp(self):
        purpose='temperature'
        command="READ:DEV:DB8.T1:TEMP:SIG:TEMP"
        return(self.query_command(command,purpose))      

    def get_He3_Cxtemp(self):
        purpose='temperature'
        command="READ:DEV:DB7.T1:TEMP:SIG:TEMP"
        return(self.query_command(command,purpose))
        
##############################################################################################

    def get_Pressure(self):
        purpose='pressure'
        command="READ:DEV:DB3.P1:PRES:SIG:PRES"
        return(self.query_command(command,purpose))
        
    def get_NV(self):
        purpose='needle_valve'
        command="READ:DEV:DB4.G1:AUX:SIG:PERC"
        return(self.query_command(command,purpose)) 

    def get_He3_Sorb_heaterpower(self):
        purpose='power'
        command="READ:DEV:MB0.H1:HTR:SIG:POWR"
        return(self.query_command(command,purpose))

    def get_VTI_heaterpower(self):
        purpose='power'
        command="READ:DEV:DB1.H1:HTR:SIG:POWR"
        return(self.query_command(command,purpose))
    
    def get_He3_heaterpower(self):
        purpose='power'
        command="READ:DEV:DB2.H1:HTR:SIG:POWR"
        return(self.query_command(command,purpose))

################################################################################################
## iTC    
    def set_NV(self, value):
        command="SET:DEV:DB3.P1:PRES:LOOP:FSET:" + str(value)
        self.set_command(command)

    
    def set_He3_temp(self, value):
        command="SET:DEV:HelioxX:HEL:SIG:TSET:" + str(value)
        self.set_command(command)
        
    def set_VTI_temp(self, value):
        command="SET:DEV:DB6.T1:TEMP:LOOP:RENA:OFF"            # Check daughter board number
        self.set_command(command)
        command="SET:DEV:DB6.T1:TEMP:LOOP:TSET:"+str(value)
        self.set_command(command)
        
    def set_He3_Sorb_temp(self, value):
        command="SET:DEV:DB5.T1:TEMP:LOOP:RENA:OFF"             # Check daughter board number
        self.set_command(command)
        command="SET:DEV:DB5.T1:TEMP:TSET:"+str(value)
        self.set_command(command)


    def set_pressure(self, value):
        command="SET:DEV:DB3.P1:PRES:LOOP:TSET:" + str(value) ## DIDN't pass test
        self.set_command(command)

    def set_VTI_temp_by_ramp(self, setT, rate):
        print(self.query_command("SET:DEV:DB6.T1:TEMP:LOOP:RSET:" + str(rate)))
        CurrentT = self.get_VTI_temp()
        print(self.query_command("SET:DEV:DB6.T1:TEMP:LOOP:TSET:"+str(CurrentT)))
        print(self.query_command("SET:DEV:DB6.T1:TEMP:LOOP:RENA:ON"))
        print(self.query_command("SET:DEV:DB6.T1:TEMP:LOOP:TSET:"+str(setT)))
        
################################################################################################################
    
        
        
    def query_command(self,command,purpose=None):
        
        while True:
            try:
                HOST=self.HOST
                PORT=self.PORT
                command=command+'\n'
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect((HOST,PORT))
                self.s.sendall(str.encode(command))
                data=self.s.recv(1024)
                self.s.close()
                
                data=data.decode('utf-8').strip('\n')
                if purpose=='temperature':
                    data=float(data.split(':')[6].strip('K'))
                elif purpose=='pressure':
                    data=float(data.split(':')[6].strip("mB\n"))
                elif purpose=='needle_valve':
                    data=float(data.split(':')[6].strip("%\n"))            
                elif purpose=='power':
                    data=float(data.split(':')[6].strip("W\n"))
                elif purpose=='status':
                    data=data.split(':')[6].strip("\n") 
                time.sleep(0.05)
                break
                
            except Exception as e:
#                print(e)
                time.sleep(0.1)
                self.s.close()
                continue
        return(data)
        
        
    def set_command(self,command):
        
        while True:
            try:
                HOST=self.HOST
                PORT=self.PORT
                command=command+'\n'
                command1=command.encode('utf-8')
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect((HOST,PORT))
                self.s.sendall(command1)
                self.data=self.s.recv(1024)
                self.data=self.data.decode('utf-8').strip('\n')
                self.s.close()
                time.sleep(0.1)
                break
            
            except Exception as e:
#                print(e)
                time.sleep(0.1)
                self.s.close()
                continue        


