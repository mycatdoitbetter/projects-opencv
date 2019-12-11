import cv2 as cv
## filtros passa baixa permitem a passagem de altas frequencias.
## also know as deixa passar as bordas
img = cv.imread('tucano.jpg',0)
cv.imshow('imagem-tucano', img)
passa_alta = cv.Canny(img,100,180)
cv.imshow('passa_alta',passa_alta)
cv.imwrite('tucano-passa-alta.jpg',passa_alta)
cv.waitKey()