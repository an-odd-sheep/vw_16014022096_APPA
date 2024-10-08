import numpy
import cv2 

whiteimage = numpy.ones((500,500,3), numpy.uint8) *255

demoline = cv2.line(whiteimage,(50,100),(250,400),(255,0,0),2)

demoline2 = cv2.line(whiteimage,(250,400),(440,100),(255,0,0),2)

demoline2 = cv2.line(whiteimage,(20,300),(20,400),(255,0,0),2)
demoline2 = cv2.line(whiteimage,(20,350),(40,400),(255,0,0),2)


demoline2 = cv2.line(whiteimage,(60,400),(60,400),(255,0,0),2)

demotext = cv2.putText(whiteimage,"rishank", (150,250), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (0,0,255))
cv2.imshow("demoline", demotext)
cv2.waitKey(0)