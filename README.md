

# Watermark Tree

simple command line python tool to 
Add both a visable and hidden, attack resistant watermark to images
Based on Blind watermark which is based on DWT-DCT-SVD.

Current version. crude, no options, but it works.

![Python](https://img.shields.io/badge/python->=3.5-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20|%20linux%20|%20macos-green.svg)
[![stars](https://img.shields.io/github/stars/guofei9987/blind_watermark.svg?style=social)](https://github.com/guofei9987/blind_watermark/)

Add both a visable and hidden watermark to every .png .jpg and .jpeg file in an entire directory tree

# install
```bash
clone the repo
pip install blind-watermark

```


# How to use
Create a watermark image, preferably .png with transparency. if you don't know how to do this, ask ChatGPT or bing image creator to create an image with transparency for you. 
Second edit the WatermarkerTree.py file change the copyright_message variable to be whatever you want it to be, this will get embedded into the image as a hidden watermark
Make the same change to WatermarkTester.py
Save it out then simply type:
Use in cmd or powershell window


```cmd
python WatermarkerTree.py "PAth To Your watermark Image"
```

to test a file if it has your watermark, 
first make sure the watermarkteseter.py file has the exact same copyright_message as your WatermarkerTree.py
In the directory with questionaable watermarked files
```cmd
python WatermarkTester.py
```
Output:
_Filename_: Watermark - _copywrite message_
_Filename_" : No matching watermark or different string





## Related Project
- blind_watermark (Embed text,image,binary data into an image): [https://github.com/guofei9987/blind_watermark](https://github.com/guofei9987/blind_watermark)  
