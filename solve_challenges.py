import cv2
import os
import numpy as np

# Load the Haar Cascade XML file
cascade_path = 'D:/ali/DIP/haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(cascade_path)

# Define the folders for each challenge
challenge_folders = {
    'viewpoint_variation': 'Viewpoint Variation',
    'deformation': 'Deformation',
    'occlusion': 'Occlusion',
    'illumination': 'Illumination',
    'cluttered_background': 'Cluttered Background',
    'intra_class_variation': 'IntraClass Variation'
}
output_folder = 'D:/ali/DIP/rasm'
os.makedirs(output_folder, exist_ok=True)
   
# Initialize a log dictionary to store results
log = {challenge: {'correct': 0, 'missed': 0} for challenge in challenge_folders}
 
# Function to evaluate detection
def evaluate_detection(image):
    detected_faces = cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return detected_faces

# Loop through each challenge folder
for challenge, folder_path in challenge_folders.items():
    for filename in os.listdir(folder_path):
        # Load and convert image to grayscale
        file_path = os.path.join(folder_path, filename)
        image = cv2.imread(file_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Perform face detection
        detected_faces = evaluate_detection(gray)

        # Draw rectangles around detected faces and count detections
        if len(detected_faces) > 0:
            log[challenge]['correct'] += 1
            for (x, y, w, h) in detected_faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle for detected face
        else:
            log[challenge]['missed'] += 1

        # Show the image with detections
        output_path = os.path.join(output_folder, f"{challenge}_{filename}")
        cv2.imwrite(output_path, image)

# Summarize Results
for challenge, results in log.items():
    print(f"\nChallenge: {challenge}")
    print(f"Correct Detections: {results['correct']}")
    print(f"Missed Detections: {results['missed']}")
