import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('Canny Edge Detection')
cv2.createTrackbar('Threshold1', 'Canny Edge Detection', 0, 255, nothing)
cv2.createTrackbar('Threshold2', 'Canny Edge Detection', 0, 255, nothing)

cv2.setTrackbarPos('Threshold1', 'Canny Edge Detection', 50)
cv2.setTrackbarPos('Threshold2', 'Canny Edge Detection', 150)

image = cv2.imread('EXPERIMENT 03//bellingam.jpg', cv2.IMREAD_GRAYSCALE)
while True:
    thresh1 = cv2.getTrackbarPos('Threshold1', 'Canny Edge Detection')
    thresh2 = cv2.getTrackbarPos('Threshold2', 'Canny Edge Detection')
    edges = cv2.Canny(image, thresh1, thresh2)
    cv2.imshow('Canny Edge Detection', edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
