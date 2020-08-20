# -*- coding: utf-8 -*-
"""
Created on May 24 21:13:51 2018 by Kaifei Kang
Updated on Dec 05 2018 by Egon Sohn



## Need to test iTC 1 & 2. Check all the daughter board assignment and test one by one


"""
import datetime
import visa
rm=visa.ResourceManager()
import time
class Mercury():

    def __init__(self):
        self.Mercury_itc = rm.open_resource('ASRL6::INSTR')                     # iTC FOR HE3 AND VTI
#        self.Mercury_itc2 = rm.open_resource('ASRL4::INSTR')                    # iTC FOR STANDARD PROBE
#        self.Mercury_ips = rm.open_resource('ASRL5::INSTR')             
#
#        self.Mercury_ips.read_termination="\r"

    def get_ipscat(self):
        text = self.Mercury_ips.query("READ:SYS:CAT")
        return text
    
    def get_itccat(self):
        text = self.Mercury_itc.query("READ:SYS:CAT")
        return text
    
    def get_itc2cat(self):
        text = self.Mercury_itc2.query("READ:SYS:CAT")
        return text
    
    def get_time(self):
        x1 = self.Mercury_ips.query("READ:SYS:TIME")
        x11 = x1.strip("\n").split(":")[3:]
        x2 = self.Mercury_ips.query("READ:SYS:DATE")
        x22 = x2.strip("\n").split(":")[3:]
        x22.extend(x11)
        time_now = datetime.datetime(int(x22[0]),int(x22[1]),int(x22[2]),int(x22[3]),int(x22[4]),int(x22[5]))
        return time_now
    
    def itc_write(self, value):
        self.Mercury_itc.query(value)
        
    def itc2_write(self, value):
        self.Mercury_itc2.query(value)

    def ips_write(self, value):
        self.Mercury_ips.query(value)
        
## COMMANDS TO READ VALUE
## iTC 
    def get_VTI_temp(self):

        while True:
            try:
                VTI_T = self.Mercury_itc.query("READ:DEV:MB1.T1:TEMP:SIG:TEMP")
                VTI_T = VTI_T.split(":")[6].strip("K\n")
                VTI_T=float(VTI_T)
                break
            except:
                continue
        return VTI_T

    def get_VTI_heatPower(self):
        VTI_P = self.Mercury_itc.query("READ:DEV:MB0.H1:HTR:SIG:POWR")
        VTI_P =VTI_P.split(":")[6].strip("W\n")
        return VTI_P 
            
    def get_Pressure(self):
        Pres = self.Mercury_itc.query("READ:DEV:DB5.P1:PRES:SIG:PRES")
        Pres = Pres.split(":")[6].strip("mB\n")
        return Pres
    
    def get_NV(self):
        Nvav = self.Mercury_itc.query("READ:DEV:DB4.G1:AUX:SIG:PERC")
        Nvav = Nvav.split(":")[6].strip("%\n")
        return Nvav    

    def get_He3_temp(self):
        He3_T = self.Mercury_itc.query("READ:DEV:HelioxX:HEL:SIG:TEMP")
        He3_T = He3_T.split(":")[6].strip("K\n")
        return He3_T
    
    def get_He3_status(self):
        Status = self.Mercury_itc.query("READ:DEV:HelioxX:HEL:SIG:STAT")
        return Status

## iTC2
    def get_Prob_temp(self):

        while True:
            try:
                Prob_T = self.Mercury_itc.query("READ:DEV:DB8.T1:TEMP:SIG:TEMP")
                Prob_T = Prob_T.split(":")[6].strip("K\n")
                Prob_T=float(Prob_T)
                break
            except:
                continue
        return Prob_T
    
    def get_Prob_heatPower(self):
        Prob_P = self.Mercury_itc2.query("READ:DEV:DB3.H1:HTR:SIG:POWR")
        Prob_P =Prob_P.split(":")[6].strip("W\n")
        return Prob_P 

