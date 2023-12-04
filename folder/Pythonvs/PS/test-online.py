# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:52:38 2023

@author: roub
"""


from flask import Flask, jsonify, send_from_directory
import base64
from get_processed_image import get_processed_image
from get_most_recent import get_most_recent
import shutil
import os
import threading
import requests as rq

extension = "*.jpg"   
input_path =   "C:\\Users\\roub\\Desktop\\Pythonvs\\input\\" 
output_path = "C:\\Users\\roub\\Desktop\\Pythonvs\\output\\"
after_image_path = 'C:\\Users\\roub\\Desktop\\Pythonvs\\output\\processed.jpg'
# last_out_new_in(output_path,input_path,"processed.jpg")

# Define a function to run get_processed_image in a separate thread
def process_image_in_thread(before_image_path, after_image_path):
    get_processed_image(before_image_path, after_image_path)
    
    
# Function to read and encode an image file
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_image    



BASE_URL = "http://roubakas.pythonanywhere.com/"
payload = {'input':'dwdwdwdw'}
response = rq.get(BASE_URL,params=payload)
json_values = response.json()
re_input = json_values=['input']
print(re_input)