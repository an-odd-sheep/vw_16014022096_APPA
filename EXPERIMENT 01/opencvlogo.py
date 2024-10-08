import cv2
import numpy 

image = numpy.ones((600, 600, 3), numpy.uint8) * 255
cv2.ellipse(image, (190, 400), (100, 100), 0, 0, 300, (0, 255, 0), -1)
cv2.ellipse(image, (410, 400), (100, 100), 300, 0, 300, (255, 0, 0), -1)
cv2.ellipse(image, (300, 200), (100, 100), 120, 0, 300, (0, 0, 255), -1)
cv2.ellipse(image, (190, 400), (40, 40), 0, 0, 300, (255, 255, 255), -1)
cv2.ellipse(image, (410, 400), (40, 40), 300, 0, 300,(255, 255, 255), -1)
cv2.ellipse(image, (300, 200), (40, 40), 120, 0, 300, (255, 255, 255), -1)
cv2.putText(image, 'vrishank.w', (300,550), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0,0,0))

cv2.imshow("OpenCV Logo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()