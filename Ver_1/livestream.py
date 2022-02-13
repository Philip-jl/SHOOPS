import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)
while True:
    ret, frame = cap.read()


    blur = cv.GaussianBlur(cap, (3,3), cv.BORDER_DEFAULT)
    canny = cv.Canny(blur, 75, 100)
   
   
   
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
