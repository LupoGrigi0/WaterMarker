import os
import shutil

for root, dirs, files in os.walk('.', topdown=False):
    for name in dirs:
        if name == 'watermarked':
            shutil.rmtree(os.path.join(root, name))
