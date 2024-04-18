#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:35:03 2024

@author: kierapond
"""

from constants import *
import matplotlib.pyplot as plt 

def Ibar(x):
	return c*epsilon0/2*np.exp(-2*x**2)*(8*x**2 +1)

def Iosc(x):
	return epsilon0/2*np.exp(-2*x**2)*4*np.sqrt(2)*x

def f(x):
	return np.exp(-x**2/2)*(1 - 2*x**2)

def g(x):
	return np.exp(-x**2/2)*2*np.sqrt(2)*x

def plotting(name,name2):
	xvals = np.linspace(-10,10,100)
	
	plt.ylabel(f'{name2}/|A$_{00}|^2$')
	plt.xlabel('x/$\omega_0$')
	plt.plot(xvals, name(xvals))