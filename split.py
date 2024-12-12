import os
import shutil
import random

# Set the paths
source_folder = 'D:/playground/field_island_presence/rgb_a'
training_folder = 'D:/playground/field_island_presence/train/absent'
testing_folder = 'D:/playground/field_island_presence/test/absent'

# Create the training and testing folders if they don't exist
os.makedirs(training_folder, exist_ok=True)
os.makedirs(testing_folder, exist_ok=True)

# Get a list of all .tif files in the source folder
tif_files = [f for f in os.listdir(source_folder) if f.endswith('.tif')]

# Shuffle the list to ensure random distribution
random.shuffle(tif_files)

# Define the split ratio
split_ratio = 0.8
split_index = int(len(tif_files) * split_ratio)

# Split the files into training and testing sets
training_files = tif_files[:split_index]
testing_files = tif_files[split_index:]

# Move the files to the respective folders
for file in training_files:
    shutil.move(os.path.join(source_folder, file), os.path.join(training_folder, file))

for file in testing_files:
    shutil.move(os.path.join(source_folder, file), os.path.join(testing_folder, file))

print(f"Moved {len(training_files)} files to the training folder.")
print(f"Moved {len(testing_files)} files to the testing folder.")