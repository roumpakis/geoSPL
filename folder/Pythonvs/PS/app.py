

from flask import Flask, jsonify, send_from_directory
import base64
from get_processed_image import get_processed_image
from get_most_recent import get_most_recent
import shutil
import os
import threading
from flask import Flask, render_template, redirect,url_for

    
extension = "*.jpg"   
input_path =   "C:\\Users\\roub\\Desktop\\Pythonvs\\input\\" 
output_path = "C:\\Users\\roub\\Desktop\\Pythonvs\\output\\"
after_image_path = 'C:\\Users\\roub\\Desktop\images\\after.jpeg'
before_image_path = 'C:\\Users\\roub\\Desktop\images\\before.jpeg'

mask_img = 'C:\\Users\\roub\\Desktop\\folder_sentinel\\folder\\mapicons\\f\\response.jpg'
# last_out_new_in(output_path,input_path,"processed.jpg")

# Define a function to run get_processed_image in a separate thread
def process_image_in_thread(before_image_path, after_image_path):
    get_processed_image(before_image_path, after_image_path)
	
app = Flask(__name__)
# 
# Function to read and encode an image file
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_image




@app.route('/get_images', methods=['GET'])
def get_images():
    # before_image_path =get_most_recent(input_path,extension)
    # process_thread = threading.Thread(target=process_image_in_thread, args=(before_image_path, after_image_path))
    # process_thread.start()

   
    # get_processed_image(before_image_path,after_image_path)

    encoded_before_image = encode_image(before_image_path)
    encoded_after_image = encode_image(after_image_path)
    encoded_mask_img = encode_image(mask_img)
    # print(str(encoded_mask_img))

    images = {
        'before_image': encoded_before_image,
        'after_image': encoded_after_image,
        'mask_img':encoded_mask_img,
    }
    # print(images)
    # redirect(url_for('event'))
    return jsonify(images)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

