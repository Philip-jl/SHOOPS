import cv2
import time
import numpy as np
import argparse as arg

# Capturing video through webcam
webcam = cv2.VideoCapture(1)

TIMER = int(3)
# Start a while loop
while (1):
    # Reading the video from the
    # webcam in image frames
    # _, imageFrame = webcam.read()
    ret, frame = webcam.read()
    cv2.imshow('img1', frame)
    k = cv2.waitKey(125)
    if k == ord('p'):
        prev = time.time()

        while TIMER >= 0:
            ret, frame = webcam.read()
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, str(TIMER),
                        (200, 250), font,
                        7, (0, 255, 255),
                        4, cv2.LINE_AA)
            cv2.imshow('img1', frame)
            cv2.waitKey(125)

            cur = time.time()

            if cur - prev >= 1:
                prev = cur
                TIMER = TIMER - 1
            else:
                ret, frame = webcam.read()
                cv2.imshow('CONTAMINANT IDENTIFIER', frame)
                cv2.waitKey(2000)

                cv2.imwrite('strip.jpg', frame)
    elif k == 27:
        break
    img = cv2.imread('Photos/color1.jpg')
    blur = cv2.GaussianBlur(img, (9, 9), cv2.BORDER_DEFAULT)
    #cv2.imshow('color', blur)

    b, g, r = cv2.split(img)

    ba = np.round(np.average(b), 0)
    ga = np.round(np.average(g), 0)
    ra = np.round(np.average(r), 0)

   # print(img.shape)
    print('b =', ba)
    print('g =', ga)
    print('r =', ra)

    color = (ra, ba, ga)

    ### values after dipping in water
    ppb0 = (222, 130, 108)
    ppb5 = (234, 193, 144)
    ppb15 = (230, 168, 136)
    ppb30 = (214, 131, 124)
    ppb50 = (211, 115, 137)

    if ppb0 < color < ppb5:
        {print("Between 0ppb and 5ppb :Ok")
         }
    elif color > ppb5 and color < ppb15:
        {print("Between 5ppb and 15ppb :Ok")}
    elif (color > ppb15 and color < ppb30):
        {print("Between 15ppb and 30ppb :Ok")}
    elif (color > ppb30 and color < ppb50):
        {print("Between 30ppb and 50ppb :  Not Ok")}

    else:
        print("Nothing")
        
webcam.release()

cv2.waitKey(0)
cv2.destroyAllWindows()
