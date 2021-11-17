import cv2 as cv
import numpy as np
import argparse as arg

img = cv.imread('Photos/test3pix.jpg') 
blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
cv.imshow('color',blur)


#blank = np.zero(img.shape[:2], dtype=)
b,g,r =cv.split(img)

#cv.imshow('blue',b)
#cv.imshow('green',g)
#cv.imshow('red',r)

#ap=arg.ArgumentParser()
#ap.add_argument("-i","--image", help = "path to the image")
#args = vars(ap.parse_args())

#image = cv.imread("Photos/color1.jpg")
#color = int(image[20,20])
#print(color)



print(img.shape)
print(b)
print(g)
print(r)
#rgb=cv.cvtColor(img, cv.COLOR_BGR2RGB)
#cv.imshow('RGB', rgb)


cv.waitKey(0)