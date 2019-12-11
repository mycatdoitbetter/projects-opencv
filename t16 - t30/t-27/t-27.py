import cv2 as cv
import numpy as np
import random


img = cv.imread("/home/andre/Área de Trabalho/training/codigos/t-27/img-paint.jpg", 0)
rows, cols = img.shape[:2]
imgGrow = np.zeros((rows, cols, 3), np.uint8)
imgSupport = np.zeros((rows, cols, 1), np.uint8)


objects = 0
form = 0
xMax = 0
xMin = 0
yMax = 0
yMin = 0
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

            yMin, yMax, xMin, xMax = row, row, col, col

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

                                        if xMin > col1 - i:
                                            xMin = col1 - i
                                        if xMax < col1 - i:
                                            xMax = col1 - i
                                        if yMax < row1 - j:
                                            yMax = row1 - j
                    cv.imshow("objects", img)
                    cv.waitKey(3)
            print("Object growed")
            form +=1
            cv.rectangle(imgSupport, (xMin, yMin), (xMax,yMax), (255, 255, 0), 1)
            rect = imgGrow[yMin-2:yMax+2, xMin-2:xMax+2]
            cv.imwrite(f"Highlighted {form}.jpg",rect)
            cv.imshow(f"Highlighted {form}", rect)

                    

cv.waitKey(0)