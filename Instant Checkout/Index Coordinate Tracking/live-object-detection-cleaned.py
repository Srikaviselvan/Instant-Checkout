# Import necessary libraries
from ultralytics import YOLO
import cv2
from tkinter import *
from threading import Thread
from time import sleep

# Initialize YOLO object_detection_model
object_detection_model = YOLO("yolov8m.pt")

# Initialize the webcam capture
cap = cv2.VideoCapture(0)

# Function to display text in a Tkinter window
def display_in_tkinter():
    while True:
        try:
            # Clear the text field
            field.delete(1.0, END)
            # Insert the string_to_display into the text field
            field.insert('insert', string_to_display)
        except:
            continue
        sleep(0.01)

# Function to start the Tkinter GUI
def start_tkinter():
    global field
    window = Tk()
    field = Text(window, width=40, height=10)
    field.pack()
    window.mainloop()

# Function to detect objects using YOLO and update the display
def detect_objects():
    while True:
        global string_to_display
        _, frame = cap.read()

        # Perform object detection using the YOLO object_detection_model
        detections = object_detection_model(frame)[0]

        all_ids = []

        corresponding_names = []

        for detection in detections.boxes.data.tolist():
            all_ids.append(detection[-1])

        object_ids = []

        valid_ids = [0, 39, 41, 43, 45, 67, 76, 44]
        corresponding_objects = ['Person', 'Water Bottle', 'Cup', 'Knife', 'Bowl', 'Cell Phone', 'Scissors', 'Spoon']

        for i in range(len(corresponding_names)):
            if corresponding_names[i] in valid_ids:
                corresponding_names[i] = corresponding_objects[valid_ids.index(corresponding_names[i])]

        for id in all_ids:
            if id in valid_ids:
                object_ids.append(id)

        unique_object_ids = list(set(object_ids))

        object_count = []

        for id in unique_object_ids:
            object_count.append(object_ids.count(id))

        objects = []

        for id in unique_object_ids:
            objects.append(corresponding_objects[valid_ids.index(id)])

        string_to_display = ""

        for i in range(len(objects)):
            string_to_display += f"{object_count[i]} {objects[i]}(s)\n"

        # Draw bounding boxes and labels on the frame
        for detection in detections.boxes.data.tolist():
            if int(detection[-1]) in valid_ids:
                cv2.rectangle(frame, (int(detection[0]), int(detection[1])), (int(detection[2]), int(detection[3])), (0, 255, 0), 2)
                cv2.putText(frame, corresponding_objects[valid_ids.index(int(detection[-1]))], (int(detection[0]), int(detection[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)

        # Display the frame with object detection
        cv2.imshow("Object Detection", frame)

        # Exit the loop when the 'Esc' key is pressed
        if cv2.waitKey(30) == 27:
            break

# Start separate threads for object detection, Tkinter GUI, and displaying text
Thread(target=detect_objects).start()
Thread(target=start_tkinter).start()
Thread(target=display_in_tkinter).start()
