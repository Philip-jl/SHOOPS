import cv2 as cv
import numpy as np

img = cv.imread('Photos/cropme.jpg',cv.IMREAD_UNCHANGED) 
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
#canny = cv.Canny(blur, 75, 100)
scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized = cv.resize(blur, dim, interpolation = cv.INTER_AREA)

imgGrey = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
_, thrash = cv.threshold(imgGrey,240,255,cv.THRESH_BINARY)
contours, _ = cv.findContours(thrash,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv.approxPolyDP(contour,0.05* cv.arcLength(contour,True), True)
    cv.drawContours(resized, [approx], 0, (0,0,0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 4:
        x,y,w,h = cv.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv.putText(resized,"Square", (x,y), cv.FONT_HERSHEY_COMPLEX, 3, (0,0,0))
        else:
            cv.putText(resized,"rectangle", (x,y), cv.FONT_HERSHEY_COMPLEX, 3, (0,0,0))
    else:
        cv.putText(resized,"oof", (x,y), cv.FONT_HERSHEY_COMPLEX, 3, (0,0,0))

cv.imshow('test', resized)
cv.waitKey(0)
cv.destroyAllWindows()
