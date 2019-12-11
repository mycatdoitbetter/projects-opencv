import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('img2.jpg',0)
img = cv.resize(img,(600,700))

img_eq = cv.equalizeHist(img)


plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')

plt.subplot(2,2,2)
plt.hist(img.ravel(),256,[0,256])

plt.subplot(2,2,3)
plt.imshow(img_eq, cmap='gray')

plt.subplot(2,2,4)
plt.hist(img_eq.ravel(),256,[0,256])
plt.show()







cv.waitKey(0)