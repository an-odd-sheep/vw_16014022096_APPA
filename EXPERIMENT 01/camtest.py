import cv2

cap = cv2.VideoCapture('EXPERIMENT 01//roberto.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', grey)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
