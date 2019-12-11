import cv2
import numpy
from matplotlib import pyplot as plt

objectImageGray = cv2.imread("object.jpeg")
objectInScene = cv2.imread("objectInScene.jpeg")
objectImageGray = cv2.resize(objectImageGray, dsize = (400, 500))
objectInScene = cv2.resize(objectInScene, dsize = (400, 500))


#sift = cv2.xfeatures2d.SIFT_create()
orb = cv2.ORB_create()


objectKeypoints, objectDescriptors = orb.detectAndCompute(objectImageGray, None)
sceneKeypoints, sceneDescriptors = orb.detectAndCompute(objectInScene, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(objectDescriptors, sceneDescriptors)

result = cv2.drawMatches(objectImageGray, objectKeypoints, objectInScene, sceneKeypoints, matches[:60], None,flags=2)


cv2.imshow("result", result)
cv2.waitKey(0)

cv2.imwrite("siftResult.jpg", result)
