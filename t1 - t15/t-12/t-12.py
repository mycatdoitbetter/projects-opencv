import cv2 as cv
import numpy as np
arq = open('arquivo.txt','r')
for i, line in enumerate(arq):
    row = [int(num) for num in line.split()]
    if i == 0:
        img = np.hstack(row)
    else: img = np.vstack(([img,row]))
arq.close()
new_img = np.asarray(img,np.uint8)
cv.imshow('new_img,',new_img)
cv.imwrite('new.jpg',new_img)
print(row,new_img)
cv.waitKey()