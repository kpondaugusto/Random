#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 09:52:31 2024

@author: kierapond
"""

from constants import *
import matplotlib.pyplot as plt

#lennard jones potential 
plt.style.use('dark_background')
sigma = 3
epsilon = 3.2

def Ulj(r):
 	return 4*epsilon*(sigma/(r)**12 -sigma/(r)**6 )

r = np.linspace(0.1,10,100) #interatomic distance

# plt.plot(r, Ulj(r))

# plt.show()

# Boltzmann's constant, J/K
kB = 1.381e-23

# The Lennard-Jones parameters:
A = 1.024e-23   # J.nm^6
B = 1.582e-26   # J.nm^12

# Adjust the units of A and B - they have more manageable values
# in K.nm^6 and K.nm^12
A, B = A / kB, B / kB

# Interatomic distance, in nm
r = np.linspace(0.3, 1, 1000)
# Interatomic potential
U = B/r**12 - A/r**6  
U2 = 2*B/r**12 - A/r**6  + 25

# Interatomic force
# F = 12*B/r**13 - 6*A/r**7

fig, ax = plt.subplots(1)

# ax.axhline(y=25, color='Pink', linestyle='dotted')
ax.hlines(y=6, xmin=0.385, xmax=0.57, linewidth=2, color='plum')
ax.vlines(x=0.45, ymin=0, ymax=6, linewidth=2, color='mediumpurple',label='Ec')
ax.vlines(x=0.9, ymin=-2, ymax=10, linewidth=2, color='darkslategrey',label='E')
ax.hlines(y=10, xmin=0.7, xmax=1, linewidth=2, color='steelblue')
ax.axhline(y=0, color='lightpink', linestyle='dotted')
ax.plot(r, U, 'k', lw=2, color='lightblue', label='Open Channel')
ax.plot(r, U2, 'k', lw=2, color='lavender', label='Closed ab Channel')
ax.set_xlabel('Atomic Seperation ')
ax.set_ylabel('Energy')
# ax.set_xlim(0, 0.8)
ax.set_ylim(-150, 100)
ax.set_yticks([0])
ax.set_xticks([0])
ax.legend()

plt.show()

#lowest energy potential from feshbach paper 
#without l(l+1) term since l=0 for swave

def lowenV(r):
	return -C/(r**6) 


B0 = 202.14 #G
Bzero = 209.07 #G
Boff = B0 - 0.04 #G

Bvals = np.linspace(Boff,-Boff,1000)

def scatteringswave(B):
	B = np.linspace(200.0, 210.0, 100)

	a97 = abg * (1 - (Bzero - B0)/(B - B0))
	
	threshold = 20
	a97[a97*kF>threshold] = np.nan
	a97[a97*kF<-threshold] = np.nan
	
	return a97

def feshbachswave():
	Bvalues = np.linspace(200.0, 210.0, 100)
	plt.xlabel('Magnetic Field (G)')
	plt.ylabel('kF*a (dim)')
	plt.plot(Bvalues, scatteringswave(Bvalues)*kF)