import cv2 
import numpy 

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 10, (255, 0 , 255), 2)
        cv2.imshow('image', img)


img = numpy.zeros((500, 600, 3), numpy.uint8) 
points = []
cv2.imshow('image', img)

cv2.setMouseCallback('image', draw_circle)
cv2.waitKey(0)