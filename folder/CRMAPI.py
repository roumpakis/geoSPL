# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 11:10:35 2023

@author: roub
"""

import requests
import requests
from bs4 import BeautifulSoup
import folium


from folium.plugins import MarkerCluster, Draw

class CRMAPI():
  # default constructor
    def __init__(self):
        self.events,self.events_ids = self.get_all_EMSR()
        
    def get_all_EMSR(self):
        # Define the URL of the page to scrape
        url = "https://poc-d8.lolandese.site/search-activations1"
        
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page with BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")
        
            # Find the tbody element
            tbody = soup.find("table").find("tbody")
            all_events = []
            if tbody:
                # Find all rows (tr) within the tbody
                rows = tbody.find_all("tr")
        
                # Loop through the rows and print their content
                for row in rows:
                    # Find all cells (td) within the row
                    cells = row.find_all("td")
                    per_event = []
                    # Extract and print the text from each cell
                    for cell in cells:
                        # print(cell.get_text(strip=True))
                        per_event.append(cell.get_text(strip=True))
                    all_events.append(per_event)                
            else:
                print("Tbody not found on the page.")
        
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
        events_ids = []
        for e in all_events:
            code = e[1]
            description = e[2]
            date = e[3]
            event = e[4]
            loc = e[5]
            events_ids.append(code)
        
        base = "https://emergency.copernicus.eu/mapping/list-of-components/"
         
        link = base+code
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        return all_events[:10],events_ids[:10]



    def get_event_details(self,event_id):
        url = "https://rapidmapping.emergency.copernicus.eu/backend/dashboard-api/public-activations/"
        params = {
            "code": event_id  # Replace with the actual activation code you want to query
        }
        
        try:
            response = requests.get(url, params=params)
        
            if response.status_code == 200:
                # Print the JSON response
                # print(response.json())
                results = response.json()
                return results
            else:
                print(f"Request failed with status code: {response.status_code}")
                return None
        
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None
        
    def get_events_map(self,map_name):
        map_center = [0, 0]
        my_map = folium.Map(location=map_center, zoom_start=12)
        res_codes = []
        res_dets = []
        for e_id in self.events_ids:
            details = self.get_event_details(e_id)
            if details is None:
                print('Null details')
                continue
            if details['results'] is None:
                print("EINAI NONE RE MLK!!!")
                continue
            res = details['results'][0]
            centroid = res['centroid'] #event centroid
            extent_coords = res['extent'].split("((")[1].split("))")[0].split(",") # the extended event area
            lat=centroid.split(" ")[1].split("(")[1]
            long = centroid.split(" ")[2].split(")")[0]
            
            
            
            stats_str=""
            extent_polygon = self.extent_coords2polygon(extent_coords)
            if res['stats']  is not None:
                
                stats_str = '<br>'.join(f"<b>{key}:</b> {value}" for key, value in res['stats'].items())
            polyline_text = "<b>"+res['code']+" - "+res['name']+ "</b><br><br>"+res['reason']+"<br><br>"+stats_str
            # polyline_text = f"<b>{res['code']} - {res['name']}</b><br>{res['reason']}<br>{stats_str}"
            poly_popup = folium.Popup(polyline_text , max_width=200)
            polygon = folium.Polygon(locations=extent_polygon, color='red', weight=2,dash_array='5, 5', fill=False,popup=poly_popup )
            # Concatenate the values into a string
            
    
            res_codes.append(res['code']+' - '+res['name'])
            res_dets.append(polyline_text)
            # print(res['code'], polyline_text)
            polygon.add_to(my_map)
            AOIS = res['aois']
            colors = [ 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']
            i = 0
            for aoi in AOIS:
               
                 extent_coords = aoi['extent'].split("((")[1].split("))")[0].split(",") # the extended event area
                 aoi_polygon = self.extent_coords2polygon(extent_coords)
                 # print(colors[i])
    
                 polygon = folium.Polygon(locations=aoi_polygon, color=colors[i], fill=True, fill_opacity=0.3).add_to(my_map)
                 tooltip_text = aoi['activationCode'] +"-"+aoi['name']
                 folium.Popup(tooltip_text).add_to(polygon)
                 if i == len(colors):
                     i=0
                 else:
                     i=(i+1) #% len(colors)
            # Save the map to an HTML file
        
        # my_map.save(map_name +".html")
        return my_map,res_codes,res_dets

    def extent_coords2polygon(self,extent_coords):

        # Coordinates for the polygon
        extent_polygon = []
        for coord in extent_coords:
            # print (coord)
            long = float(coord.strip().split(" ")[0])
            lat = float(coord.strip().split(" ")[1])
            extent_polygon.append((lat,long))
        return    extent_polygon         
        
        
