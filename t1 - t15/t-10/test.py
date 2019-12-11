# a imagem tem 18x17 pixels

import cv2 as cv
from PIL import Image
import numpy as np


img = cv.imread('tucano.jpg',0)
qtyRows, qtyCols = img.shape
print(img.shape)
img = cv.resize(img, (int(qtyCols/2), int(qtyRows/2))) #colunas, linhas
imgResult = np.zeros((int(qtyRows/2),int(qtyCols/2)), np.uint8) #linhas, colunas

cv.imshow("Teste", img)
# cv.imshow("Teste2", imgResult)
# cv.waitKey(0)

for i in range(int(qtyRows/2)):
    for j in range(int(qtyCols/2)):
        if img[i,j] > 100 and img[i,j] < 180 :
            imgResult[i, j] = 0
        else: imgResult[i, j] = 255
cv.imshow('img-resultado',imgResult)

cv.waitKey()