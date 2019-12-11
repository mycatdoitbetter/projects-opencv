import cv2 as cv
import numpy as np
## teste.jpg -- 18x17 pixels

img = cv.imread('teste.jpg',0)

QtyRows, QtyCols = img.shape
#matrix = np.zeros(img.shape,np.uint8)

#for i in range(QtyRows):
#    for j in range(QtyCols):
#        matrix[i,j] = img[i,j]

img[8][8] = 255


print(img)
cv.imshow('centroide',img)
cv.imwrite('centroide.jpg',img)
cv.waitKey(0)