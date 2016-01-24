#!/usr/bin/python

import csv, re

with open('data.csv', 'rb') as f:
	reader = csv.reader(f)
	fi = open('data2.csv', 'w')
	fi.write("First,M.I.,Last,Number\n")
	for row in reader:
		if len(row[1]) < 10:
			continue
		words = row[0].split()
		if len(words) == 2:
			regex = r"([a-zA-Z]+)\D+?([a-zA-Z]+)"
			if words[0][-1] == ',':
				#last name is first
				fi.write(re.sub(regex, r"\2,\1,", row[0]))
			else:
				#first name is first
				fi.write(re.sub(regex, r"\1,\2,", row[0]))
		else:
			regex = r"([a-zA-Z]+)\D+?([a-zA-Z]+)\D?\D?([a-zA-Z]+)\D?"
			if words[0][-1] == ',':
				#last first middle
				fi.write(re.sub(regex, r"\2,\3.,\1,", row[0]))
			else:
				#first middle last
				fi.write(re.sub(regex, r"\1,\2.,\3,", row[0]))
		#regex for numbers
		regex = r"(\d-)?\(?([0-9]{3})\D?([0-9]{3})\D?([0-9]{4})"
		fi.write(re.sub(regex, r"(\2) \3-\4", row[1])+"\n")
	f.close()
	fi.close()




