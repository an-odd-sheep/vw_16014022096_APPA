
import cv2

img = cv2.imread('EXPERIMENT 01//bellingam.jpg', 0)
cv2.imshow('demo', img)

k = cv2.waitKey(0)

if (k == 27):
    cv2.destroyAllwindows()
else:
    k == ord("s")
    cv2.imwrite("newdemo.jpg", img)
    cv2.destroyAllWindows()