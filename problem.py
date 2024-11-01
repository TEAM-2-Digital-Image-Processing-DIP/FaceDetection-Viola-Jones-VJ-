import cv2
import time
import numpy as np

# Load your trained Haar cascade XML file
cascade_path = 'DIP\classifier\cascade.xml'
cascade = cv2.CascadeClassifier(cascade_path)

# Define the path to your test image
image_path = 'testtt.jpg'

# Minimum and maximum face size trackers
min_face_size = None
max_face_size = None

# Detection time trackers
total_detection_time = 0
total_faces_detected = 0

# Loop through a set of images to get average detection times
for i in range(10):  # Testing on 10 images for better accuracy
    # Load and preprocess the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Start the timer
    start_time = time.time()
    
    # Detect faces in the image
    faces = cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,  # Adjust for different sizes
        minNeighbors=8,
        minSize=(200, 200),  # Start with a smaller min size to find min detectable size
        #maxSize=(189,189)
    )
    
    # Calculate detection time for this image
    detection_time = time.time() - start_time
    total_detection_time += detection_time
    total_faces_detected += len(faces)
    
    # Update min and max face size if faces are detected
    for (x, y, w, h) in faces:
        face_size = (w, h)
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Update min and max face sizes
        if min_face_size is None or (w * h) < (min_face_size[0] * min_face_size[1]):
            min_face_size = face_size
        if max_face_size is None or (w * h) > (max_face_size[0] * max_face_size[1]):
            max_face_size = face_size

    print(f"Image {i+1} Detection Time: {detection_time:.4f} seconds, Faces Detected: {len(faces)}")

# Calculate averages
average_detection_time_per_image = total_detection_time / 10  # For 10 images
average_detection_time_per_face = total_detection_time / total_faces_detected if total_faces_detected else 0

print("\n--- Detection Results ---")
print(f"Minimum Detectable Face Size: {min_face_size}")
print(f"Maximum Detectable Face Size: {max_face_size}")
print(f"Average Detection Time per Image: {average_detection_time_per_image:.4f} seconds")
print(f"Average Detection Time per Face: {average_detection_time_per_face:.4f} seconds")
cv2.imwrite("this.jpg", image)