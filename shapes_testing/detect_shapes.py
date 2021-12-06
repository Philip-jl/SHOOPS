# import the necessary packages
from shapedetector import ShapeDetector
import argparse
import imutils
import cv2

imagescan = cv2.imread('shapes_testing\cropme.jpg',cv2.IMREAD_UNCHANGED) 

scale_percent = 20 # percent of original size
width = int(imagescan.shape[1] * scale_percent / 100)
height = int(imagescan.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
scan = cv2.resize(imagescan, dim, interpolation = cv2.INTER_AREA) #RSscan is the ReSized 'scan'

resized = imutils.resize(scan, width=100)
ratio = scan.shape[0] / float(resized.shape[0])
# convert the resized image to grayscale, blur it slightly,
# and threshold it
grey = cv2.cvtColor(scan, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(grey, (5, 5), cv2.BORDER_DEFAULT)
thresh = cv2.threshold(blurred, 200, 100, cv2.THRESH_BINARY)[1]
# find contours in the thresholded image and initialize the
# shape detector
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()
# loop over the contours
for c in cnts:
	# compute the center of the contour, then detect the name of the
	# shape using only the contour
	M = cv2.moments(c)
	if M["m00"] == 0:
		M["m00"]=1
	cX = int((M["m10"] / M["m00"]) * ratio)
	cY = int((M["m01"] / M["m00"]) * ratio)
	shape = sd.detect(c)
	# multiply the contour (x, y)-coordinates by the resize ratio,
	# then draw the contours and the name of the shape on the image
	c = c.astype("float")
	c *= ratio
	c = c.astype("int")
	cv2.drawContours(scan, [c], -1, (0, 255, 0), 2)
	cv2.putText(scan, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (255, 255, 255), 2)
	# show the output image
cv2.imshow("thresh", thresh)
cv2.imshow("Image", scan)
cv2.waitKey(0)