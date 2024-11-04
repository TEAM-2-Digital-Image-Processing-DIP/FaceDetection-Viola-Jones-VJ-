import cv2
import os

input_folder = 'D:/ali/pppppp'        
output_folder = 'Deformation' 

target_width, target_height = 1024, 600

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        file_path = os.path.join(input_folder, filename)
        image = cv2.imread(file_path)

        resized_image = cv2.resize(image, (target_width, target_height))
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, resized_image)

print("Completed")
