#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 14:06:47 2024

@author: kierapond
"""

from constants import *
import matplotlib.pyplot as plt

lamdbaodt = 1064 #nm for odt
xchip = 8 #mm 
P = 10 #W 
omega0beam = 16 # microm beam waist
Gamma = 6.035 #(11) MHz K40 D2 
omega = 2*np.pi*c/lambdaodt#

vals = np.linspace(15,30,100)

def ztrap(omega0):
	return omega0*(1 + ((lamdbaodt*xchip)/(np.pi*omega0**2))**2 )**(1/2)

def ztrapplot():
	
	plt.xlabel('ztrap')
	plt.ylabel('beam waist')
	plt.plot(ztrap(vals),vals,'o')

#rayleigh range
def rZ():
	return omega0beam**2*np.pi/lambdaodt

def omegar(r):
	return omega0beam*(1+ (r/rZ())**2)**(1/2)

def Imax():
	return 2*P/(np.pi*omegar(vals)**2) 

def Vopt(omega0):
	return -3*np.pi*c**2*Gamma/(2*omega0)*(1/(omega0-omega) + 1/(omega0+omega))*Imax()

# r*np.pi*c/lambdaodt = 1770349.2173955387

omegavals = np.linspace(1770349-100,1770349+100,100)

def Voptplot():
	
	plt.plot(omegavals,Vopt(omegavals),'o')