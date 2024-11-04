
import os
folder_path = 'p'

base_name = "image"
counter = 0

for filename in os.listdir(folder_path):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        new_name = f"{base_name}_{counter}.jpg"

        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)

        os.rename(old_file, new_file)

        counter += 1

print("Completed")
