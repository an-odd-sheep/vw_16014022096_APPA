import cv2
import matplotlib.pyplot as plt

image = cv2.imread('EXPERIMENT 03//bellingam.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

contours1, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours2, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours3, _ = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
contours4, _ = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours5, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours6, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

image1 = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
image2 = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
image3 = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
image4 = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
image5 = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
image6 = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)

cv2.drawContours(image1, contours1, -1, (255, 0, 0), 2)
cv2.drawContours(image2, contours2, -1, (0, 255, 0), 2)
cv2.drawContours(image3, contours3, -1, (0, 0, 255), 2)
cv2.drawContours(image4, contours4, -1, (255, 255, 0), 2)
cv2.drawContours(image5, contours5, -1, (0, 255, 255), 2)
cv2.drawContours(image6, contours6, -1, (255, 0, 255), 2)

plt.subplot(231)
plt.imshow(image1, cmap='gray')
plt.title('TREE + NONE')

plt.subplot(232)
plt.imshow(image2, cmap='gray')
plt.title('TREE + SIMPLE')

plt.subplot(233)
plt.imshow(image3, cmap='gray')
plt.title('LIST + NONE')

plt.subplot(234)
plt.imshow(image4, cmap='gray')
plt.title('LIST + SIMPLE')

plt.subplot(235)
plt.imshow(image5, cmap='gray')
plt.title('EXTERNAL + NONE')

plt.subplot(236)
plt.imshow(image6, cmap='gray')
plt.title('EXTERNAL + SIMPLE')

plt.show()
