import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print("demo hello")

image = cv2.imread('EXPERIMENT 06/demo2.jpg')
kernel = np.ones((2, 1), np.uint8)
img1 = cv2.erode(image, kernel, iterations=1)
img2 = cv2.dilate(image, kernel, iterations=1)
out_below = pytesseract.image_to_string(image)

print("OUTPUT: \n", out_below)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img2_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(img2_rgb)
plt.title('Dilated Image')

plt.show()


