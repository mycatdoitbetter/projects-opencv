import cv2 as cv

img = cv.imread('tucano.jpg',0)
cv.imshow('imagem-tucano', img)
passa_alta = cv.Canny(img,100,100)
cv.imshow('passa_alta',passa_alta)
cv.imwrite('tucano-passa-alta-com-treshold.jpg',passa_alta)
cv.waitKey()