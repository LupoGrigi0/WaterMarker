# SingleImageVisWatermark.py
# applies the first parameter as an image to the lower right of the second parameter which must be a .jpg .jpeg or .png
import os
from PIL import Image
import time

# The watermark image path should be given as a command line argument
import sys
copyright_message = 'Copyright 2023,2024 Lupo Grigio'

if len(sys.argv) <= 2:
    sys.exit("Usage: SingleImageVisWatermark.py watermark_image_path image_to_watermark")

watermark_path = sys.argv[1] if len(sys.argv) > 1 else ''
image_to_watermark = sys.argv[2] if len(sys.argv) > 2 else ''


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


root = os.path.dirname(image_to_watermark)
watermark_dir = os.path.join(root, 'watermarked')

# Debug output
print(os.getcwd())
print(image_to_watermark)
print(f" is file {os.path.isfile(image_to_watermark)} ends with {image_to_watermark.endswith(('.png', '.jpg', '.jpeg', '.jfif'))} image is file {os.path.isfile(watermark_path)}")


if os.path.isfile(image_to_watermark) and image_to_watermark.endswith(('.png', '.jpg', '.jpeg', '.jfif')) and os.path.isfile(watermark_path):
    print("both files exist")
    try:
        if not os.path.exists(watermark_dir):
            print(f"creating watermark dir {watermark_dir}")
            os.makedirs(watermark_dir)

        start_time = time.time()

        # Apply the visible watermark
        add_watermark(image_to_watermark, watermark_path, watermark_dir)

        # Print the file name

        duration = time.time() - start_time
        print(f"it took {duration} to apply Watermark to {image_to_watermark}")

    except Exception as e:
        print(f"Error processing {image_to_watermark}: {e}")
