#!/usr/bin/python

#Brandon Pon

import math

def f1(x):
	return x**2 -1

def f1p(x):
	return 2*x

def f2(x):
	return math.sin(x)

def f2p(x):
	return math.cos(x)

def f3(x):
	return math.log(x) - 1

def f3p(x):
	return 1.0 / x

def newton(x, toler, f, fp):

	y = f(x)
	yp = fp(x)
	x1 = x - y / float(yp)		
	x = x1
	while math.fabs(f(x1)) >= toler:
		y = f(x)
		yp = fp(x)
		x1 = x - y / float(yp)
		if 	math.fabs(f(x1)) < toler:
			break
		x = x1

	return x1


error = 0.0001
print newton(3, error, f1, f1p)
print newton(-.5, error, f1, f1p)
print newton(2, error, f2, f2p)
print newton(1.5, error, f3, f3p)