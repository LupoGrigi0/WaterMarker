# Directory VisWatermark.py
# applies the first parameter as an image to the lower right of all the images in the directory passed as the second parameter which must be a .jpg .jpeg .png or .jfif
import os
from PIL import Image
import time

# The watermark image path should be given as a command line argument
import sys
copyright_message = 'Copyright 2023,2024 Lupo Grigio'

if len(sys.argv) <= 2:
    sys.exit("Usage:python DirectoryVisWatermark.py watermark_image_path Directory_to_watermark")

watermark_path = sys.argv[1] if len(sys.argv) > 1 else ''
Directory_to_watermark = sys.argv[2] if len(sys.argv) > 2 else ''


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
    new_file_name = f"{file_name}_watermarked.jpg"
    JpegOutput = base_image.convert('RGB')
    # Save the watermarked image
    JpegOutput.save(os.path.join(output_dir, new_file_name))


watermark_dir = os.path.join(Directory_to_watermark, 'watermarked')

# Debug output
# print(os.getcwd())
print(f"watermarking files in {Directory_to_watermark}")

try:
    if not os.path.exists(watermark_dir):
        print(f"creating watermark dir {watermark_dir}")
        os.makedirs(watermark_dir)

except Exception as e:
    print(f"Error could not create {watermark_dir}: {e}")
    
for item in os.listdir(Directory_to_watermark):
    image_to_watermark = os.path.join(Directory_to_watermark,item)
    # more debug, helpful when debugging registry entry
    # print(f"processing {image_to_watermark} is {os.path.isfile(image_to_watermark)} is image is {image_to_watermark.endswith(('.png', '.jpg', '.jpeg', '.jfif'))} ")
    if os.path.isfile(image_to_watermark) and image_to_watermark.endswith(('.png', '.jpg', '.jpeg', '.jfif')):
        try:

            start_time = time.time()

            # Apply the visible watermark
            add_watermark(image_to_watermark, watermark_path, watermark_dir)

            # Print the file name and how long it took

            duration = time.time() - start_time
            print(f"it took {duration} to apply Watermark to {image_to_watermark}")

        except Exception as e:
            print(f"Error processing {image_to_watermark}: {e}")
