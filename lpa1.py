#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 17:41:33 2024

@author: kierapond
"""

import matplotlib.pyplot as plt
import numpy as np 

c = 299792458 # m (s^-1) -- speed of light 
h = 6.62607015e-34 # J s
hbar = h/(2*np.pi) # J s -- Planck's constant
kB = 1.380649e-23 #J (K^-1) -- Boltzman's constant new exact value 


nuvalues = np.linspace(.001,5000000,1000)

def blackbodyspectraldengh(v,T):
	return (8*np.pi*v**2)/(c**3)*(h*v)/(np.exp((h*v*10**9/(kB*T))-1))*10**(-27)

def blackbodyspectraldenth(v,T):
	return (8*np.pi*v**2)/(c**3)*(h*v)/(np.exp((h*v*10**12/(kB*T))-1))*10**(-36)

def blackbodyspectralden(v,T):
	return (8*np.pi*v**2)/(c**3)*(h*v)/(np.exp((h*v*10**9/(kB*T))-1))*10**(-27)

def blackbodyrad(wavelen,T):
	return ((2*np.pi*h*c**2)/(wavelen**5))*(1/(np.exp(((h*c)/(kB*T))*(1/(wavelen*10**(-9))))-1))*10**(45)

def blackbodyradmm(wavelen,T):
	return ((2*np.pi*h*c**2)/(wavelen**5))*(1/(np.exp(((h*c)/(kB*T))*(1/(wavelen*10**(-3))))-1))*10**(15)

def blackbodyradum(wavelen,T):
	return ((2*np.pi*h*c**2)/(wavelen**5))*(1/(np.exp(((h*c)/(kB*T))*(1/(wavelen*10**(-6))))-1))*10**(30)

def x(v):
	return 1/v**5*1/np.exp(1/v)

def nuplots():
	
	figall, axs = plt.subplots(2, 2)

	nuvalues = np.linspace(.001,1000,1000)
	axs[0,1].plot(nuvalues,blackbodyspectraldengh(nuvalues,2.7),label='CMB Temp')
	axs[0,1].set_xlabel('Frequency (GHz)')
	axs[0,1].set_ylabel('Spectral energy density (J/m3-GHz)')
	axs[0,1].yaxis.set_label_coords(-0.1, 0)
	axs[0,1].legend()
	nuvalues = np.linspace(1,100,1000)
	axs[0,0].plot(nuvalues,blackbodyspectraldenth(nuvalues,298.15),label='Room Temp')
	axs[0,0].set_xlabel('Frequency (THz)')
	axs[0,0].set_ylabel('Spectral energy density (J/m3-THz)')
	axs[0,0].yaxis.set_label_coords(-0.1, 0)
	axs[0,0].legend()
	nuvalues = np.linspace(1,1300,1100)
	axs[1,0].plot(nuvalues,blackbodyspectraldenth(nuvalues,6000),label='Sun Temp')	
	axs[1,0].set_xlabel('Frequency (THz)')
	axs[1,0].legend()	
	
# 	axs[1,1].plot(nuvalues,blackbodyspectraldengh(nuvalues,2.7),label='CMB Temp')
# 	nuvalues = np.linspace(1,100,1000)
# 	axs[1,1].plot(nuvalues/100,blackbodyspectraldenth(nuvalues,298.15)/1000000,label='Room Temp')
# 	nuvalues = np.linspace(1,1300,1100)
# 	axs[1,1].plot(nuvalues,blackbodyspectraldenth(nuvalues,6000),label='Sun Temp')
# 	axs[1,1].legend()
	
	plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
	plt.grid(False)
# 	figall.supxlabel('Spectral energy density (J/m3 Hz)')
# 	figall.supylabel('Frequency (nHz)')
	
	plt.subplots_adjust(left=0.13,
                    bottom=0.12, 
                    right=1, 
                    top=0.9, 
                    wspace=0.3, 
                    hspace=0.45)
	return figall

def lambdaplots():
	
	figall, axs = plt.subplots(2, 2)

	nuvalues = np.linspace(.1,5,1000)
	axs[0,1].plot(nuvalues,blackbodyradmm(nuvalues,2.7),label='CMB Temp')
	axs[0,1].set_xlabel('Wavelength (mm)')
	axs[0,1].set_ylabel('Spectral energy density (J/m3-mm)')
	axs[0,1].yaxis.set_label_coords(-0.2, 0)
	axs[0,1].legend()
	nuvalues = np.linspace(100,40000,1000)
	axs[0,0].plot(nuvalues,blackbodyrad(nuvalues,298.15),label='Room Temp')
	axs[0,0].set_xlabel('Wavelength (um)')
	axs[0,0].set_ylabel('Spectral energy density (J/m3-nm)')
	axs[0,0].yaxis.set_label_coords(-0.1, 0)
	axs[0,0].legend()
	nuvalues = np.linspace(1,1200,1000)
	axs[1,0].plot(nuvalues,blackbodyrad(nuvalues,6000),label='Sun Temp')
	axs[1,0].set_xlabel('Wavelength (nm)')
	axs[1,0].legend()	
	nuvalues = np.linspace(1,5000000,1000)	
# 	axs[1,1].plot(nuvalues,blackbodyrad(nuvalues,2.7)*10**(14),label='CMB Temp')
# 	axs[1,1].plot(nuvalues,blackbodyrad(nuvalues,298.15)*10**(6),label='Room Temp')
# 	axs[1,1].plot(nuvalues,blackbodyrad(nuvalues,6000),label='Sun Temp')
# 	axs[1,1].legend()	
	plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
	plt.grid(False)
# 	figall.supylabel('Spectral energy density (J/m3 nm)') # michael wouldn't update matplotlib so this wont work on his comp
# 	figall.supxlabel('Wavelength (nm)')

	plt.subplots_adjust(left=0.14,
                    bottom=0.12, 
                    right=1.3, 
                    top=0.9, 
                    wspace=0.3, 
                    hspace=0.45)

	
		
	return figall

def wavelengths():
	nuvalues = np.linspace(.1,5,1000)
	wavelengthcmb = (blackbodyradmm(nuvalues,2.7).tolist()).index(max(blackbodyradmm(nuvalues,2.7)))
	nuvalues = np.linspace(100,40000,1000)
	wavelengthroom = (blackbodyrad(nuvalues,298.15).tolist()).index(max(blackbodyrad(nuvalues,298.15)))
	nuvalues = np.linspace(1,1200,1000)
	wavelengthsun = (blackbodyrad(nuvalues,6000).tolist()).index(max(blackbodyrad(nuvalues,6000)))
		
	
	return wavelengthcmb, wavelengthroom, wavelengthsun

def nus():
	nuvalues = np.linspace(.001,1000,1000)
	wavelengthcmb = (blackbodyspectraldengh(nuvalues,2.7).tolist()).index(max(blackbodyspectraldengh(nuvalues,2.7)))
	nuvalues = np.linspace(1,100,1000)
	wavelengthroom = (blackbodyspectraldenth(nuvalues,298.15).tolist()).index(max(blackbodyspectraldenth(nuvalues,298.15)))
	nuvalues = np.linspace(1,1300,1100)
	wavelengthsun = (blackbodyspectraldenth(nuvalues,6000).tolist()).index(max(blackbodyspectraldenth(nuvalues,6000)))
		
	
	return wavelengthcmb, wavelengthroom, wavelengthsun
