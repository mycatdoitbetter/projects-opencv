import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('ag.jpg',0)

Gx = cv.Sobel(img, dx=1, dy=0, ddepth=cv.CV_64F, ksize=3)
Gy = cv.Sobel(img, dx=0, dy=1, ddepth=cv.CV_64F, ksize=3)

sobel = (Gx ** 2 + Gy ** 2) ** (1 / 2)


plt.plot(1)
plt.subplot(2,2,1)

plt.imshow(img, cmap='gray')
plt.subplot(2,2,2)

plt.hist(img.ravel(),256,[0,256])
plt.subplot(2,2,3)

plt.imshow(sobel, cmap='gray')
plt.subplot(2,2,4)

plt.hist(sobel.ravel(),256,[0,256])

plt.show()


cv.waitKey(0)