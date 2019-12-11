import cv2 as cv
import numpy as np


image = cv.imread('img.jpg')
imageGray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
imageGrayCanny = cv.Canny(image,100,150)
cv.imshow('canny',imageGrayCanny)

contours, hierarchy = cv.findContours(imageGrayCanny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

contours_poly = [None] * len(contours)
boundRect = [None] * len(contours)
for local, contour in enumerate(contours):
    contours_poly[local] = cv.approxPolyDP(contour, 3, True)
    boundRect[local] = cv.boundingRect(contours_poly[local])

draw = np.copy(image)
for i in range(len(contours)):

    color = ((0, 0, 255))
    cv.drawContours(draw, contours_poly, i, color)
    cv.rectangle(draw, (int(boundRect[i][0]), int(boundRect[i][1])),
                 (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)

for index ,contour in enumerate(contours):
    print(f"object {index + 1}: {cv.contourArea(contour)} a.u.")

cv.imshow('draw',draw)
cv.waitKey(0)
cv.imwrite("objects.jpg", draw)
