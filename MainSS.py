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
    #cv2.circle(RSscan, (cX, cY), 3, (255, 255, 255), -1)        # circle that was drawn with this command messed with the color detect.
    approx = cv2.approxPolyDP(c, 0.009 * cv2.arcLength(c, True), True)
    # Used to flatted the array containing
    # the co-ordinates of the vertices.
    Cimg = RSscan[int(cY):int(cY+10), int(cX):int(cX+10)]     #cropping image 100 pixes from the ceter square

    #img = cv2.imread(Cimg) 
    blur = cv2.GaussianBlur(Cimg, (9,9), cv2.BORDER_DEFAULT)

    b,g,r =cv2.split(Cimg)

    #image = cv.imread()
    #color = int(image[20,20])

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


Ph_RGB =   cl[7][2]
Iron_RGB = cl[6][2]
Lead_RGB = cl[5][2]
Copp_RGB = cl[4][2]
Alum_RGB = cl[3][2]
Merc_RGB = cl[2][2]
Sulf_RGB = cl[1][2]
Brom_RGB = cl[0][2]

Ph_HSV =   cl[7][3]
Iron_HSV = cl[6][3]
Lead_HSV = cl[5][3]
Copp_HSV = cl[4][3]
Alum_HSV = cl[3][3]
Merc_HSV = cl[2][3]
Sulf_HSV = cl[1][3]
Brom_HSV = cl[0][3]


print(*cl, sep = "\n")
#print("red")   print(*r, sep = "\n")   print("green")  print(*g, sep = "\n")   print("blue")   print(*b, sep = "\n")
# Show the output image
cv2.imshow('Output', out)
#cv2.imshow("Image", RSscan)
#cv2.imshow('thresh',thresh)
#cv2.imshow('Blurred',blurred)
cv2.waitKey(0)