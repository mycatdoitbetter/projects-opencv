import cv2
import numpy as np
count=1
data  =[]
for img in range(0,10):
    image = cv2.imread(f'imagem{count}.jpg')
    imageGray = cv2.cvtColor(image ,cv2.COLOR_BGR2GRAY)
    imageGrayCanny = cv2.Canny(imageGray,100,255)
    imageGrayCannyLaplace = cv2.Laplacian(imageGrayCanny,cv2.CV_8UC1,3)
    ret, thresh = cv2.threshold(imageGrayCannyLaplace,127,255,cv2.THRESH_BINARY)

    spatialMoments = cv2.moments(thresh)
    moments = spatialMoments['m00'], spatialMoments['m10'], spatialMoments['m01'], spatialMoments['m20'], spatialMoments['m11'],spatialMoments['m02'], spatialMoments['m30'],\
              spatialMoments['m21'], spatialMoments['m12'], spatialMoments['m03']

    print(str(moments),'\n')

    data.append(moments)

    cv2.waitKey(500)
    count += 1
np.savetxt('Spatial Moments.csv',data,delimiter='--------')