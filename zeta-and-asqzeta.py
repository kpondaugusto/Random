# %%
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 13:06:33 2024

@author: kierapond
"""

from constants import *
import matplotlib.pyplot as plt
import scipy.special as sc

def zeta(v):
	return v**2*(-1 - (1+v**2)*np.exp(v**2) * sc.expi(-v**2) )

def asqzeta(v):
	return np.log(1/(np.sqrt(2*np.pi) * np.abs(v)) ) +1

vvals = np.linspace(-1,1,10000)
vvals2 = np.linspace(-2,2,10000)

def add_subplot_axes(ax,rect,facecolor='w'):
    fig = plt.gcf()
    box = ax.get_position()
    width = box.width
    height = box.height
    inax_position  = ax.transAxes.transform(rect[0:2])
    transFigure = fig.transFigure.inverted()
    infig_position = transFigure.transform(inax_position)    
    x = infig_position[0]
    y = infig_position[1]
    width *= rect[2]
    height *= rect[3]  
    #subax = fig.add_axes([x,y,width,height],facecolor=facecolor)  # matplotlib 2.0+
    subax = fig.add_axes([x,y,width,height])
    x_labelsize = subax.get_xticklabels()[0].get_size()
    y_labelsize = subax.get_yticklabels()[0].get_size()
    x_labelsize *= rect[2]**0.5
    y_labelsize *= rect[3]**0.5
    subax.xaxis.set_tick_params(labelsize=x_labelsize)
    subax.yaxis.set_tick_params(labelsize=y_labelsize)
    return subax
    
def example1():
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    rect = [0.2,0.2,0.5,0.5]
    ax1 = add_subplot_axes(ax,rect)
    # ax2 = add_subplot_axes(ax1,rect)
    # ax3 = add_subplot_axes(ax2,rect)
    plt.show()

def example2():
    fig = plt.figure(figsize=(10,10))
    axes = []
    subpos = [0.2,0.6,0.3,0.3]
    x = np.linspace(-np.pi,np.pi)
    for i in range(1,4):
        axes.append(fig.add_subplot(2,2,i))
    for axis in axes:
        axis.set_xlim(-np.pi,np.pi)
        axis.set_ylim(-1,3)
        axis.plot(x,np.sin(x))
        subax1 = add_subplot_axes(axis,subpos)
        subax2 = add_subplot_axes(subax1,subpos)
        subax1.plot(x,np.sin(x))
        subax2.plot(x,np.sin(x))

def example3():
    fig = plt.figure(figsize=(14,10))
    axes = []
    subpos = [0.1,0.57,0.4,0.4]
    x = np.linspace(-np.pi,np.pi)
    for i in range(1,2): #2 is one plot, 3 is 2 plots beside each other, 4 is 3 plots, 5 is 4 plots ??
        axes.append(fig.add_subplot(2,2,i))
    for axis in axes:
        axis.set_xlim(-np.pi,np.pi)
        axis.set_ylim(-1,3)
        axis.plot(vvals2,zeta(vvals2))
        axis.text(0.8, 0.21, '$\zeta$', horizontalalignment='center', verticalalignment='center')
        axis.text(0.1, 0.225, '$1/a$', horizontalalignment='center', verticalalignment='center')
        axis.set_ylim(0,0.4)
        axis.set_xlim(-2,2)
        axis.set_xlabel('1/a')
        # axis.set_ylabel('Bulk Viscosity')

        subax1 = add_subplot_axes(axis,subpos)
        # subax2 = add_subplot_axes(subax1,subpos)
        subax1.plot(vvals,asqzeta(vvals))
        subax1.set_ylim(0,3)
        subax1.set_xlim(-1,1)
        subax1.text(0.5, 1.5, '$a^2\zeta$', horizontalalignment='center', verticalalignment='center')
		   # subax1.set_xlabel('v')

        # subax2.plot(x,np.sin(x))	
	
if __name__ == '__main__':
    example3()
    plt.show()
# plt.plot(vvals,asqzeta(vvals))
# plt.plot(vvals2,zeta(vvals2))

# plt.ylim()
# %%
