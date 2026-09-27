import os

# Specify your source folder path
folder_path = r'C:\Users\Sai\Downloads\terrain dataset\Grass Terrain'

# Output folder for renamed and changed extension images
output_folder = r'C:\Users\Sai\Downloads\terrain dataset\New folder'

# Target extension (e.g., jpg)
new_extension = 'jpg'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to rename and change image extension
def process_images(folder_path, output_folder, new_extension):
    for filename in os.listdir(folder_path):
        # Check if the file has a supported image extension
        if filename.lower().endswith(('.png', '.jpg', '.jpeg','.webp')):
            file_path = os.path.join(folder_path, filename)

            # Generate a new filename with the specified extension
            new_filename = os.path.splitext(filename)[0] + f".{new_extension}"

            # Check if the destination file already exists
            counter = 1
            while os.path.exists(os.path.join(output_folder, new_filename)):
                new_filename = os.path.splitext(filename)[0] + f"_{counter}.{new_extension}"
                counter += 1

            # Save the renamed and changed extension image to the output folder
            os.rename(file_path, os.path.join(output_folder, new_filename))

# Call the function
process_images(folder_path, output_folder, new_extension)
