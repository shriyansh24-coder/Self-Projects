#Python File Detection

import os

file_path = "text.txt"

if os.path.exists(file_path):
    print("File exists.")

    if os.path.isfile(file_path):
        print("It is a file.")
    elif os.path.isdir(file_path):
        print("It is a directory.")    
    else:
        print("It is not a file.")
else:
    print("File does not exist.")
