from ultralytics import YOLO
import cv2
from time import sleep

cap = cv2.VideoCapture(0)


model = YOLO('yolov8n-pose.pt')


while True:
    _, frame = cap.read()
    
    results = model.track(frame, persist = True)

    detection = results[0].plot()


    cv2.imshow("Person Tracking", detection)

    if cv2.waitKey(30) == 27:
        break