##iPS
    def get_Mag_temp(self):
        Mag_T = self.Mercury_ips.query("READ:DEV:MB1.T1:TEMP:SIG:TEMP")
        Mag_T = Mag_T.split(":")[6].strip("K\n")
        return Mag_T
    
    def get_PT2_temp(self):
        PT2_T = self.Mercury_ips.query("READ:DEV:DB7.T1:TEMP:SIG:TEMP")
        PT2_T = PT2_T.split(":")[6].strip("K\n")
        return PT2_T
    
    def get_PT1_temp(self):
        PT1_T = self.Mercury_ips.query("READ:DEV:DB8.T1:TEMP:SIG:TEMP")
        PT1_T = PT1_T.split(":")[6].strip("K\n")
        return PT1_T
    
    def get_Mag_curr(self):
        Mag_cur = self.Mercury_ips.query("READ:DEV:PSU.M1:PSU:SIG:CURR")
        Mag_cur = Mag_cur.split(":")[6].strip("A\n")
        return Mag_cur

    def get_Mag_Field(self):
        Mag_cur = self.Mercury_ips.query("READ:DEV:GRPZ:PSU:SIG:FLD")
        Mag_cur = Mag_cur.split(":")[6].strip("T\n")
        return Mag_cur

    def get_persistant_Field(self):
        Mag_cur = self.Mercury_ips.query("READ:DEV:GRPZ:PSU:SIG:PFLD")
        Mag_cur = Mag_cur.split(":")[6].strip("T\n")
        return Mag_cur

#####   COMMANDS TO SET VALUE
## iTC    
    def set_NV(self, value):
        self.Mercury_itc.query("SET:DEV:DB5.P1:PRES:LOOP:FSET:" + str(value))
    
    def set_He3_temp(self, value):
        self.Mercury_itc.query("SET:DEV:HelioxX:HEL:SIG:TSET:" + str(value))

#    def set_pressure(self, value):
#        self.Mercury_itc.query("SET:DEV:DB5.P1:PRES:LOOP:HSET:" + str(value))       ## DIDN't pass test
        
## iTC2
    def set_Prob_temp(self,value):
        
        self.Mercury_itc.query("SET:DEV:DB8.T1:TEMP:LOOP:RENA:OFF")
        self.Mercury_itc.query("SET:DEV:DB8.T1:TEMP:LOOP:TSET:"+str(value))
        time.sleep(0.05)
    
    def set_VTI_temp(self,value):
        self.Mercury_itc.query("SET:DEV:MB1.T1:TEMP:LOOP:RENA:OFF")
        self.Mercury_itc.query("SET:DEV:MB1.T1:TEMP:LOOP:TSET:"+str(value))        
        time.sleep(0.05)
    
    def set_Prob_temp_by_ramp(self, setT, rate):
        print(self.Mercury_itc.query("SET:DEV:DB8.T1:TEMP:LOOP:RSET:" + str(rate)))
        CurrentT = self.get_Prob_temp()
        print(self.Mercury_itc.query("SET:DEV:DB8.T1:TEMP:LOOP:TSET:"+str(CurrentT)))
        print(self.Mercury_itc.query("SET:DEV:DB8.T1:TEMP:LOOP:RENA:ON"))
        print(self.Mercury_itc.query("SET:DEV:DB8.T1:TEMP:LOOP:TSET:"+str(setT)))
        
#        print(self.Mercury_itc.query("SET:DEV:MB1.T1:TEMP:LOOP:RSET:" + str(rate)))
#        print(self.Mercury_itc.query("SET:DEV:MB1.T1:TEMP:LOOP:TSET:"+str(float(CurrentT)-0.2)))
#        print(self.Mercury_itc.query("SET:DEV:MB1.T1:TEMP:LOOP:RENA:ON"))
#        print(self.Mercury_itc.query("SET:DEV:MB1.T1:TEMP:LOOP:TSET:"+str(float(setT)-0.2)))

##iPS
    def set_Mag_Field(self,field,rate):
        print(self.Mercury_ips.query("SET:DEV:GRPZ:PSU:SIG:FSET:"+str(field)))
        print(self.Mercury_ips.query("SET:DEV:GRPZ:PSU:SIG:RFST:"+str(rate)))
        print(self.Mercury_ips.query("SET:DEV:GRPZ:PSU:ACTN:RTOS:VALID"))

    def set_Mag_Zero(self,rate):
        self.Mercury_ips.write("SET:DEV:GRPZ:PSU:SIG:RFST:"+str(rate))
        self.Mercury_ips.write("SET:DEV:GRPZ:PSU:ACTN:RTOZ:VALID")    
    
    def set_Mag_Hold(self):
        print(self.Mercury_ips.query("SET:DEV:GRPZ:PSU:ACTN:HOLD:VALID"))

        

    def closeall(self):
        self.Mercury_ips.close()
        self.Mercury_itc.close()
        
