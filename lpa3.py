#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:42:13 2024

@author: kierapond
"""

from constants import *
import matplotlib.pyplot as plt 

svals = np.linspace(0, 20, 10000)

def N2oN(s):
	return s/(1 + s) * 1/2

def DeltaNoN(s):
	return s/(1+s) - 1

fig = plt.figure(0)
# plt.xlabel('s')
# plt.ylabel('N2/N')
plt.plot(svals, N2oN(svals), color='lightblue',label='N2/N')
#

# fig01 = plt.figure(3)
plt.xlabel('Saturation Paramter')
plt.ylabel('Number Fraction')
# plt.plot(svals, DeltaNoN(svals), color='lightpink',label='$\Delta$N/N')
plt.legend()

def aoa0(x,I):
	return 1/(x**2 + 1 + I)

def IToIin(phi,R):
	F = 4*R/(1-R)**2
	
	return 1/(1 + F*(np.sin(phi/2))**2)

class Plots:
	def __init__(self,x,R,function):
		self.R = R
		self.x = x
		self.function = function
		
		self.xdata = self.x
		self.ydata = self.function(self.x,self.R)
		
	def plot(self):
		self.fig = plt.figure()
		self.ax = plt.subplot()
		self.ax.plot(self.xdata, self.ydata)
		
		self.ax.set_xlabel('$\phi$ (rad)')
		self.ax.set_ylabel('$I_T/I_{in}$')

rvals = [0.1,0.9,0.99]

fig1 = plt.figure(1)
plt.xlabel('$\phi$ (rad)')
plt.ylabel('$I_T/I_{in}$')
plt.plot(svals,IToIin(svals,0.1),label='R=0.1')
plt.plot(svals,IToIin(svals,0.9),label='R=0.9')
plt.plot(svals,IToIin(svals,0.99),label='R=0.99')
plt.legend()

svals2 = np.linspace(-10,10,1000)

fig2 = plt.figure(2)
plt.xlabel('Detuning/$\Gamma$')
plt.ylabel('a($\\nu$)/a$_0$($\\nu_0$)')
plt.plot(svals2,aoa0(svals2,0),label='$I/I_{sat}$=0')
plt.plot(svals2,aoa0(svals2,0.1),label='$I/I_{sat}$=0.1')
plt.plot(svals2,aoa0(svals2,1),label='$I/I_{sat}$=1')
plt.plot(svals2,aoa0(svals2,10),label='$I/I_{sat}$=10')
plt.plot(svals2,aoa0(svals2,100),label='$I/I_{sat}$=100')

plt.legend()

def IoIin(x,R,L=1,k=1):
	return (1-R)*(1-(R)**(1/2))**2/((1-R)**2 + 4*R*(np.sin(k*L)**2)) * (1 + 4*(R)**(1/2)/(1-R**(1/2))**2 *(np.sin(k*(L-x)))**2 )

rvals = [0.1,0.9,0.99]
# svals = np.linspace(0,5,1000)
fig3 = plt.figure(3)
plt.xlabel('kx')
plt.ylabel('$I_T/I_{in}$')
plt.plot(svals,IoIin(svals,0.1),label='R=0.1')
plt.plot(svals,IoIin(svals,0.9),label='R=0.9')
plt.plot(svals,IoIin(svals,0.99),label='R=0.99')
plt.legend()

def IoIin(x,A):
	return A * (1 - (np.sin(x))**2 )

rvals = [0.1,0.9,0.99]

fig4 = plt.figure(4)
plt.xlabel('$\phi(x)$')
plt.ylabel('$I_T$')
plt.plot(svals,IoIin(svals,0.01)+1,label='A=0.01')
plt.plot(svals,IoIin(svals,1)*0.5 +0.5,label='A=1')
# plt.legend()

# for i in rvals:
# 	Plots(svals, i, IToIin).plot()
L=1

rvals = np.linspace(0,1,100)

def vc(r):
	return (1-r)*(1+r)/(8*np.pi)*c/L
fig5 = plt.figure(5)

plt.plot(rvals,vc(rvals))

fig6 = plt.figure(6)
plt.plot(rvals, 1-rvals)

lambda2 = 767 
nu =  c/ lambda2

def gog0(x,A):
	return (1 + (A *(1 - (np.sin(x))**2) )  )**(-1)

svals = np.linspace(0,10,100000)

fig7 = plt.figure(7)
plt.xlabel('$\phi(x)$')
plt.ylabel('$g/g_0$')
plt.plot(svals,gog0(svals,0.01),label='$AI_{in}/I_{v}^{sat}$=0.01')
plt.plot(svals,gog0(svals,1),label='$AI_{in}/I_{v}^{sat}$=1')
plt.legend()