import cv2
import os

# Folder paths
input_folder = 'D:/ali/pppppp'          # Folder with original images
output_folder = 'D:/ali/ppppppp' # Folder to save resized images

# Target resolution
target_width, target_height = 1024, 600

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through each file in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is an image
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        # Construct the full path to the image
        file_path = os.path.join(input_folder, filename)
        
        # Read the image
        image = cv2.imread(file_path)
        
        # Resize the image to target resolution
        resized_image = cv2.resize(image, (target_width, target_height))
        
        # Construct the path to save the resized image
        output_path = os.path.join(output_folder, filename)
        
        # Save the resized image
        cv2.imwrite(output_path, resized_image)

print("All images have been resized to 1024x768 and saved.")
