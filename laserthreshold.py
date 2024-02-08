#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 19:52:20 2024

@author: kierapond
"""

from constants import *
import matplotlib.pyplot as plt

qs = 10**7

Cvalsm = np.linspace(0,1,10)
Cvalsp = np.linspace(1,3,10)

Cvals = np.linspace(0,3,10000)
Cvals1 = np.linspace(1.0001,3,1000)


def qp(C):
	return ((C-1)*qs + np.sqrt( ((C-1)**2)*(qs**2) + 4*qs*C))/2

def qm(C):
	return ((C-1)*qs - np.sqrt((C-1)**2*qs**2 + 4*qs*C))/2
plt.figure(0)

plt.xlabel('C')
plt.ylabel('q')
plt.plot(Cvals,qp(Cvals),'g-',label='qp')
plt.plot(Cvals,qm(Cvals),'r--',label='qm')
plt.legend()

plt.figure(1)
plt.yscale('log')
plt.xlabel('C')
plt.ylabel('log(q)')
plt.plot(Cvals,qp(Cvals),label='qp')
plt.plot(Cvals,np.abs(qm(Cvals)),label='abs(qm)')
plt.legend()
