import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('EXPERIMENT 06/demo3.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray,(11,11),0)
canny = cv2.Canny(blur,30,150,3)
dilated=cv2.dilate(canny,(1,1),iterations=1)

cnt,hierarchy=cv2.findContours(dilated.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
image2 = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

cv2.drawContours(image2,cnt,-1,(0,255,0),2)
print("Coins in the image are:", len(cnt))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('original image')

plt.subplot(1, 2, 2)
plt.imshow(image2)
plt.title('contour image of coins')

plt.show()
