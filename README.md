

# SingleImageVisWatermark
Simple python script to apply visable watermark image to lower right hand corner of target image

# Usage
```bash
python SingleImageVisWatermark.py "D:\fully\qualified\path\to\my watermark.png" "c:\fully\qualified\path\to\my image.jpg"

```
A directory called watermarked will be created in the same directory as the second parameter "c:\fully\qualified\path\to\my image.jpg"
the watermarked image will be called my image_watermarked.jpg
NOTE. the resulting image will be converted to a .jpg file

The goal of this python script is to allow for the creation of a right click menu item in windows 

Type regedit and press Enter to open the Registry Editor
Navigate to the following path: HKEY_CLASSES_ROOT\*\shell
Right-click on the shell key, select New > Key, and name it whatever you want the context menu item to be
2.With the new key selected, right-click in the right pane, select New > String Value, and name it Icon. Double-click the new Icon value, type cmd.exe, and press Enter
3. Right-click on the new key you created, select New > Key, and name it command.
With the command key selected, in the right pane, double-click the Default value. In the Value data box, type 

cmd.exe /k python "D:\fully\qualified\path\to\SingleImageVisWatermark.py" "D:\fully\qualified\path\to\my watermark.png" %1

Note %1 is passed in fully qualified and with quotes. 
As soon as you enter this in right click on an image file (must be .png .jpg .jpeg .jfif)

# DirectoryeVisWatermark
Simple python script to apply visable watermark image to lower right hand corner of every image file in a directory
Intended to be bound to right click menu via the windows registry

# Usage
```bash
python DirectoryeVisWatermark.py "D:\fully\qualified\path\to\my watermark.png" "c:\fully\qualified\path"

```
A directory called watermarked will be created as a subdirectory of parameter #2 all the watermarked files will be put in that directory
the watermarked image will be called my image_watermarked.jpg
NOTE. the resulting image will be converted to a .jpg file

Type regedit and press Enter to open the Registry Editor1.
Navigate to the following path: HKEY_CLASSES_ROOT\
Right-click on the shell key, select New > Key, and name it whatever you want the context menu item to be
2.With the new key selected, right-click in the right pane, select New > String Value, and name it Icon. Double-click the new Icon value, type cmd.exe, and press Enter
3. Right-click on the new key you created, select New > Key, and name it command.
With the command key selected, in the right pane, double-click the Default value. In the Value data box, type 

cmd.exe /k python "D:\fully\qualified\path\to\DirectoryeVisWatermark.py" "D:\fully\qualified\path\to\my watermark.png" %1

Note %1 is passed in fully qualified and with quotes. 
As soon as you enter this in right click on a directory in explorer and all .png .jpg .jpeg .jfif files in the directory will be watermarked with your watermark

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
