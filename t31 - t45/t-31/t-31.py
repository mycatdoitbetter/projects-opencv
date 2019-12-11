import cv2 as cv
import numpy as np
import random as rng
imagem = cv.imread('img.jpg')
cinza = cv.cvtColor(imagem,cv.COLOR_BGR2GRAY)
canny = cv.Canny(imagem,100,150)
cv.imshow('canny',canny)



contours, _ = cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
contours_poly = [None] * len(contours)
boundRect = [None] * len(contours)
for i, c in enumerate(contours):
    contours_poly[i] = cv.approxPolyDP(c, 3, True)
    boundRect[i] = cv.boundingRect(contours_poly[i])


desenho = np.copy(imagem)
for i in range(len(contours)):
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        cv.drawContours(desenho, contours_poly, i, color)
        cv.rectangle(desenho, (int(boundRect[i][0]), int(boundRect[i][1])),
          (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)

cv.imshow('desenhado',desenho)
cv.imwrite("desenhado.jpg",desenho)
cv.waitKey(0)

cv.