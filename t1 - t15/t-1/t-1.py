import cv2

## 1: colored, 0: gray scale, -1: alpha scale

img = cv2.imread('tucano.jpg',1)
cv2.imshow('imagem_tucano',img)
cv2.imwrite('tucano_p-1.jpg',img)
cv2.waitKey(0)