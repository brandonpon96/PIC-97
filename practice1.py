#!/usr/bin/python

N = 7
i = 2
isPrime = True

while i < N and isPrime == True:
	if N % i == 0:
		isPrime = False
	i = i + 1

message = ""
if isPrime:
	message = "prime"
else:
	message = "not prime"

print message