import numpy
import cv2 
print(cv2.__version__)

img = cv2.imread("D://Vrishank_A2//images.jpg", 1)

demoline = cv2.line(img,(150,0),(150,160),(255,0,0),2)
cv2.imshow("demoline", demoline)
cv2.waitKey(500)

democircle = cv2.circle(img, (150, 85), 50, (255,0,0), 2)
cv2.imshow("demoline", democircle)
cv2.waitKey(500)

demorectangle = cv2.rectangle(img, (100, 10), (200,160), (255,0,0), 2)
cv2.imshow("demoline", demorectangle)
cv2.waitKey(500)

demoellipse = cv2.ellipse(img, (150,85), (20, 16), 0, 0, 360 ,(255,0,0), -1)
cv2.imshow("demoline", demoellipse)
cv2.waitKey(500)

demotext = cv2.putText(img,"hello", (100,85), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (0,0,255))
cv2.imshow("demoline", demotext)
cv2.waitKey(500)

pts = numpy.array([[10,20],[30,40],[60,80],[90,100]], numpy.int32)
demopoly = cv2.polylines(img, [pts], True, (0,255,0), 2)
cv2.imshow("demoline", demopoly)
cv2.waitKey(500)

blackimage = numpy.zeros((500,500,3), numpy.uint8)
cv2.imshow("demoline", blackimage)
cv2.waitKey(500)

whiteimage = numpy.ones((500,500,3), numpy.uint8) *255
cv2.imshow("demoline", whiteimage)
cv2.waitKey(500)