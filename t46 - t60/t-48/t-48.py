import cv2
import numpy as np
momentsData = []
count = 1
for index in range(0, 10):
    imageGray = cv2.imread(f"imagem{count}.jpg", 0)
    imageGrayCanny = cv2.Canny(imageGray, 100, 255)
    imageGrayCannyLaplace = cv2.Laplacian(imageGrayCanny, cv2.CV_8UC1, 3)
    ret, threshImage = cv2.threshold(imageGrayCannyLaplace, 127, 255, cv2.THRESH_BINARY)

    moments = cv2.moments(threshImage)
    HuMoments = cv2.HuMoments(moments)
    HuMoments = [moment[0] for moment in HuMoments]

    print(f"HuMoments of {count} image")
    print(str(HuMoments), '\n')

    momentsData.append(HuMoments)

    cv2.waitKey(500)

    count += 1


np.savetxt("HuMoments.cv", momentsData, delimiter="--------------")

