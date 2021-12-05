import cv2 as cv
import numpy as np
import argparse as arg

img = cv.imread('Photos/color1.jpg') 
blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
cv.imshow('color',blur)

b,g,r =cv.split(img)

ba=np.round(np.average(b),0)
ga=np.round(np.average(g),0)
ra=np.round(np.average(r),0)

print(img.shape)
print('b =',ba)
print('g =',ga)
print('r =',ra)

cv.waitKey(0)
