# import the necessary packages
import imutils
import cv2
from shapedetector import ShapeDetector

# load the image, convert it to grayscale, blur it slightly,
# and threshold it

scan = cv2.imread('Photos/newstrip.jpg',cv2.IMREAD_UNCHANGED) 

scale_percent = 40 # percent of original size
width = int(scan.shape[1] * scale_percent / 100)
height = int(scan.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
RSscan = cv2.resize(scan, dim, interpolation = cv2.INTER_AREA) #RSscan is the ReSized 'scan'

grey = cv2.cvtColor(RSscan, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(grey, (5, 5), cv2.BORDER_DEFAULT)
thresh = cv2.threshold(blurred, 100, 200, cv2.THRESH_BINARY)[1]

# find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()
# loop over the contours
for c in cnts:
	M = cv2.moments(c)
	if M["m00"] == 0:
		M["m00"]=1
	# compute the center of the contour
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
	shape = sd.detect(c)
	# draw the contour and center of the shape on the image
	cv2.drawContours(RSscan, [c], -1, (0, 255, 0), 2)
	cv2.circle(RSscan, (cX, cY), 3, (255, 255, 255), -1)
	cv2.putText(scan, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
	0.5, (255, 255, 255), 2)
	# show the image
cv2.imshow("Image", RSscan)
cv2.imshow('thresh',thresh)
cv2.imshow('Blurred',blurred)
cv2.waitKey(0)