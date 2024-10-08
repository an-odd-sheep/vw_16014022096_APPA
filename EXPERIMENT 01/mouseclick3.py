import cv2
import numpy

print("left click for coordinates and right click for rgb value")
img = cv2.imread('EXPERIMENT 01//bellingam.jpg',1)
cv2.imshow('image', img)

def click_event2(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x)+','+str(y)
        cv2.putText(img, strXY, (x,y), font, 1, (255,255,0), 2)
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(red)+','+str(green)+','+str(blue)
        cv2.putText(img, strXY, (x,y), font, 1, (255,255,0), 2)
        cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event2)
cv2.waitKey(0)