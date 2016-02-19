#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

cutimg = mpimg.imread('b.jpg')
addimg = mpimg.imread('a.jpg')
arow = len(addimg) #rows
crow = len(cutimg)
startrow = arow/2 - crow/2
endrow = arow/2 + crow/2
adim = len(addimg[0]) #columns
cdim = len(cutimg[0])
startpos = adim/2 - cdim/2
endpos = adim/2 + cdim/2
addimg[startrow:endrow, startpos:endpos] = cutimg
imgplot = plt.imshow(addimg)
plt.savefig('c.jpg')

ver1 = mpimg.imread('g.jpg')
ver1 = ver1.astype(int)
ver2 = mpimg.imread('h.jpg')
ver2 = ver2.astype(int)
dif = (np.absolute(ver1 - ver2) > 10)
dif = dif * ver2
dif = dif.astype(np.uint8)
imgplot = plt.imshow(dif)
plt.savefig('i.jpg')

minion = mpimg.imread('e.jpg')
backdrop = mpimg.imread('d.jpg')
minion = minion.astype(int)
r1, g1, b1 = 1, 255, 19 # Original value
r2, g2, b2 = 0, 0, 0 

red, green, blue = minion[:,:,0], minion[:,:,1], minion[:,:,2]

mask = (np.absolute(red - r1) < 25) & (np.absolute(green - g1) < 25) & (np.absolute(blue - b1) < 25)
mask2 = ~mask
minion[:,:,:3][mask] = [r2, g2, b2]
minion = minion.astype(np.uint8)
mrow = len(minion)
mcol = len(minion[0])
backdrop[550:550+mrow, 300:300+mcol][mask2] = minion[mask2]

imgplot = plt.imshow(backdrop)
plt.savefig('f.jpg')

