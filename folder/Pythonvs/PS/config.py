# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:03:37 2023

@author: roub
"""

# gunicorn_config.py
bind = '0.0.0.0:8000'  # Set the host and port
workers = 4  # Adjust the number of worker processes based on your server's resources
app = 'app:app'  # Replace 'your_flask_app' with your Flask app name
