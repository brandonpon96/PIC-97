#!/usr/bin/python

from scipy.integrate import odeint
import numpy as np
import pylab as plt

m = 1
l = 1
g = 1

def calc(yvec, time, m, l, g):
	return (yvec[1], -g*np.sin(yvec[0])/l)


time_vec = np.linspace(0,10, 100)
yarr = odeint(calc, (1,0), time_vec, args = (m,l,g))

angle = [item[0] for item in yarr]
plt.plot(time_vec,angle)
plt.ylabel('angle (rad)')
plt.xlabel('time (t)')
plt.title('Pendulum Motion')
plt.show()

