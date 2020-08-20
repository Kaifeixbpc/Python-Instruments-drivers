# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:12:53 2018

@author: lenovo
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
V,I=np.loadtxt('R18,19_G0V_T1.5K_0T_1',skiprows=2,usecols=(1,2),unpack=True)
plt.plot(V,I)
#plt.semilogy(I,V)
#def fit(x,a,b,c):
#    return a*np.exp(b*np.sqrt(x))+c
#popt,popv = curve_fit(fit,I,V)
#print(popt)
#plt.plot(I,fit(I,*popt))