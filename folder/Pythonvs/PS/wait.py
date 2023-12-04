# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:10:53 2023

@author: roub
"""

from waitress import serve
from app import app  

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=80)
