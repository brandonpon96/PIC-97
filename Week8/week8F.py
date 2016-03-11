#!/usr/bin/python

from scipy.integrate import odeint
import numpy as np
import pylab as plt

m = 1
l = 1
g = 9.81

# def calc(yvec, time, m, l, g):
# 	return (yvec[1], -g*np.sin(yvec[0])/l)

def calc(yvec, time, l, g):
	return -g #* time + 10

time_vec = np.linspace(0,2.04, 100)
yarr = odeint(calc, 0, time_vec, args = (l, g))

angle = [item[0] for item in yarr]
plt.plot(time_vec,angle)
plt.ylabel('angle (rad)')
plt.xlabel('time (t)')
plt.title('Pendulum Motion')
plt.show()

# a = g
# v = -gt + v
# x = x0 + vt -g * t^2/2

