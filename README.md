# Instant Checkout with Computer Vision:

Experience seamless shopping with our innovative computer vision system. Simply walk into the store filled with cameras that identify you with a unique ID. As you pick items, the system detects them automatically. Say goodbye to waiting in line at the checkout counter—your bill is conveniently sent straight to your phone. Enjoy the freedom to shop without the hassle of traditional checkout processes.

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

