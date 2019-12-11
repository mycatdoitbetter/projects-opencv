import cv2 as cv
## gravar imagem
img = cv.imread('tucano.jpg',1)
## dividir imagem
b,g,r = cv.split(img)
#mostrar cada imagem
cv.imshow('b-channel',b)
cv.imshow('g-channel',g)
cv.imshow('r-channel',r)
#save
cv.imwrite('tucano_p-3-b-channel.png',b)
cv.imwrite('tucano_p-3-g-channel.png',g)
cv.imwrite('tucano_p-3-r-channel.png',r)
cv.waitKey()

