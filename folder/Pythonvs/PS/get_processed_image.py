# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 09:40:19 2023

@author: roub
"""

def get_processed_image(image_path,output_path):
    import cv2
    import numpy as np
    print('you call process image!!!!!!!!!!')
    # Load the image
    # image_path = "your_image.jpg"
    image = cv2.imread(image_path)
    # cv2.imshow("Image", image)
    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load the image")
        exit()
    # Define the rotation angle (in degrees)
    angle = 90
    
    # Get the height and width of the image
    height, width = image.shape[:2]
    
    # Calculate the center of the image (rotation point)
    center = (width // 2, height // 2)
    
    # Create a rotation matrix using OpenCV
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Apply the rotation to the image
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    
    # Display the rotated image (optional)
    # cv2.imshow("Rotated Image", rotated_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Save the rotated image to a file
 
    cv2.imwrite(output_path, rotated_image)
    # cv2.imwrite(image_path, rotated_image)


