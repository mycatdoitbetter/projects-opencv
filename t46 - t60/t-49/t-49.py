from skimage import feature
import numpy as np
import cv2
LocalBinaryPatternsData = []
count = 1
for i in range(0, 10):
    imageGray = cv2.imread(f"imagem{count}.jpg", 0)
    imageGrayCanny = cv2.Canny(imageGray, 100, 255)
    imageGrayCannyLaplace = cv2.Laplacian(imageGrayCanny, cv2.CV_8UC1, 3)
    ret, threshImage = cv2.threshold(imageGrayCannyLaplace, 127, 255, cv2.THRESH_BINARY)

    LocalBinaryPatterns = feature.local_binary_pattern(imageGray, 24, 8, method='uniform')

    hist, ret = np.histogram(LocalBinaryPatterns.ravel(), bins=np.arange(0, 30), range=(0, 30))

    hist = hist.astype('float')
    hist /= (hist.sum() + 1e-7)

    imageLocalBinaryPatterns = [item for item in list(hist)]

    print(imageLocalBinaryPatterns)
    LocalBinaryPatternsData.append(imageLocalBinaryPatterns)
    print('\n')

    cv2.waitKey(500)
    count += 1
np.savetxt("LocalBinaryPatternsData.csv", LocalBinaryPatternsData, delimiter='------')
