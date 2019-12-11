import cv2 as cv
## 40 É A FLAG DO -----> COLOR_BGR2HSV, PODE SER ESCRITO
## COMO cv.COLOR_COLOR_BGR2HSV (file) .
img = cv.imread('tucano.jpg',40)
h,s,v = cv.split(img)
cv.imshow('h-channel-HSV',h)
cv.imshow('s-channel-HSV',s)
cv.imshow('v-channel-HSV',v)
#save
cv.imwrite('tucano_p-3-h-channel-HSV.png',h)
cv.imwrite('tucano_p-3-s-channel-HSV.png',s)
cv.imwrite('tucano_p-3-v-channel-HSV.png',v)
cv.waitKey()





cv.waitKey()