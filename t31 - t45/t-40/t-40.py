import cv2 as cv

imageGray = cv.imread("img.png", 0 )
ret, lim = cv.threshold(imageGray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
cv.imshow("thresh", lim)
cv.waitKey(0)
cv.destroyWindow("thresh")

# a questão fala que um objeto 1x3 gera crescimento vertical, mas ele gera crescimento horizontal.
# o getStructuringElemet recebe (col,row)
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 1))

for i in range(20):
    verticalErode = cv.erode(lim, kernel, iterations = i)
    cv.imshow("eroding...", verticalErode)
    cv.waitKey(300)
cv.destroyWindow("erode")
cv.imshow("erode", verticalErode)
cv.imwrite("erode.jpg", verticalErode)
cv.waitKey(0)