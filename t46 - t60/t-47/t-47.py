import cv2
import numpy as np
count = 1
data = []

for img in range(0, 10):
    imageGray = cv2.imread(f'imagem{count}.jpg', 0)
    imageGrayCanny = cv2.Canny(imageGray, 100, 255)
    imageGrayCannyLaplace = cv2.Laplacian(imageGrayCanny, cv2.CV_8UC1,3)
    ret, thresh = cv2.threshold(imageGrayCannyLaplace,127,255, cv2.THRESH_BINARY)

    moments = cv2.moments(thresh)
    centralMoments = moments['mu20'], moments['mu11'], moments['mu02'], moments['mu30'],\
                     moments['mu21'], moments['mu12'], moments['mu03']

    print(str(centralMoments),'\n')

    data.append(centralMoments)

    cv2.waitKey(500)
    count += 1
np.savetxt('CentralMoments.csv', data, delimiter='--------')




