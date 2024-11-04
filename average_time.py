import cv2
import os
import time

# Load the trained Haar Cascade model
cascade_path = './classifier/cascade.xml'
cascade = cv2.CascadeClassifier(cascade_path)

# Define folder containing test images
test_images_folder = 'p'
image_files = [f for f in os.listdir(test_images_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Initialize variables to calculate average detection time
total_time = 0
total_faces = 0
image_count = len(image_files)

# Loop through each image in the folder
for image_file in image_files:
    # Load the image
    image_path = os.path.join(test_images_folder, image_file)
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Start timing the face detection
    start_time = time.time()
    faces = cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    detection_time = time.time() - start_time

    # Add detection time for this image to total time
    total_time += detection_time
    total_faces += len(faces)


# Calculate and print average detection times
average_time_per_image = total_time / image_count
average_time_per_face = total_time / total_faces if total_faces > 0 else 0

print("Average Detection Time per Image:", average_time_per_image, "seconds")
print("Average Detection Time per Face:", average_time_per_face, "seconds")
