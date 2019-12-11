import cv2 as cv
import numpy as np
import random


img = cv.imread("/home/andre/Área de Trabalho/training/codigos/t-26/forms.png", 0)
rows, cols = img.shape[:2]
imgGrow = np.zeros((rows, cols, 3), np.uint8)
imgSupport = np.zeros((rows, cols, 1), np.uint8)


objects = 0
r = 0
g = 0
b = 0
for row in range(rows):
    for col in range(cols):
        if img[row, col] == 0 and imgSupport[row, col] == 0:
            objects += 1
            imgSupport[row, col] = 255

            imgGrow[row, col, 2] = r
            imgGrow[row, col, 1] = g
            imgGrow[row, col, 0] = b

            if objects == 0:
                r -= random.randint(0, 256)
                g += random.randint(0, 256)
                b -= random.randint(0, 256)
            if objects%2 == 0:
                r += random.randint(0, 256)
                g -= random.randint(0, 256)
                b += random.randint(0, 256)
            if objects%2 != 0:
                r -= random.randint(0, 256)
                g -= random.randint(0, 256)
                b -= random.randint(0, 256)

            current = 1
            previous = 0

            while current != previous:
                current = previous
                print("I'm growing, patience please.......")
                for row1 in range(rows):
                    for col1 in range(cols):
                        if imgSupport[row1, col1] == 255:
                            for j in range(-1, 2):
                                for i in range(-1, 2):
                                    if img[row1 - j, col1 - i] < 127 and imgSupport[row1 - j, col1 - i] != 255:
                                        imgGrow[row1 - j, col1 - i, 2] = r
                                        imgGrow[row1 - j, col1 - i, 1] = g
                                        imgGrow[row1 - j, col1 - i, 0] = b
                                        imgSupport[row1 - j, col1 - i] = 255
                                        img[row1 - j, col1 - i] = 255
                                        previous += 1
                    cv.imshow("image-growing with random colors scale",imgGrow)
                    cv.imshow("objects", img)
                    cv.waitKey(30)
cv.imshow("Growed with random colors", imgGrow)
cv.imshow("Stated objects", imgSupport)
cv.imwrite("colored objects.jpg", imgGrow)
cv.waitKey(0)