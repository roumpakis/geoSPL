# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:17:54 2023

@author: roub
"""
import feedparser
import requests
# Replace the URL with the actual RSS feed URL
import folium
import xml.etree.ElementTree as ET
geo_polygons = []
url = "https://emergency.copernicus.eu/mapping/list-of-components/"+'EMSN177'+"/aemfeed"
        
        # Make a request to the URL
response = requests.get(url)
        
        # Check if the request was successful (status code 200)
if response.status_code == 200:
            # Parse the feed using feedparser
    feed = feedparser.parse(response.content)