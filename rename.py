
import os

# Folder containing images to rename
folder_path = 'mert'

# Define a new base name for images
base_name = "image"

# Initialize a counter
counter = 508

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image (e.g., jpg, jpeg, png)
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        # Build the new filename with counter
        new_name = f"{base_name}_{counter}.jpg"
        
        # Construct full file paths
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_file, new_file)
        
        # Increment the counter
        counter += 1

print("All images have been renamed.")
