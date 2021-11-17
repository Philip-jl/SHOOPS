import cv2 as cv

# finding lines and identifying square
# blur > edge cascade > some sort of square locator 

img = cv.imread('Photos/test2.jpg') 
cv.imshow('test2',img)

blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 75, 100)
cv.imshow('Canny Edges', canny)

cv.waitKey(0)