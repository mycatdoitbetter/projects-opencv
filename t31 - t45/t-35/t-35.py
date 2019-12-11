import cv2 as cv
import numpy as np

imageGray = cv.imread("img.png", 0 )
ret, lim = cv.threshold(imageGray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
cv.imshow("thresh", lim)
cv.waitKey(0)
cv.destroyWindow("thresh")

kernel = np.ones((5, 5), np.uint8)

for i in range(30):
    dilate = cv.dilate(lim, kernel, iterations = i)
    cv.imshow("dilate", dilate)
    cv.waitKey(300)
cv.destroyWindow("dilate")
cv.imshow("dilating...", dilate)
cv.imwrite("dilate.jpg", dilate)
cv.waitKey(0)


