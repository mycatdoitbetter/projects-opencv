import cv2 as cv
import numpy as np


imgGray = cv.imread("paint.jpg", 0)
cv.imshow("before detection", imgGray)

#the (6,6) on my parameter serves to assist in the detection

imgBlur = cv.blur(imgGray,(5,5))

circles = cv.HoughCircles(imgBlur,cv.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.round(circles[0, :]).astype("int")
imgBlur = cv.cvtColor(imgBlur,cv.COLOR_GRAY2BGR)
for x, y, r in circles:
    cv.circle(imgBlur, (x, y), r, (0, 0, 255), 4)


cv.imshow("circles", imgBlur)
cv.imwrite("circles_on_the_image.jpg", imgBlur)
cv.waitKey(0)