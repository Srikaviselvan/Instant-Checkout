# Import necessary libraries
from ultralytics import YOLO
import cv2
from tkinter import *
from threading import Thread
from time import sleep

# Initialize YOLO model
model = YOLO("yolov8n.pt")

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

        # Perform object detection using the YOLO model
        detections = model(frame)[0] # To select the detection with the highest confidence threshold

        # Initialize an empty list to store IDs from detections
        all_ids = []

        # Initialize an empty list to store corresponding names
        corresponding_names = []


        for detection in detections.boxes.data.tolist():
            # Append the id of the detected object to 'all_ids'
            all_ids.append(detection[-1])

        # Initialize an empty list to store object IDs
        object_ids = []

        # Define a list of valid object IDs
        valid_ids = [0, 39, 41, 43, 45, 67, 76, 44]

        # Define a list of corresponding object names for the valid IDs
        corresponding_objects = ['Person', 'Water Bottle', 'Cup', 'Knife', 'Bowl', 'Cell Phone', 'Scissors', 'Spoon']


        for i in range(len(corresponding_names)):
            # Check if the corresponding name at index 'i' is in the list of valid IDs
            if corresponding_names[i] in valid_ids:
                # Replace the corresponding name with the corresponding object name
                corresponding_names[i] = corresponding_objects[valid_ids.index(corresponding_names[i])]


        for id in all_ids:
            # Check if 'id' is in the list of valid IDs
            if id in valid_ids:
                # Append the valid 'id' to the 'object_ids' list
                object_ids.append(id)

        # Create a list of unique object IDs
        unique_object_ids = list(set(object_ids))

        # Initialize an empty list to store the count of each object
        object_count = []

        # Iterate through each unique object ID
        for id in unique_object_ids:
            # Count the occurrences of the object ID in 'object_ids' and append it to 'object_count'
            object_count.append(object_ids.count(id))

        # Initialize an empty list to store the names of objects corresponding to the unique object IDs
        objects = []

        # Iterate through each unique object ID.
        for id in unique_object_ids:
            # Find the corresponding object name based on the index of the ID in 'valid_ids'
            objects.append(corresponding_objects[valid_ids.index(id)])

        # Initialize an empty string to build the final display string
        string_to_display = ""

        for i in range(len(objects)):
            # Create a formatted string with the object count and name and concatenate it to 'string_to_display'
            string_to_display += f"{object_count[i]} {objects[i]}(s)\n"


        # Draw bounding boxes and labels on the frame
        for detection in detections.boxes.data.tolist():
            if int(detection[-1]) in valid_ids:
                cv2.rectangle(frame, (int(detection[0]), int(detection[1])), (int(detection[2]), int(detection[3])), (0, 255, 0), 2)
                cv2.putText(frame, corresponding_objects[valid_ids.index(int(detection[-1]))], (int(detection[0]), int(detection[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)

        # Display the frame with object detection
        cv2.imshow("Object Detection", frame)

        # Exit the loop when the 'Esc' key is pressed
        if cv2.waitKey(30) == 27:
            break

# Start separate threads for object detection, Tkinter GUI, and displaying text
Thread(target=detect_objects).start()
Thread(target=start_tkinter).start()
Thread(target=display_in_tkinter).start()
