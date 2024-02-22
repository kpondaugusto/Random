#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 14:06:47 2024

@author: kierapond

Modelling an optical dipole trap for the chip lab experiment 
"""

from constants import *
import matplotlib.pyplot as plt

lamdbaodt = 1064 #nm ; wavelength for odt
xchip = 8 #mm ; 1/2 length of chip 
P = 10 #W ; power of odt laser 
omega0beam = 16*10**(-6) # microm ; beam waist
Gamma = 6.035*10**(3) #(11) MHz K40 D2 
omega = 2*np.pi*c/lambdaodt #freq of light 

vals = np.linspace(15,30,10)

#distance of beam waist from chip

def ztrap(omega0):
	return omega0*(1 + ((lamdbaodt*xchip)/(np.pi*omega0**2))**2 )**(1/2)

#for omega0 = 16um beam waist ztrap >/= 170 um

def ztrapplot():
	
	plt.xlabel('ztrap (um?)')
	plt.ylabel('beam waist (um)')
	plt.plot(ztrap(vals),vals,'o')

#rayleigh range
def rZ():
	return omega0beam**2*np.pi/lambdaodt

def omegar(r):
	return omega0beam*(1+ (r/rZ())**2)**(1/2)

#r 

#max intensity of a focussed gaussian laser beam 

vals = np.linspace(15,30,100)

def Imax():
	return 2*P/(np.pi*omega0beam**2) 

def rho():
	return np.sqrt(r1**2 + r2**2)

def I():
	return 2*P/(np.pi*omegar(vals)**2) * np.exp(-2*(rho-rho0)**2/omega0beam**2)

#rho0 is the location of the beam focus 

#potential for odt 

def Vopt(omega0):
	return -3*np.pi*c**2*Gamma/(2*omega0**3)*(1/(omega0-omega) + 1/(omega0+omega))*Imax()


print('trap depth is',Vopt(1770349))
#omega0 res freq, omega freq light 

# r*np.pi*c/lambdaodt = 1770349.2173955387 ?? 

omegavals = np.linspace(omega-100,omega+100,100)

def Voptplot():
	
	plt.xlabel('resonant freq (hz?)')
	plt.ylabel('potential (J)')
	plt.plot(omegavals,Vopt(omegavals),'o')