import cv2 as cv
import numpy as np




imageGray = cv.imread("img.png", 0 )
ret, lim = cv.threshold(imageGray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
cv.imshow("thresh", lim)
cv.waitKey(0)
cv.destroyWindow("thresh")

kernel = np.ones((5, 5), np.uint8)

for i in range(10):
    erode = cv.erode(lim, kernel, iterations = i)
    cv.imshow("erode", erode)
    cv.waitKey(300)
cv.destroyWindow("erode")
cv.imshow("erosing...", erode)
cv.imwrite("erode.jpg", erode)
cv.waitKey(0)
