import cv2
import os

input_folder = 'p'
output_folder = 'DIP/pp'

os.makedirs(output_folder, exist_ok=True)
count = 1
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)

    if filename.endswith(('.jpg', '.jpeg', '.png')):
        image = cv2.imread(file_path)
    
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        output_path = os.path.join(output_folder, filename)
        print(output_path)
        cv2.imwrite(output_path, gray_image)
    count +=1
print("Completed")
