import cv2 as cv

img = cv.imread('tucano.jpg',1)
img_cinza = cv.imread('tucano.jpg',0)

mediana = cv.medianBlur(img_cinza,5)
media = cv.blur(img_cinza,(5,5))

cv.imshow('tucano-cinza.jpg-color',img)
cv.imshow('tucano-cinza-median',mediana)
cv.imshow('tucano-cinza.jpg-media',media)


cv.imwrite('tucano-cinza-median.png',mediana)
cv.imwrite('tucano-cinza.jpg-media.png',media)

cv.waitKey()