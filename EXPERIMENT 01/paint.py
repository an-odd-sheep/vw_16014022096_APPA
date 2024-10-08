import cv2
import numpy as np

drawing = False
ix, iy = -1, -1

def nothing(x):
    pass

img = np.zeros((500, 700, 3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('Radius', 'image', 0, 10, nothing)
cv2.createTrackbar('Thickness', 'image', -1, 10, nothing)
cv2.createTrackbar('Shape', 'image', 0, 2, nothing)

def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, r, g, b, ra, crl, fb

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if crl == 0:
                cv2.circle(img, (x, y), ra, (b, g, r), fb)
            elif crl == 1: 
                cv2.rectangle(img, (ix, iy), (x, y), (b, g, r), fb)
            else:
                cv2.line(img, (ix, iy), (x, y), (b, g, r), fb)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if crl == 0:
            cv2.circle(img, (x, y), ra, (b, g, r), fb)
        elif crl == 1: 
            cv2.rectangle(img, (ix, iy), (x, y), (b, g, r), fb)
        else:
            cv2.line(img, (ix, iy), (x, y), (b, g, r), fb)

cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == 27: 
        break

    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    crl = cv2.getTrackbarPos('Shape', 'image')
    ra = cv2.getTrackbarPos('Radius', 'image')
    fb = cv2.getTrackbarPos('Thickness', 'image')

cv2.destroyAllWindows()
