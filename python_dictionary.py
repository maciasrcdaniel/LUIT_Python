#!/usr/bin/env python3
# Import the os module
import os

# Store files from for loop 
file_list = []

# List the files in the current working directory
current_directory = os.getcwd()
list_current = os.listdir(current_directory)

# Iterate through current working directory
for file in list_current:
        # Get the file size 
        file_size = os.path.getsize(file)
        # Format your dictionary
        dict_files = {
            'file_name': file,
            'file_size_in_bytes': file_size
        }
        # Add your files/sizes to the file list to store
        file_list.append(dict_files)

# For every time in file_list --> print       
for dict_files in file_list: 
        print(dict_files)

