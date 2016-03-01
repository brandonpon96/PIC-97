#!/usr/bin/python

from scipy.optimize import minimize
from scipy.integrate import trapz
import random
import numpy as np
import pylab as plt
from sympy import *


P = float(pi)/2
z0 = range(50)
for g in range(50):
	z0[g] = random.random() * P

def getArea(array):
	limit = array[0]
	xaxis = np.linspace(0, limit, 50)
	dx = xaxis[1] - xaxis[0]
	area = trapz(array[1:],xaxis[:len(xaxis)-1])
	area = area + array[len(array)-1] * dx / 2
	return -1 * area

def perimeter(array):
	perim = 0.
	limit = array[0]
	xaxis = np.linspace(0, limit, 50)
	dx = xaxis[1] - xaxis[0]
	for ind in range(len(array[1:])) :
		perim = perim + ((array[ind+1] - array[ind])**2 + dx**2)**0.5
	perim = perim + (array[len(array)-1]**2 + dx**2)**0.5
	return perim - P

def bounds(array):
	return [(0,P) for x in array]

def types():
	return {'type':"eq", 'fun':perimeter}

min = minimize(getArea, z0, bounds = bounds(z0), constraints = types())
sol = min.x
limit = sol[0]
xaxis = np.linspace(0, limit, 50)
sol = sol[1:]
sol = np.append(sol, 0)

plt.axis('equal')
plt.title('Optimized Area')
plt.plot(xaxis, z0, 'r--', xaxis, sol, 'b-')
plt.show()





