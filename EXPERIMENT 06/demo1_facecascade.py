import numpy as np
import cv2
import matplotlib.pyplot as plt

faceCascade = cv2.CascadeClassifier('EXPERIMENT 06/haarcascade_frontalface_default.xml')

image = cv2.imread('EXPERIMENT 06/demo.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,minSize=(30, 30))
print(f"Found {len(faces)} faces!")

image2 = image.copy()

for (x, y, w, h) in faces:
    cv2.rectangle(image2, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('original image')

plt.subplot(1, 2, 2)
plt.imshow(image2)
plt.title('face cascade image')

plt.show()


