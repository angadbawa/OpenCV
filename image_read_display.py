import cv2 as cv

img = cv.imread('lab1\\Angad.jpeg')

cv.imshow('Angad img', img)

cv.waitKey(0)
cv.destroyAllWindows()