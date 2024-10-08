import cv2
events = [i for i in dir(cv2) if 'Event' in i]
print(events)