import cv2 as cv

img = cv.imread('lab2\\Angad.jpeg')

flipp = cv.flip(img, 0)


resized_image = cv.resize(flipp, (450, 600))
cv.imshow('Flipped image', resized_image)
cv.waitKey(0)
