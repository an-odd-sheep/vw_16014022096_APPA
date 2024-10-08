import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('EXPERIMENT 02/bellingam.jpg', 1)
img = cv2.resize(img, (400, 300))

reflect = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_REFLECT)
replicate = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_REPLICATE)
constant = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=(0, 0, 255))
wrap = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_WRAP)
reflect101 = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_REFLECT_101)


plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original')

plt.subplot(2, 3, 2)
plt.imshow(reflect, cmap='gray')
plt.title('Reflect')

plt.subplot(2, 3, 3)
plt.imshow(replicate, cmap='gray')
plt.title('Replicate')

plt.subplot(2, 3, 4)
plt.imshow(constant, cmap='gray')
plt.title('Constant')

plt.subplot(2, 3, 5)
plt.imshow(wrap, cmap='gray')
plt.title('Wrap')

plt.subplot(2, 3, 6)
plt.imshow(reflect101, cmap='gray')
plt.title('Reflect 101')

plt.show()
