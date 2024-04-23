#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:20:33 2024

@author: kierapond
"""

from constants import *
import matplotlib.pyplot as plt

def pbox(n,x,L):
	return np.sin(n*x*np.pi/L)

xvals = np.linspace(0,1,1000)

fig, ax = plt.subplots(1)
plt.plot(xvals,pbox(1,xvals,1))

plt.vlines(0.5, 0, 1.1, linestyle='dashed',color='black')
ax.set_xlabel('x')
ax.set_ylabel('$\psi$')
ax.set_yticks([0])
ax.set_xticks([0])

