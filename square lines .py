import cv2 as cv

# finding lines and identifying square
# blur > edge cascade > some sort of square locator 

img = cv.imread('Photos/cropme.jpg',cv.IMREAD_UNCHANGED) 

scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)

cv.imshow('test2', resized)

blur = cv.GaussianBlur(resized, (3,3), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 100, 200)
cv.imshow('Canny Edges', canny)


cv.waitKey(0)
cv.destroyAllWindows() 