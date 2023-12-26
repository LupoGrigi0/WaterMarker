import os
import sys

directory = sys.argv[1]

for filename in os.listdir(directory):
    if ' ' in filename:
        new_filename = filename.replace(' ', '_')
        print(f"renaming {filename} to {new_filename}")
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))