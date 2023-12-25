from blind_watermark import WaterMark
import os

# Initialize the blind watermark with passwords
copyright_message = 'watermarked with guofei9987 blind_watermark v0.4.4 Copyright 2023,2024 Lupo Grigio'

bwm = WaterMark(password_img=1, password_wm=2)


# Process each image in the directory
for item in os.listdir('.'):
    if os.path.isfile(item) and item.endswith(('.png', '.jpg', '.jpeg')):
        bwm.read_img(item)
        bwm.read_wm(copyright_message, mode='str')
        # bwm.embed(item)
        len_wm = len(bwm.wm_bit)

        wm_extract = bwm.extract(item, wm_shape=len_wm, mode='str')
        if isinstance(wm_extract, str):
            if wm_extract == copyright_message:
                print(f"{item}: Watermark - {wm_extract}")
            else:
                print(f"{item}: No matching watermark or different string")
        else:
            print(f"{item}: No recognizable watermark or binary data")


