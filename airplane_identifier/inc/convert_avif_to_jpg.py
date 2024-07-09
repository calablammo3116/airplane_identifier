import os
from PIL import Image
import pillow_avif

def convert_avif_to_image(file_path, output_format):
    with Image.open(file_path) as img:
        # Split the file path into name and extension
        file_root, _ = os.path.splitext(file_path)
        # Construct the new file path with the desired extension
        new_file_path = f"{file_root}.{output_format}"
        img.save(new_file_path, format=output_format.upper())

def convert_avif_files_in_directory(directory, output_format='jpg'):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.avif'):
                avif_file_path = os.path.join(root, file)
                convert_avif_to_image(avif_file_path, output_format)
                print(f"Converted: {avif_file_path} to {output_format.upper()}")

if __name__ == "__main__":
    current_directory = os.getcwd()
    output_format = 'jpg'  # Change to 'jpeg' or 'png' as needed
    convert_avif_files_in_directory(current_directory, output_format)
