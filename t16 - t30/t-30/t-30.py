import cv2 as cv
img = cv.imread('img.png', 0)
#cinza = cv.cvtColor(imagem,cv.COLOR_BGR2GRAY)
imgCanny = cv.Canny(img,100,150)
cv.imshow('canny',imgCanny)
contornos= cv.findContours(imgCanny,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
print('contornos',len(contornos))
cv.waitKey(0)