#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 19:10:03 2024

@author: kierapond
"""

from constants import *
import matplotlib.pyplot as plt

sigmax = np.array([[0,1],[1,0]])
sigmay = np.array([[0,-1j],[1j,0]])
sigmaz = np.array([[1,0],[0,-1]])
I = np.array([[1,0],[0,1]])

IxJx = np.tensordot(sigmax, sigmax, axes=0)
IyJy = np.tensordot(sigmay, sigmay, axes=0)
IzJz = np.tensordot(sigmaz, sigmaz, axes=0)

IxJxsq = np.tensordot(sigmax**2, sigmax**2, axes=0)
IyJysq = np.tensordot(sigmay**2, sigmay**2, axes=0)
IzJzsq = np.tensordot(sigmaz**2, sigmaz**2, axes=0)

JxI = np.tensordot(sigmax,I,axes=0)
JyI = np.tensordot(sigmay,I,axes=0)
JzI = np.tensordot(sigmaz,I,axes=0)

IIx = np.tensordot(I, sigmax, axes=0)
IIy = np.tensordot(I, sigmay, axes=0)
IIz = np.tensordot(I, sigmaz, axes=0)

IdotJ = IxJx + IyJy + IzJz

IJsq = IxJxsq + IyJysq + IzJzsq

J=3/2 

JxplusIx = gJ*JxI + gI*IIx
JyplusIy = gJ*JyI + gI*IIy
JzplusIz = gJ*JzI + gI*IIz

# Hhf = (ahfHzS/hbar**2) * IdotJ + (bhfHz/hbar**2)*((3*(IdotJ)**2 + (3/2)*(IdotJ) - IJsq) / (2*I*(2*I -1) *J*(2*J -1)))

def Hz(B):
	Hz = (muB/hbar)*(JxplusIx + JyplusIy + JzplusIz)*B

	
	fig = plt.figure(1)
	
	plt.plot(Hz,B)
	
	return fig 
