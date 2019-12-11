import cv2 as cv
import numpy as np

img = cv.imread('tucano.jpg',0)
resized =  cv.resize(img,(200,150))
#cv.imshow('image',resized)

rows, cols = resized.shape

new_img = np.zeros((rows, cols), np.uint8)

for row in range(1,rows-1):
    for col in range(1,cols-1):
        Gx = resized[row - 1, col - 1] * (-1) + resized[row, col - 1] * (-2) + \
             resized[row + 1, col - 1] * (-1) + resized[row - 1, col + 1] + \
             resized[row, col + 1] * 2 + resized[row + 1, col + 1]
        Gy = resized[row - 1, col - 1] * (-1) + resized[row - 1, col] * (-2) + \
             resized[row - 1, col + 1] * (-1) + resized[row + 1, col - 1] + \
             resized[row + 1, col] * 2 + resized[row - 1, col + 1]

        new_img[row][col] = ((Gx**2) + (Gy**2))**(1/2)

print(new_img)
cv.imshow('ds',new_img)
cv.imwrite('filtradopae.jpg',new_img)


cv.waitKey(0)

