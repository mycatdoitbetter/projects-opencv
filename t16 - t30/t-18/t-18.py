import cv2 as cv

img = cv.imread('ag.jpg',0)
cv.imshow('imagem', img)

cv.waitKey(0)

laplac = cv.Laplacian(img,cv.CV_64F)
cv.imshow('imagem-laplac',laplac,)
cv.imwrite('laplac.jpg',laplac)
cv.waitKey(0)


laplac = cv.convertScaleAbs(laplac)

laplac_equalizada = cv.equalizeHist(laplac)
cv.imshow('laplace-equalizada', laplac_equalizada)
cv.imwrite('laplace_equalizada.jpg',laplac_equalizada)
cv.waitKey(0)