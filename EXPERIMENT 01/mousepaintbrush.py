import cv2
import numpy as np

drawing = False
ix, iy = -1, -1

def nothing(x):
    pass

img = np.zeros((500, 600, 3), np.uint8)
cv2.namedWindow('image')

def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, r, g, b, s

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(img, (x, y), 4, (255, 255, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, (x, y), 4, (255, 255, 255), -1)

cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == 27:  
        break


cv2.destroyAllWindows()
