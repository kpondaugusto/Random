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


def qp(C):
	return ((C-1)*qs + np.sqrt((C-1)**2*qs**2 + 4*qs))/2

def qm(C):
	return ((C-1)*qs - np.sqrt((C-1)**2*qs**2 + 4*qs))/2
plt.figure(0)

plt.xlabel('C')
plt.ylabel('q')
plt.plot(Cvalsp,qp(Cvalsp),label='plus')
plt.plot(Cvalsm,qm(Cvalsm),label='minus')
plt.legend()

plt.figure(1)

plt.xlabel('C')
plt.ylabel('q')
plt.loglog(Cvals,qp(Cvals),label='plus')
plt.loglog(Cvals,qm(Cvals),label='minus')
# plt.legend()
