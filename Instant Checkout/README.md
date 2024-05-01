# Required Modules

pip3 install utralytics
pip3 install opencv-python
pip3 install pymysql
pip3 install mediapipe


# Instant Checkout/Object Detection/live-object-detection.py
Detects Objects and creates a bounding box for their position
Only detects objects provided in corresponding_objects
If more objects have to be detected, add their name in corresponding_objects and their respective id in valid_ids.
(You can view the id and names of objects in Instant Checkout/coco128.yaml)

# Instant Checkout/Object Tracking/object-tracking.py
Determines if products are in stock or in virtual cart and updates them in the database

# Instant Checkout/Person Tracking/main.py
Implemented skeleton annotation and tracking each person by assigning them unique identifiers

# Instant Checkout/Person Tracking With Hand Gestures/main.py
Skeleton annotation with additional hand tracking features

# Instant Checkout/Index Coordinate Tracking/app.py
Determines object closest to index finger

