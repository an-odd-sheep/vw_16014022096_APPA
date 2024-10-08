import cv2
import numpy

img = cv2.imread("D://Vrishank_A2//23july//bellingam.jpg", 1)
ball = img[700:810, 650:750]
img[100:200, 150:250] = ball

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
