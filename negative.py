import cv2 as cv


img = cv.imread('lab2\\Angad.jpeg')

row = img.shape[0]
col = img.shape[1]


grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
negative = grayimg.copy()

cv.imshow('Grayscale', grayimg)
L = img.max()


for i in range(row):
    for j in range(col):
        negative[i][j] = 255 - negative[i][j]

cv.imshow('Negative image', negative)

cv.waitKey(0)
cv.destroyAllWindows()