import imutils
import cv2
import numpy as np
import math
import sys

#Color ballance code originally sources by https://www.morethantechnical.com/2015/01/14/simplest-color-balance-with-opencv-wcode/ and by https://gist.github.com/DavidYKay/9dad6c4ab0d8d7dbf3dc which was then optemized by JackDesBwa

#Color balance 
def simplest_cb(img, percent=1):
    out_channels = []
    cumustops = (
        img.shape[0] * img.shape[1] * percent / 200.0,
        img.shape[0] * img.shape[1] * (1 - percent / 200.0)
    )
    for channel in cv2.split(img):
        cumuhist = np.cumsum(cv2.calcHist([channel], [0], None, [256], (0,256)))
        low_cut, high_cut = np.searchsorted(cumuhist, cumustops)
        lut = np.concatenate((
            np.zeros(low_cut),
            np.around(np.linspace(0, 255, high_cut - low_cut + 1)),
            255 * np.ones(255 - high_cut)
        ))
        out_channels.append(cv2.LUT(channel, lut.astype('uint8')))
    return cv2.merge(out_channels)

img=cv2.imread('SHOOPS_Output.jpg')
imgg = simplest_cb(img, 1)

#Cropping image
c1 = imgg[680:860,350:600] # Slicing to crop the image
#c2 = imgg[280:440,600:840] # Slicing to crop the image

#Greyscale
grey1 = cv2.cvtColor(c1, cv2.COLOR_BGR2GRAY)
#grey2 = cv2.cvtColor(c2, cv2.COLOR_BGR2GRAY)

#Adjusting brightness and contrast formated from https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv 
alpha = 1 # Contrast control (1.0-3.0)
beta = 10 # Brightness control (0-100)

adj1 = cv2.convertScaleAbs(grey1, alpha=alpha, beta=beta)
#adj2 = cv2.convertScaleAbs(grey2, alpha=alpha, beta=beta)

#Bluring
blurred1 = cv2.GaussianBlur(adj1, (0, 0), cv2.BORDER_DEFAULT)
#blurred2 = cv2.GaussianBlur(adj2, (0, 0), cv2.BORDER_DEFAULT)
#blurred = cv2.blur(blurred1, (8, 4), cv2.BORDER_DEFAULT) #extra blur if needed

#Sharpening
sharpen_kernel = np.array([[-1,-1,-1], 
                           [-1, 9,-1], 
                           [-1,-1,-1]])

sharpen1 = cv2.filter2D(blurred1, -1, sharpen_kernel)
#sharpen2 = cv2.filter2D(blurred2, -1, sharpen_kernel)

#Thresholding
thresh1 = cv2.adaptiveThreshold(blurred1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,23,-2)
#thresh2 = cv2.adaptiveThreshold(blurred2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,23,-2)
#trash, thresh = cv2.threshold(adj, 127,255,cv2.THRESH_BINARY) # different thresholding method 

#Morphological transformations
Mkernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
close1 = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, Mkernel, iterations=2)
#close2 = cv2.morphologyEx(thresh2, cv2.MORPH_CLOSE, Mkernel, iterations=2)


#Find contours in the thresholded image
cnts = cv2.findContours(close1, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)


#contour list
cl1= []
cl2= []
cl3= []
cl4= []

#Min and Max area for contours
min_area = 620
max_area = 2450

#Loop over the contours
for c in cnts:
    M = cv2.moments(c)
    if M["m00"] == 0:
	    M["m00"]=1  
    cX = int (M["m10"]/M["m00"])                             # compute the center of the contour
    cY = int (M["m01"]/M["m00"])
    area = cv2.contourArea(c)
    if area > min_area and area < max_area:
        cv2.drawContours(c1, [c], -1, (0, 255, 0), 2)    	    # draw the contour and center of the shape on the image
        #cv2.circle(c1, (cX, cY), 3, (255, 255, 255), -1)        # circle that was drawn with this command messed with the color detect.
        approx = cv2.approxPolyDP(c, 0.009 * cv2.arcLength(c, True), True)

        #Used to flatted the array containing Co-ordinates of the vertices.
        Cimg = c1[int(cY):int(cY+10), int(cX):int(cX+10)]     #cropping image 100 pixes from the ceter square

        #Blur the contour to help average out the color
        blur = cv2.GaussianBlur(Cimg, (9,9), cv2.BORDER_DEFAULT)
        b,g,r =cv2.split(Cimg)

        ba=np.round(np.average(b),0)    
        ga=np.round(np.average(g),0)
        ra=np.round(np.average(r),0)

        #rgb=cv.cvtColor(img, cv.COLOR_BGR2RGB)
        #cv.imshow('RGB', rgb)
        #color = (r,g,b)

        Co = cv2.mean(Cimg)
        #aR = np.mean(Co[:,:,2])
        #aG = np.mean(Co[:,:,1])
        #aB = np.mean(Co[:,:,0])
        # Swap blue and red values (making it RGB, not BGR)
        hsv_bgr = cv2.cvtColor(Cimg, cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(hsv_bgr)
        aH = np.round(np.mean(h)*2,0)
        aS = np.round((np.mean(s)/255)*100,0)
        aV = np.round((np.mean(v)/255)*100,0)
        HSV = [aH,aS,aV] 
        RGB = [ra,ga,ba]                       #np.array([(aH[2],aS[1],aV[0])])     #np.array([(hsv_bgr[2], hsv_bgr[1], hsv_bgr[0])]) 
        #RGB_1 = [aR, aG, aB]                                        #RGB = np.array([(Co[2], Co[1], Co[0])])
        cil=[cX, cY, RGB, HSV] 
        Cmid = 100                                               # contour inner list
        if cY > Cmid:
            for y in range(0):
                cil.append(y)
            cl2.append(cil)
        elif cY < Cmid:
            for y in range(0):
                cil.append(y)
            cl1.append(cil)
        else:
            print('error')    
n = approx.ravel() 
i = 0



mask1 = thresh1 # Create mask where white is what we want, black otherwise
out1 = np.zeros_like(c1) # Extract out the object and place into output image
out1[mask1 == 255] = (c1[mask1 == 255])

# Now crop
(y, x) = np.where(mask1 == 255)
(topy, topx) = (np.min(y), np.min(x))
(bottomy, bottomx) = (np.max(y), np.max(x))
out1 = out1[topy:bottomy+1, topx:bottomx+1]

def sort_key(ColorList): #sorting the lists x values from least to greatest
	return ColorList[0]

cl1.sort(key=sort_key)
cl2.sort(key=sort_key)


clc= cl1 + cl2 #combined lists

#cl1

c1_Iron_RGB = clc[0][2]
c1_Lead_RGB = clc[1][2]
c1_Copp_RGB = clc[2][2]
c1_Ph_RGB   = clc[3][2]
c1_Merc_RGB = clc[4][2]
c1_Brom_RGB = clc[5][2]

c1_Iron_HSV = clc[0][3]
c1_Lead_HSV = clc[1][3]
c1_Copp_HSV = clc[2][3]
c1_Ph_HSV   = clc[3][3]
c1_Merc_HSV = clc[4][3]
c1_Brom_HSV = clc[5][3]


#print(*cl1, sep = "\n")
#print(*cl2, sep = "\n")
#print(*clc, sep = "\n")
#print("red")   print(*r, sep = "\n")   print("green")  print(*g, sep = "\n")   print("blue")   print(*b, sep = "\n")
# Show the output image
cv2.imshow("Imgg", img)
cv2.imshow("Image1", c1)
cv2.imshow('thresh1',thresh1)
#cv2.imshow('Blurred',blurred)
cv2.waitKey(0)

