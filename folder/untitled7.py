# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 12:21:44 2023

@author: roub
"""
from copernicusNotify import copernicusNotify as CN
import requests
import feedparser
geo_polygons = []
cn = CN()
events = cn.get_all_notifications()

for e in events:
    url = "https://emergency.copernicus.eu/mapping/list-of-components/"+e['id']+"/aemfeed"
    print(e['id'])
    # Make a request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the feed using feedparser
        feed = feedparser.parse(response.content)
    
        # Check if the feed has entries
        if len(feed.entries) > 0:
            # Extract the georss:polygon from the first entry (assuming it's present)
            for i in range(len(feed.entries)):
                
                georss_polygon = feed.entries[i].where['coordinates']
                geo_polygons.append(georss_polygon)
                if georss_polygon:
                    print(f"georss:polygon: {georss_polygon}")
                else:
                    print("No georss:polygon found in the feed.")
            print(geo_polygons)
            
        else:
            print("No entries found in the feed.")
    else:
        print(f"Failed to fetch the URL. Status code: {response.status_code}")
