# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 09:53:29 2019

@author: kaife
"""
import numpy as np
import time
from tkinter import *
from tkinter import ttk
import tkinter.filedialog as tf
import matplotlib.pyplot as plt
import tkinter.messagebox as tm
import sys
import socket
import ips_ethernet
ips=ips_ethernet.ips()
sys.path.append(b'C:\Users\kaife\Desktop\Instruments')


root = Tk()
root.title("Shan and Mak Lab Measurement System")
root.geometry('1200x800')
root.configure(bg='black')
f1= Frame(root,width=1200, height=800,bg='black')
def printhello():
    print('hello')

magtemp=0
field=0

#### aquire data
def get_temp():
    global magtemp
    while True:
        try:
            magtemp=ips.get_magtemp()
            break
        except socket.error as msg:
            time.sleep(5)
            continue
    f1.after(5000,get_temp)
    
def get_field():
    global field
    while True:
        try:
            field=ips.get_field()
            break
        except socket.error as msg:
            time.sleep(5)
            continue
    f1.after(5000,get_field)
    
####labels magfield
def labels():

    l1=Label(f1,text="Magnetic field:",fg='red',bg='black',font=("Helvetica", 120))
    l1.grid(row=1,column=0)
    l2=Label(f1,text=str(field)+" Tesla",fg='red',bg='black',font=("Helvetica", 120))
    l2.grid(row=2,column=0)
    ###labels temperature
    l3=Label(f1,text="Manget T: ",fg='yellow',bg='black',font=("Helvetica", 30))
    l3.grid(row=20,column=0)
    l4=Label(f1,text=str(magtemp)+" Kelvin",fg='yellow',bg='black',font=("Helvetica", 30))
    l4.grid(row=21,column=0)
    f1.after(1000,labels)
#####buttons
#    b1=Button(f1,text="Manget T: ",fg='yellow',bg='black',font=("Helvetica", 30),command=lambda:printhello())
#    b1.grid(row=23,column=0)




if __name__ == '__main__':
    f1.grid(pady=200, padx=300)
    get_field()
    get_temp()
    labels()
    root.mainloop()


