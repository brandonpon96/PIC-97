#!/usr/bin/python

class MathVector:
	def __init__(self, *args):
		self.l = []
		if len(args) == 1:
			if type(args[0]) is int:
				self.l = [0] * args[0]
			elif type(args[0]) is list:
				self.l = args[0]
			elif type(args[0]) is tuple:
				self.l = list(args[0])
		else:
			[self.l.append(x) for x in args]

	def get_el(self, i):
		return self.l[i-1]
	def neg(self):
		return MathVector([-i for i in self.l])
	def mag(self):
		return sum(x**2 for x in self.l) ** 0.5
	def dot(self, other):
		return sum(x * y for x,y in zip(self.l, other.l))
	def plus(self, other):
		return MathVector([x + y for x,y in zip(self.l, other.l)])
	def sp(self,scalar):
		return MathVector([x * scalar for x in self.l])
	def print_me(self):
		print self.l
	def __getitem__(self, index):
		return self.get_el(index)
	def __neg__(self):
		return self.neg()
	def __abs__(self):
		return self.mag()
	def __mul__(self, other):
		if type(other) is int:
			return self.sp(other)
		return self.dot(other)
	__rmul__ = __mul__
	def __add__(self, other):
		return self.plus(other)
	def __str__(self):
		return str(self.l)

u = MathVector(5)
print "u =",
u.print_me()

v = MathVector([2,3, 6])
print "v =",
v.print_me()

w = MathVector(1,2,3)
print "w =",
w.print_me()

print v.get_el(2)
v.neg().print_me()
print v.mag()
print v.dot(w)
v.plus(w).print_me()
v.sp(3).print_me()

print v
print v[2]
print -v
print abs(v)
print v*w
print v+w
print v*3
print 3*v
