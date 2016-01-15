#!/usr/bin/python

def mydivide1(a, b):
	return [float(x)/y for x,y in zip(a,b)]

def mydivide2(a, b):
	for i in b:
		if i == 0:
			print "someting wong wit input"
			return []
	return mydivide1(a, b)

def mydivide3(a, b):
	try:
		return mydivide1(a, b)
	except ZeroDivisionError:
		print "attempted to divide by 0"
	except TypeError:
		print "Non-numeric data detected"
	except ValueError:
		print "incorrect value detected"
	return []

a = range(0,1000000); b = range(1,1000000)+ ['a'] 

#mydivide2(a,b)
mydivide3(a,b)
