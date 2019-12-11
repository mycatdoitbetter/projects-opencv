# a imagem tem 18x17 pixels

import cv2 as cv
from PIL import Image
# numpy

img = cv.imread('teste.jpg',0)

# imOrig = cv.imread("teste.jpg", 0)

px_img = Image.open('teste.jpg','r')

px_val = list(px_img.getdata())

matrix = open('matrix.txt','w+')

k = 0
for i in range(len(px_val)):
    k += 1
    px_val[i] = str(px_val[i][1]) + ' '
    if len(px_val[i]) < 3 : px_val[i] =  px_val[i]
    #escrita no doc

    if int(px_val[i]) < 200 : px_val[i] = '1'
    else: (px_val[i]) = '0'

    matrix.write(px_val[i])
    #quebra de linha em formatação
    if k == 18:
        k = 0
        matrix.write('\n')
print(px_val)
cv.waitKey()