#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:55:20 2024

@author: kierapond
"""

from constants import * 
import matplotlib.pyplot as plt 

#Halmholtz is sep btw coils = radius ! 

def B(x,a,c):
	#here is really 2*B/mu*I*N = a^2 ( + ) 
	return a**2 * ( (a**2+(c-x)**2)**(-3/2) + (a**2+(c+x)**2)**(-3/2) )

#a is radius of coils along y axis 
#c is dist of coil to origin along x axis , so 2c = a for helholtz

def Bconst(x,c):
# 	c=0.5
#If we express  𝐵  in units of  𝜇𝑁𝐼/(2𝑎)  and  𝑐  and  𝑥  in units of  𝑎
#The coil separation is  2𝑐 , and distances are in units of the coil radius 𝑎 . 
#Notice that when  𝑐=0.5 , which means that the coil separation is equal to the coil 
#radius, the field is uniform over a large range, and this is the usefulness of the 
#Helmholtz arrangement for providing a uniform field.
	return (1+(c-x)**2)**(-3/2)+ (1+(c+x)**2)**(-3/2)

xvals = np.linspace(-1.5,1.5,1000)


plt.xlabel("x")
plt.ylabel('B*2/(mu*I)')
plt.plot(xvals,B(xvals,2,1)) 
