# to get file with its extention

import os
file = input("Enter a file with extention")# file.mp3
file_name, file_extention = os.path.splitext(file)
print("File name is "+file_name)
print("Extention name is "+file_extention)
