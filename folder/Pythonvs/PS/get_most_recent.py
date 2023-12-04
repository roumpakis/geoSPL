# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 10:35:00 2023

@author: roub
"""

import os
import glob

def get_most_recent(folder_path,extension):
 # Replace with the path to your folder
    
    # Use glob to search for all .jpg files in the folder
    jpg_files = glob.glob(os.path.join(folder_path, extension))
    
    # Check if there are any .jpg files in the folder
    if jpg_files:
        # Get the most recent .jpg file based on file modification time
        most_recent_file = max(jpg_files, key=os.path.getmtime)
        print(f"The most recent .jpg file is: {most_recent_file}")
        return most_recent_file
    else:
        print("No .jpg files found in the folder.")
    
        