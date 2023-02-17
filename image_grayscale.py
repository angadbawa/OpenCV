import cv2 as cv

img = cv.imread('lab1\\Angad.jpeg')

grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Grayscale', grayimg)

cv.waitKey(0)
cv.destroyAllWindows()