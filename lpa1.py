#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 17:41:33 2024

@author: kierapond
"""

import matplotlib.pyplot as plt
from constants import *

nuvalues = np.linspace(.001,5000000,1000)

def blackbodyspectralden(v,T):
	return (8*np.pi*v**2)/(c**3)*(h*v)/(np.exp((h*v)/(kB*T*10**(-9)))-1)*10**(45)

def blackbodyspectralden2(v,T):
	return (8*np.pi*v**2)/(c**3)*(h*v)/(np.exp((h*v)/(kB*T))-1)

def blackbodyrad(wavelen,T):
	return ((2*np.pi*h*c**2)/(wavelen**5))*(1/(np.exp(((h*c)/(kB*T))*(1/(wavelen*10**(-9))))-1))*10**(45)

def x(v):
	return 1/v**5*1/np.exp(1/v)


# plt.xlabel('')
# plt.plot(nuvalues,blackbodyrad(nuvalues,6000))
def nuplots():
	
	figall, axs = plt.subplots(2, 2)

	nuvalues = np.linspace(.001,1000,1000)
	axs[0,0].plot(nuvalues,blackbodyspectralden(nuvalues,2.7),label='CMB Temp')
	nuvalues = np.linspace(1,12*10**4,1000)
	axs[0,1].plot(nuvalues,blackbodyspectralden(nuvalues,298.15),label='Room Temp')
	nuvalues = np.linspace(1,15*10**5,1000)
	axs[1,0].plot(nuvalues,blackbodyspectralden(nuvalues,6000),label='Sun Temp')	
	
	axs[1,1].plot(nuvalues,blackbodyspectralden(nuvalues,2.7)*10**(14),label='CMB Temp')
	axs[1,1].plot(nuvalues,blackbodyspectralden(nuvalues,298.15)*10**(4),label='Room Temp')
	axs[1,1].plot(nuvalues,blackbodyspectralden(nuvalues,6000),label='Sun Temp')
	
	plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
	plt.grid(False)
	figall.supxlabel('Spectral energy density (J/m3 Hz)')
	figall.supylabel('Frequency (nHz)')
	
	plt.subplots_adjust(left=0.13,
                    bottom=0.12, 
                    right=1, 
                    top=0.9, 
                    wspace=0.1, 
                    hspace=0.45)
	return figall

def lambdaplots():
	
	figall, axs = plt.subplots(2, 2)

	nuvalues = np.linspace(100000,5000000,1000)
	axs[0,0].plot(nuvalues,blackbodyrad(nuvalues,2.7),label='CMB Temp')
	wavelengthcmb = (blackbodyrad(nuvalues,2.7).tolist()).index(max(blackbodyrad(nuvalues,2.7)))
	nuvalues = np.linspace(1,60000,1000)
	axs[0,1].plot(nuvalues,blackbodyrad(nuvalues,298.15),label='Room Temp')
	wavelengthroom = (blackbodyrad(nuvalues,298.15).tolist()).index(max(blackbodyrad(nuvalues,298.15)))
	nuvalues = np.linspace(1,1200,1000)
	axs[1,0].plot(nuvalues,blackbodyrad(nuvalues,6000),label='Sun Temp')	
	wavelengthsun = (blackbodyrad(nuvalues,6000).tolist()).index(max(blackbodyrad(nuvalues,6000)))
	nuvalues = np.linspace(1,5000000,1000)	
	axs[1,1].plot(nuvalues,blackbodyrad(nuvalues,2.7)*10**(14),label='CMB Temp')
	axs[1,1].plot(nuvalues,blackbodyrad(nuvalues,298.15)*10**(4),label='Room Temp')
	axs[1,1].plot(nuvalues,blackbodyrad(nuvalues,6000),label='Sun Temp')
	
	plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
	plt.grid(False)
	figall.supylabel('Spectral energy density (J/m3 nm)')
	figall.supxlabel('Wavelength (nm)')

	plt.subplots_adjust(left=0.14,
                    bottom=0.12, 
                    right=1.3, 
                    top=0.9, 
                    wspace=0.15, 
                    hspace=0.45)

	
		
	return figall

def wavelengths():
	nuvalues = np.linspace(100000,5000000,1000)
	wavelengthcmb = (blackbodyrad(nuvalues,2.7).tolist()).index(max(blackbodyrad(nuvalues,2.7)))
	nuvalues = np.linspace(1,60000,1000)
	wavelengthroom = (blackbodyrad(nuvalues,298.15).tolist()).index(max(blackbodyrad(nuvalues,298.15)))
	nuvalues = np.linspace(1,1200,1000)
	wavelengthsun = (blackbodyrad(nuvalues,6000).tolist()).index(max(blackbodyrad(nuvalues,6000)))
		
	
	return wavelengthcmb, wavelengthroom, wavelengthsun
