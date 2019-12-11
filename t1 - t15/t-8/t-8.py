import cv2 as cv

img = cv.imread('tucano.jpg',0)
cv.imshow('tucano-color',img)

resized = cv.resize(img,(700,600))

cv.imshow('tucano-resized',resized)

cv.imwrite('tucano-resized.png',resized)
cv.waitKey()