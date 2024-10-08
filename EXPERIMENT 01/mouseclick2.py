import cv2
import numpy

print("lines on single click")
img = numpy.zeros((500, 600, 3), numpy.uint8) 
points = []
cv2.imshow('image', img)

def click_event (event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN :
        points.append(x)
        points.append(y)
        if len(points) >= 2:
            cv2.line(img, (points[-2], points[-1]),(points[-4], points[-3]), (255,255,0), 4)
            cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()