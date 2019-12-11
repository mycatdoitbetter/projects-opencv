import cv2
import numpy
from skimage import feature

count = 1
glcmData = []
angles = [0]
distances = [5]
for index in range(0,10):
    image = cv2.imread(f"imagem{count}.jpg")
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imageGrayCanny = cv2.Canny(imageGray, 100, 255)
    imageGrayCannyLaplace = cv2.Laplacian(imageGrayCanny, cv2.CV_8UC1, 3)
    ret, thresh = cv2.threshold(imageGrayCannyLaplace, 127, 255, cv2.THRESH_BINARY)
    glcm = feature.greycomatrix(imageGray, distances, angles, 256, symmetric=False, normed=True)

    glcmProperties = ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation', 'ASM']
    features = [feature.greycoprops(glcm, glcmProperties)[0, 0] for glcmProperties in glcmProperties]

    glcmData.append(features)

    count += 1
    cv2.waitKey(500)

numpy.savetxt("glcmData.csv", glcmData, delimiter='------')