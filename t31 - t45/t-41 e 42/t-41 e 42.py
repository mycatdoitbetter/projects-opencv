import cv2 as cv


imgGray = cv.imread("img.png", 0)
imgGrayCanny = cv.Canny(imgGray, 170, 255)

# criando o objeto params para atribuir dados de detecção

params = cv.SimpleBlobDetector_Params()

# para entender melhor os parametros abaixo sugiro ler mais nesse site: https://www.learnopencv.com/blob-detection-using-opencv-python-c/
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

blob = detector.detect(imgGrayCanny)

print(f"number of objects: {len(blob)}")

cv.waitKey(0)

