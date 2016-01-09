#!/usr/bin/python

import time

def createList(s):
	d = {}
	#return a dictionary
	for word in s:
		if word in d:
			d[word] = d[word] + 1
		else:
			d[word] = 1
	return d


gibber = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

words = gibber.split()

#problem 1
dic = {x:words.count(x) for x in words}
print dic

#problem 2
unique = len(dic)
print unique

#problem 3
f = open('plaintext.txt', 'r')
book = f.read();
words = book.split()

start = time.time()
dic = {x:words.count(x) for x in words}
end = time.time()
print "dictionary comprehension elapsed time is",(end - start)

start = time.time()
dic = createList(words)
end = time.time()
print "my function elapsed time is", (end - start)
#print book
print dic['found']







