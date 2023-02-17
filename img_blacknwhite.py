import cv2 as cv

img = cv.imread('lab1\\Angad.jpeg')

grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(thresh, blacknwhite) = cv.threshold(grayimg, 127, 255, cv.THRESH_BINARY)

cv.imshow('Grayscale', grayimg)
cv.imshow('Black n White', blacknwhite)
cv.waitKey(0)
cv.destroyAllWindows()