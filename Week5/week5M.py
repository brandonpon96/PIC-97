#!/usr/bin/python

import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
from IPython.display import Image
import json

data = py.get_figure('dfreder1', '69').get_data()
datadict = data[0]
dates = datadict['x']

def f(x):
	return x >=1900 and x <= 2010

def createDict(s):
	d = {}
	#return a dictionary
	for word in s:
		if word in d:
			d[word] = d[word] + 1
		else:
			d[word] = 1
	return d

parse_dates = sorted(filter(f, dates))
#dictionary keys should be sorted
freq_dict = createDict(parse_dates)

#create a cumulative list
sumvals = 0
for key, value in freq_dict.iteritems():
	sumvals = sumvals + value
	freq_dict[key] = sumvals

#keys are the year (x-axis) and values are the total bridges (y-axis)
x_axis = freq_dict.keys()
y_axis = freq_dict.values()

graph = go.Figure(
		data = go.Data([go.Scatter(x = x_axis, y = y_axis, line= go.Line(color='orange'),fill='tozeroy')]),
		layout = go.Layout(
			height = 400,
			width = 600,
			font = go.Font(family = "Times New Roman", size = '25'),
			title = 'Total Bridges Built in CA Since 1900',
			xaxis1 = go.XAxis(title ='Year',nticks=12),
			yaxis1 = go.YAxis(title = 'Total Bridges')
			)
	)

py.image.save_as(graph, 'bridges.png', width = 1800, height = 1200)




















