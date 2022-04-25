import cv2 as cv
import numpy as np
import argparse as arg

img = cv.imread('Photos/leadtestbad.png') 
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

ba=np.round(np.average(b),0)
ga=np.round(np.average(g),0)
ra=np.round(np.average(r),0)

print(img.shape)
print('r =',r)
print('g =',g)
print('b =',b)
#rgb=cv.cvtColor(img, cv.COLOR_BGR2RGB)
#cv.imshow('RGB', rgb)
color = (r,g,b)

    ### values after dipping in water
ppb0 = (238, 207, 154)
ppb5 = (233, 193, 146)
ppb15 = (231, 136, 186)
ppb30 = (214, 129, 124)
ppb50 = (211, 115, 111)

if ppb0 >= color and color >= ppb5:
    {print("Between 0ppb and 5ppb :Ok")}
elif color <= ppb5 and color >= ppb15:
    {print("Between 5ppb and 15ppb :Ok")}
elif (color <= ppb15 and color >= ppb30):
    {print("Between 15ppb and 30ppb :Ok")}
elif (color <= ppb30 and color >= ppb50):
    {print("Between 30ppb and 50ppb :  Not Ok")}

else:
    print("Nothing")
cv.waitKey(0)
