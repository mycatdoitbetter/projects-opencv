import cv2 as cv
import numpy as np

image = cv.imread('img.jpg')
imageGray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
imageGrayCanny = cv.Canny(image,100,150)

contours, hierarchy = cv.findContours(imageGrayCanny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

contoursPoly = [None] * len(contours)
boundRect = [None] * len(contours)
for local, contour in enumerate(contours):
    contoursPoly[local] = cv.approxPolyDP(contour, 3, True)
    boundRect[local] = cv.boundingRect(contoursPoly[local])


draw = np.copy(image)
for contour in range(len(contours)):
        color = (0, 0, 255) # red
        cv.drawContours(draw, contoursPoly, contour, color)
        cv.rectangle(draw, (int(boundRect[contour][0]), int(boundRect[contour][1])),
                      (int(boundRect[contour][0]+boundRect[contour][2]), int(boundRect[contour][1]+boundRect[contour][3])), color, 2)
        cutted = draw[int(boundRect[contour][1]):int(boundRect[contour][1]) + boundRect[contour][3],
                 (boundRect[contour][0]):int(boundRect[contour][0]) + int(boundRect[contour][2])]
        cv.imshow(f"{contour + 1} object cutted", cutted)
        cv.imwrite(f"object-number-{contour}.jpg", cutted)
        cv.waitKey(1000)
for index ,contour in enumerate(contours):
    print(f"object {index + 1}: {cv.contourArea(contour)} a.u.")

cv.imshow('draw',draw)
cv.waitKey(0)
cv.imwrite("objects.jpg", draw)
