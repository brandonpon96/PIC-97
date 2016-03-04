#!/usr/bin/python

import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture('RyanRun.MP4')
template = cv2.imread('hip.png',1)
w, h, d = template.shape[::-1]
comps = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
meth = comps[4]
method = eval(meth)
posx = []
posy = []

for i in range(870):
	ret = cap.grab()
for i in range(212):
	ret, img = cap.read()

	# Apply template Matching
	res = cv2.matchTemplate(img,template,method)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

	top_left = min_loc
	bottom_right = (top_left[0] + w, top_left[1] + h)
	posx.append(top_left[0])
	posy.append(top_left[1])

	cv2.rectangle(img,top_left, bottom_right, (0, 0,255), 2)
	cv2.imshow('wtf', img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
posx = posx[23:len(posx)-25]
posy = posy[23:len(posy)-25]
posy = [-y for y in posy]
plt.plot(posx, posy, 'b-')
plt.title('Hip Trace')
plt.xlabel('X Pixel')
plt.ylabel('Y Pixel')
plt.show()
