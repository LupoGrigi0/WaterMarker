# Watermarker2.py
import os
from PIL import Image
from blind_watermark import WaterMark
import time

# The watermark image path should be given as a command line argument
import sys
copyright_message = 'watermarked with guofei9987 blind_watermark v0.4.4 Copyright 2023,2024 Lupo Grigio'

watermark_path = sys.argv[1] if len(sys.argv) > 1 else ''
# Initialize the blind watermark with passwords
#mode can be nothing multithreading or multiprocessing
bwm = WaterMark(password_img=1, password_wm=2)

def add_watermark(image_path, watermark_path, output_dir):
    base_image = Image.open(image_path)
    watermark = Image.open(watermark_path)
    # Calculate the position for the watermark (bottom left corner)
    # position = (0, base_image.size[0] - watermark.size[1])
    # Calculate the position for the watermark (bottom Right corner)
    position = (base_image.size[0] - watermark.size[0], base_image.size[1] - watermark.size[1])
    # Paste the watermark into the base image
    base_image.paste(watermark, position, watermark)
    # Extract the file name without extension and add the 'watermarked' suffix
    file_name = os.path.splitext(os.path.basename(image_path))[0]
    new_file_name = f"{file_name}_watermarked.png"
    # Save the watermarked image
    base_image.save(os.path.join(output_dir, new_file_name))

for root, dirs, files in os.walk('.'):
    image_files = [f for f in files if f.endswith(('.png', '.jpg', '.jpeg'))]
    watermark_dir = os.path.join(root, 'watermarked')

    if not os.path.exists(watermark_dir):
        os.makedirs(watermark_dir)

    for file in image_files:
        full_file_path = os.path.join(root, file)
        if os.path.isfile(full_file_path):
            try:
                start_time = time.time()
                # Embed the hidden watermark
                bwm.read_img(full_file_path)
                bwm.read_wm(copyright_message, mode='str')
                watermarked_image_path = os.path.join(watermark_dir, f"{os.path.splitext(file)[0]}_hidden.png")
                bwm.embed(watermarked_image_path)

                # Apply the visible watermark
                add_watermark(watermarked_image_path, watermark_path, watermark_dir)
                os.remove(watermarked_image_path) 

                # Print the file name

                duration = time.time() - start_time
                print(f"it took {duration} to apply Watermark to {os.path.join(root, 'watermarked', watermarked_image_path)}")

            except Exception as e:
                print(f"Error processing {full_file_path}: {e}")
