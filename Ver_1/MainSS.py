# import the necessary packages
import imutils
import cv2
import numpy as np

# load the image, convert it to grayscale, blur it slightly,
# and threshold it

scan = cv2.imread('Photos/newstrip.jpg',cv2.IMREAD_UNCHANGED) 

scale_percent = 60 # percent of original size
width = int(scan.shape[1] * scale_percent / 100)
height = int(scan.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
RSscan = cv2.resize(scan, dim, interpolation = cv2.INTER_AREA) #RSscan is the ReSized 'scan'

grey = cv2.cvtColor(RSscan, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(grey, (5, 5), cv2.BORDER_DEFAULT)
thresh = cv2.threshold(blurred, 130, 255, cv2.THRESH_BINARY)[1]

# find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
# loop over the contours

cl1= []
cl2= []
#contour list

for c in cnts:
    M = cv2.moments(c)
    if M["m00"] == 0:
	    M["m00"]=1  
    cX = int (M["m10"]/M["m00"])                              # compute the center of the contour
    cY = int (M["m01"]/M["m00"])

    cv2.drawContours(RSscan, [c], -1, (0, 255, 0), 2)    	    # draw the contour and center of the shape on the image
    cv2.circle(RSscan, (cX, cY), 3, (255, 255, 255), -1)
    approx = cv2.approxPolyDP(c, 0.009 * cv2.arcLength(c, True), True)
    # Used to flatted the array containing
    # the co-ordinates of the vertices.
    Cimg = RSscan[int(cY):int(cY+100), int(cX):int(cX+100)]     #cropping image 100 pixes from the ceter square
    Co = cv2.mean(Cimg)
    # Swap blue and red values (making it RGB, not BGR)
    hsv_bgr = cv2.cvtColor(RSscan, cv2.COLOR_BGR2HSV)
    aH = np.mean(hsv_bgr[:,:,2])
    aS = np.mean(hsv_bgr[:,:,1])
    aV = np.mean(hsv_bgr[:,:,0])
    HSV = [aH,aS,aV]                        #np.array([(aH[2],aS[1],aV[0])])     #np.array([(hsv_bgr[2], hsv_bgr[1], hsv_bgr[0])]) 
    RGB = np.array([(Co[2], Co[1], Co[0])])
    cil=[cX, cY, RGB, HSV]                                                # contour inner list
    if cY > 250:
        for y in range(0):
            cil.append(y)
        cl2.append(cil)
    elif cY < 220:
        for y in range(0):
            cil.append(y)
        cl1.append(cil)
    else:
        print('error')    
n = approx.ravel() 
i = 0

for j in n :
        if(i % 2 == 0):
            x = n[i]
            y = n[i + 1]
  
            # String containing the co-ordinates.
            string = str(x) + " " + str(y) 
  
            if(i == 0):
                # text on topmost co-ordinate.
                cv2.putText(RSscan, "topmost co-ordinate", (x, y), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 0, 0)) 
            else:
                # text on remaining co-ordinates.
                cv2.putText(RSscan, string, (x, y), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 255, 0)) 
        i = i + 1

mask = thresh # Create mask where white is what we want, black otherwise
out = np.zeros_like(RSscan) # Extract out the object and place into output image
out[mask == 255] = (RSscan[mask == 255])

# Now crop
(y, x) = np.where(mask == 255)
(topy, topx) = (np.min(y), np.min(x))
(bottomy, bottomx) = (np.max(y), np.max(x))
out = out[topy:bottomy+1, topx:bottomx+1]

def sort_key(ColorList): #sorting the lists x values from least to greatest
	return ColorList[0]

cl1.sort(key=sort_key)
cl2.sort(key=sort_key)
cl= cl2 + cl1 #combined lists

print(*cl, sep = "\n")


# Show the output image
cv2.imshow('Output', out)
# cv2.imshow("Image", RSscan)
#cv2.imshow('thresh',thresh)
#cv2.imshow('Blurred',blurred)
cv2.waitKey(0)
