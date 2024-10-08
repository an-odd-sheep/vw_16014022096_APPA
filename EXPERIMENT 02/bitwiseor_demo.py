import cv2
import numpy as np


img = cv2.imread('EXPERIMENT 02/bellingam.jpg', 1)
img = cv2.resize(img, (637, 313))

img1 = cv2.imread('EXPERIMENT 02/opencv.jpg', 1)
img1 = cv2.resize(img1, (637, 313))


mark = cv2.bitwise_or(img,img1)

cv2.imshow('BITWISE OR', mark)
cv2.waitKey(0)
cv2.destroyAllWindows()
