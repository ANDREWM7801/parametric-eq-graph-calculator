#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 16:21:29 2023

@author: andrewmarshall
"""

"""parameterised plotter"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
def t_list(start, end, step):
    num = np.linspace(start, end,(end-start)
                      *int(1/step)+1).tolist()
    return [round(i, 2) for i in num]

t_0 = int(input("first t value? "))
t_final = int(input("final t value "))
steps = int(input("steps between numbers? "))



f_t = input("x = f(t): ")
g_t = input("y = g(t): ")
h_t = input("z = h(t): ")

def x_funct(t):
    return eval(f_t, {'t': t, 'np': np})
def y_funct(t):
    return eval(g_t, {'t': t, 'np': np})
def z_funct(t):
    return eval(h_t, {'t': t, 'np': np})


x_values = ['']*steps
y_values = ['']*steps
z_values = ['']*steps
interval = (t_final - t_0)/steps
t = t_list(t_0, t_final, interval)

for i in range(steps):
    x_values[i] = x_funct(t[i])
    y_values[i] = y_funct(t[i])
    z_values[i] = z_funct(t[i])

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.plot(x_values, y_values, z_values)
plt.show()



''' 

*include list of basic functions 
*allow for retype of function if invalid
*use 2 or more variables

'''

