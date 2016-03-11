from scipy.integrate import odeint
import numpy as np
import pylab as plt

m,l,g = (0,0, 9.8)
def calc(ypos, time, m, l, g):
	return -g * time + 10

time_vec = np.linspace(0,4,40)
yvec= odeint(calc, 0, time_vec,args=(m,l,g))

for i in range(len(yvec)):
	print time_vec[i], yvec[i]

plt.plot(time_vec, yvec)
plt.xlabel('hi')
plt.ylabel('dslk')
plt.title('titel')
plt.show()