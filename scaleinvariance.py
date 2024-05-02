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

def format_func(value):
    # find number of multiples of pi/2
    N = xvals 
    if N == 0:
        return "0"
    elif N == 1:
        return r"L"
    else:
        return r"${0}\pi$".format(N // 2)

# ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))

tickvals = [0,0.5,1]
ticktext = [0,"L/2","L"]

plt.vlines(0.5, 0, 1.1, linestyle='dashed',color='black')
ax.set_xlabel('x')
ax.set_ylabel('$\psi$')
ax.set_yticks([0])
# Set number of ticks for x-axis
ax.set_xticks(tickvals)
# Set ticks labels for x-axis
ax.set_xticklabels(ticktext)

