import numpy as np
import cv2


image = cv2.imread('Photos/cropme.jpg',cv2.IMREAD_COLOR)

scale_percent = 20 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
img = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('Shape image')
value = 240
contours = []
def returnTrackBarValue(x):
    value = x

print('Value '+str(value))
_, thresh = cv2.threshold(imgGray,value,255,cv2.THRESH_BINARY)
dilated = cv2.dilate(thresh, None, iterations=3)
contours, _ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print('contours found' + str(len(contours)))

for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(img,[approx],0,(255,255,255),5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    
    print("Approx value"+ str(len(approx)))
    
    if len(approx) == 3:
        cv2.putText(img, "Triangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

    elif len(approx) == 4:
        x,y,w,h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print("AspectRatio "+ str(aspectRatio))
        
        if aspectRatio >= 0.95 and aspectRatio <=1.05:
            cv2.putText(img, "Squar",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
        else:
            cv2.putText(img, "Rectangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

    elif len(approx) == 5:
        cv2.putText(img, "Pentagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

    elif len(approx) == 10:
        cv2.putText(img, "Star",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
    else:
        cv2.putText(img, "Circle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
 
        cv2.imshow('Shape image',img) 
cv2.createTrackbar('Val','Shape image',0,255,returnTrackBarValue)

cv2.imshow('Shape image',img)
cv2.waitKey()
cv2.destroyAllWindows()