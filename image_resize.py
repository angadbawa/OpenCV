import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('lab1\\Angad.jpeg')

half = cv.resize(img, (0,0), fx = 0.1, fy = 0.1)
bigger = cv.resize(img, (1050, 1610))

cv.imshow('original', img)
cv.imshow('half', half)
cv.imshow('bigger', bigger)

cv.waitKey(0)
cv.destroyAllWindows()