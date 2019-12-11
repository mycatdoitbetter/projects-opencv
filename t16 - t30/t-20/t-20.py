import numpy as np
import cv2 as cv

img = cv.imread('img-paint.jpg',0)


rows, cols = img.shape

xc, yc = (rows/2,cols/2)

segmentado = np.zeros_like(img)


segmentado[int(xc), int(yc)] = 255


ponto_atual = 0
ponto_anterior = 1

while ponto_anterior != ponto_atual:
    ponto_anterior = ponto_atual
    ponto_atual = 0
    for row in range(rows):
        for col in range(cols):
            if segmentado[row, col] == 255:
                if img[row - 1, col - 1] < 127:
                        segmentado[row - 1, col - 1] = 255
                        ponto_atual += 1
                if img[row - 1, col] < 127:
                        segmentado[row - 1, col] = 255
                        ponto_atual += 1
                if img[row - 1, col + 1] < 127:
                        segmentado[row - 1, col + 1] = 255
                        ponto_atual += 1
                if img[row, col - 1] < 127:
                        segmentado[row, col - 1] = 255
                        ponto_atual += 1
                if img[row, col + 1] < 127:
                        segmentado[row, col + 1] = 255
                        ponto_atual += 1
                if img[row + 1, col - 1] < 127:
                        segmentado[row + 1, col - 1] = 255
                        ponto_atual += 1
                if img[row + 1, col] < 127:
                        segmentado[row + 1, col] = 255
                        ponto_atual += 1
                if img[row + 1, col + 1] < 127:
                        segmentado[row + 1, col + 1] = 255
                        ponto_atual += 1


cv.imshow('img-segmentada', segmentado)
cv.imshow('normal',img)
cv.waitKey(0)

cv.imwrite('img-segmentada.jpg', segmentado)


