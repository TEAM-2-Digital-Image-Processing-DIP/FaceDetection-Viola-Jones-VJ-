import cv2
import os
import numpy as np

cascade_path = 'classifier/cascade.xml'
cascade = cv2.CascadeClassifier(cascade_path)

challenge_folders = {
    'viewpoint_variation': 'challenges_Source/Viewpoint Variation',
    'deformation': 'challenges_Source/Deformation',
    'occlusion': 'challenges_Source/Occlusion',
    'illumination': 'challenges_Source/Illumination',
    'cluttered_background': 'challenges_Source/Cluttered Background',
    'intra_class_variation': 'challenges_Source/IntraClass Variation'
}
output_folder = 'results_of_challenges'
os.makedirs(output_folder, exist_ok=True)

log = {challenge: {'correct': 0, 'missed': 0} for challenge in challenge_folders}
 
def evaluate_detection(image):
    detected_faces = cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return detected_faces

for challenge, folder_path in challenge_folders.items():
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        image = cv2.imread(file_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        detected_faces = evaluate_detection(gray)

        if len(detected_faces) > 0:
            log[challenge]['correct'] += 1
            for (x, y, w, h) in detected_faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            log[challenge]['missed'] += 1

        output_path = os.path.join(output_folder, f"{challenge}_{filename}")
        cv2.imwrite(output_path, image)

for challenge, results in log.items():
    print(f"\nChallenge: {challenge}")
    print(f"Correct Detections: {results['correct']}")
    print(f"Missed Detections: {results['missed']}")
