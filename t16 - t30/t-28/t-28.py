import cv2 as cv

img = cv.imread("/home/andre/Área de Trabalho/training/codigos/t-29/sapo.jpg", 0)
img_threshed = cv.adaptiveThreshold(img, 127, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11, 2)
cv.imshow("image", img)
cv.imshow("threshed", img_threshed)
cv.waitKey(0)
cv.imwrite("threshed.jpg", img_threshed)