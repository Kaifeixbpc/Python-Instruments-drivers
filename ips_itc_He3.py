# -*- coding: utf-8 -*-
"""
Created on May 24 21:13:51 2018 by Kaifei Kang
Updated on Dec 05 2018 by Egon Sohn



## Need to test iTC 1 & 2. Check all the daughter board assignment and test one by one


"""
import datetime
import visa
rm=visa.ResourceManager()

class Mercury():

    def __init__(self):
        self.Mercury_itc = rm.open_resource('ASRL5::INSTR')                     # iTC FOR HE3 AND VTI
#        self.Mercury_itc2 = rm.open_resource('ASRL4::INSTR')                    # iTC FOR STANDARD PROBE
#        self.Mercury_ips = rm.open_resource('ASRL3::INSTR')             

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
        msg = self.Mercury_itc.query(value)
        print(msg)
    
    def itc2_write(self, value):
        msg = self.Mercury_itc2.query(value)
        print(msg)
        

    def ips_write(self, value):
        self.Mercury_ips.query(value)
        
## COMMANDS TO READ VALUE
## iTC 
    def get_VTI_temp(self):
        while True:
            try:
                Pot_T = self.Mercury_itc.query("READ:DEV:DB6.T1:TEMP:SIG:TEMP")
                Pot_T = Pot_T.split(":")[6].strip("K\n")
                break
            except:
                continue
        return Pot_T


    def get_VTI_heaterpower(self):
        VTI_P = self.Mercury_itc.query("READ:DEV:DB1.H1:HTR:SIG:POWR")
        VTI_P =VTI_P.split(":")[6].strip("W\n")
        return VTI_P 
            
    def get_Pressure(self):
        Pres = self.Mercury_itc.query("READ:DEV:DB3.P1:PRES:SIG:PRES")
        Pres = Pres.split(":")[6].strip("mB\n")
        return Pres
    
    def get_NV(self):
        Nvav = self.Mercury_itc.query("READ:DEV:DB4.G1:AUX:SIG:PERC")
        Nvav = Nvav.split(":")[6].strip("%\n")
        return Nvav    

    def get_He3_temp(self):
        
        command="READ:DEV:HelioxX:HEL:SIG:TEMP"
        return(self.query_command(command))
    
    def get_He3_status(self):
        Status = self.Mercury_itc.query("READ:DEV:HelioxX:HEL:SIG:STAT")
        Status = Status.split(":")[6].strip("\n")
        return Status
    
    def get_He3_Sorb_temp(self):
        command="READ:DEV:MB1.T1:TEMP:SIG:TEMP"
        return(self.query_command(command))
        
    def get_He3_Sorb_heaterpower(self):
        Sorb_P = self.Mercury_itc.query("READ:DEV:MB0.H1:HTR:SIG:POWR")
        Sorb_P = Sorb_P.split(":")[6].strip("W\n")
        return Sorb_P 
    
    def get_He3_1Kplate_temp(self):
        command="READ:DEV:DB5.T1:TEMP:SIG:TEMP"
        return(self.query_command(command))

    def get_He3_Rutemp(self):
        command="READ:DEV:DB8.T1:TEMP:SIG:TEMP"
        return(self.query_command(command))      

    def get_He3_Cxtemp(self):
        command="READ:DEV:DB7.T1:TEMP:SIG:TEMP"
        return(self.query_command(command))
    
    def get_He3_heaterpower(self):

        He3_P = self.Mercury_itc.query("READ:DEV:DB2.H1:HTR:SIG:POWR")
        He3_P = He3_P.split(":")[6].strip("W\n")
        return He3_P
    
## iTC2
    def get_Prob_temp(self):
        Prob_T = self.Mercury_itc2.query("READ:DEV:DB8.T1:TEMP:SIG:TEMP")
        Prob_T = Prob_T.split(":")[6].strip("K\n")
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
#        Mag_cur = Mag_cur.split(":")[6].strip("T\n")
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
       
    def set_VTI_temp(self, value):
        self.Mercury_itc.write("SET:DEV:DB5.T1:TEMP:LOOP:RENA:OFF")             # Check daughter board number
        self.Mercury_itc.write("SET:DEV:DB5.T1:TEMP:TSET:"+str(value))
    
    def set_He3_Sorb_temp(self, value):
        self.Mercury_itc.write("SET:DEV:DB5.T1:TEMP:LOOP:RENA:OFF")             # Check daughter board number
        self.Mercury_itc.write("SET:DEV:DB5.T1:TEMP:TSET:"+str(value))


    def set_pressure(self, value):
        self.Mercury_itc.query("SET:DEV:DB5.P1:PRES:LOOP:HSET:" + str(value))       ## DIDN't pass test
        
## iTC2
    def set_Prob_temp(self,value):
        self.Mercury_itc2.write("SET:DEV:DB8.T1:TEMP:LOOP:RENA:OFF")
        self.Mercury_itc2.write("SET:DEV:DB8.T1:TEMP:TSET:"+str(value))
    
    def set_Prob_temp_by_ramp(self, setT, rate):
        self.Mercury_itc2.write("SET:DEV:DB8.T1:TEMP:LOOP:RSET:" + str(rate))
        CurrentT = self.Mercury_itc.query("READ:DEV:DB8.T1:TEMP:SIG:TEMP")
        self.Mercury_itc2.write("SET:DEV:DB8.T1:TEMP:LOOP:TSET:"+str(CurrentT))
        self.Mercury_itc2.write("SET:DEV:DB8.T1:TEMP:LOOP:RENA:ON")
        self.Mercury_itc2.write("SET:DEV:DB8.T1:TEMP:LOOP:TSET:"+str(setT))

    def query_command(self,command):
        
        while True:
                try:
                    temp = self.Mercury_itc.query(command)
                    temp = float(temp.split(":")[6].strip("K\n"))
                    break
                except:
                    continue
        return temp        
        

    def closeall(self):
        self.Mercury_ips.close()
        self.Mercury_itc.close()
        
