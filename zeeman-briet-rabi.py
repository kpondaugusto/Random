#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 19:10:03 2024

@author: kierapond
"""

from constants import *

sigmax = np.array([[0,1],[1,0]])
sigmay = np.array([[0,-1j],[1j,0]])
sigmaz = np.array([[1,0],[0,-1]])

IxJx = np.tensordot(sigmax, sigmax, axes=0)
IyJy = np.tensordot(sigmay, sigmay, axes=0)
IzJz = np.tensordot(sigmaz, sigmaz, axes=0)

IdotJ = IxJx + IyJy + IzJz

print(IdotJ)