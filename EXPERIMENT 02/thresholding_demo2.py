import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('EXPERIMENT 02/bellingam.jpg')
_, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
adaptive_thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
_, otsu_thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


plt.subplot(221)
plt.imshow(image)
plt.title('ORIGINAL')

plt.subplot(222)
plt.imshow(thresh1)
plt.title('Simple Thresholding')

plt.subplot(223)
plt.plot(adaptive_thresh)
plt.title('Adaptive Thresholding')

plt.subplot(224)
plt.plot(otsu_thresh)
plt.title('Otsu\'s Thresholding')

plt.show()