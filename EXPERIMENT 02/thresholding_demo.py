import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('EXPERIMENT 02/bellingam.jpg', 0)
img = cv2.resize(img, (400, 300))

ret, thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)


plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original')

plt.subplot(2, 3, 2)
plt.imshow(thresh1, cmap='gray')
plt.title('thresh1')

plt.subplot(2, 3, 3)
plt.imshow(thresh2, cmap='gray')
plt.title('thresh2')

plt.subplot(2, 3, 4)
plt.imshow(thresh3, cmap='gray')
plt.title('thresh3')

plt.subplot(2, 3, 5)
plt.imshow(thresh4, cmap='gray')
plt.title('thresh4')

plt.subplot(2, 3, 6)
plt.imshow(thresh5, cmap='gray')
plt.title('thresh5')

plt.show()
