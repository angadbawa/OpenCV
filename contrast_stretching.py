import cv2 as cv
import numpy as np

img = cv.imread("lab2\\Angad.jpeg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

xp = [0,64,128,192,255]
fp = [0,15,128,240,255]

x = np.arange(256)
table = np.interp(x,xp,fp).astype('uint8')
img = cv.LUT(gray, table)

cv.imshow('original', gray)
cv.imshow('contrast', img)
cv.waitKey(0)
cv.destroyAllWindows()