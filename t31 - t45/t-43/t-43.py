import cv2 as cv
import numpy as np
# para entender melhor os parametros do blob sugiro ler mais nesse site: https://www.learnopencv.com/blob-detection-using-opencv-python-c/

img = cv.imread("img.png")
imgCanny = cv.Canny(img, 170, 255)

# criando o objeto params para atribuir dados de detecção
params = cv.SimpleBlobDetector_Params()


# adicionando threshold
params.maxThreshold = 200
params.minThreshold = 10

# adicionando filtro pela área e pelo tipo de figura
params.filterByArea = True
params.minArea = 20
params.maxArea = 40000
params.filterByCircularity = False
params.minCircularity = 0.1
params.filterByConvexity = False
params.minConvexity = 0.87
params.filterByInertia = False  # isso significa o qual alongado o objeto é
params.minInertiaRatio = 0.01

detector = cv.SimpleBlobDetector_create(params)

detectedObjects = detector.detect(imgCanny)
quantityOfRows, quantityOfCols = imgCanny.shape[:2]

drawing = cv.drawKeypoints(imgCanny, detectedObjects, np.array([]), (0, 0, 255),cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

newImage = img.copy()
for object in range(len(detectedObjects)):

    xCoor, yCoor = np.int(detectedObjects[object].pt[0]), np.int(detectedObjects[object].pt[1])
    size = np.int(detectedObjects[object].size)
    if size > 0:
        size = np.int(size / 2)
        imgBlob = cv.rectangle(newImage, (xCoor - size - 25, yCoor - size - 25), (xCoor + size + 25, yCoor + size + 25), color=(0,255,0), thickness=2)

cv.imshow("Blob image", imgBlob)

cv.waitKey(0)

cv.imwrite("blobObjects.jpg", imgBlob)
