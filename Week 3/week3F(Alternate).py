#!/usr/bin/python

import csv, re

with open('data.csv', 'rb') as f:
	reader = csv.reader(f)
	fi = open('data2.csv', 'w')
	fi.write("First,M.I.,Last,Number\n")
	#regex2 = r"([a-zA-Z]+)\D+?([a-zA-Z]+)"
	regex = r"([a-zA-Z]*).?\s([a-zA-Z.]*)\s?([a-zA-Z.]*)\.?"
	regexnum = r"(\d-)?\(?([0-9]{3})\D?([0-9]{3})\D?([0-9]{4})"
	for row in reader:
		if len(row[1]) < 10:
			continue
		words = row[0].split()
		if words[0][-1] == ',':
			#last name is first
			fi.write(re.sub(regex, r"\2,\3,\1,", row[0]))
			#print re.sub(regex, r"\2,\3,\1,", row[0])
		else:
			#first name is first
			fi.write(re.sub(regex, r"\1,\2,\3,", row[0]))
			#print re.sub(regex, r"\1,\2,\3,", row[0])
		#regex for numbers
		fi.write(re.sub(regexnum, r"(\2) \3-\4", row[1])+"\n")
		#print re.sub(regexnum, r"(\2) \3-\4", row[1])
	f.close()
	fi.close()

# regex = r"([a-zA-Z]*).?\s([a-zA-Z.]*)\s?([a-zA-Z.]*)\.?"
# print re.sub(regex, r"\1 \2 \3", "yu, henry M.")
# print re.sub(regex, r"\1 \2 \3", "henry M. yu")
# print re.sub(regex, r"\1 \2 \3", "Bill Nyee")
# print re.sub(regex, r"\1 \2 \3", "Nye, Bill")





