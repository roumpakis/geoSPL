# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:55:51 2023

@author: roub
"""
import requests
import folium
from copernicusNotify import copernicusNotify as CN

class mapHandler:
  def __init__(self, long,lat,zoom,cn,add_all=False):
    self.cn = cn
    self.events,self.feed = self.cn.get_all_notifications()
    self.m = folium.Map(location=[long, lat], zoom_start=zoom,max_bounds = True,zoom_control=False)
    
    
    # path = "C:\\Users\\roub\\Desktop\\folder_sentinel\\folder\\output_image.png"
    # self.add_image_layer(path)
    if add_all:
        self.addFeedMap(self.events)
    
    # Reset or clear the markers
    # Remove all markers
    
    # Add a base tile layer from OpenStreetMap to the Folium map 
 
      
  def addLayer(self,layerName):
        folium.TileLayer(layerName).add_to(self.m)
        
  def addPinPopup(self,long,lat,msg):
            folium.Marker([lat,long], popup="<b>Marker Popup</b><br>P"+msg).add_to(self.m)

  def addPinEvent(self,long,lat,msg,event=""):
      print(event)
      if event == "fire":
          img = 'C:\\Users\\roub\\Desktop\\folder\\mapicons\\fire.png'
      elif event == "flood":
           img = 'C:\\Users\\roub\\Desktop\\folder\\mapicons\\flood.png'
      else:
         print('den edwses')
         self.addPinEvent(long, lat, msg)
         img=""
      # Define the icon for your custom pin (replace 'icon.png' with your image file)
      custom_icon = folium.CustomIcon(icon_image=img, icon_size=(50, 50))
      marker = folium.Marker(location=[lat, long],popup='Custom Pin Popup Text',  icon=custom_icon)
      
      marker.add_to(self.m)
  def create_event_map(self,e):
                              # Create a folium map centered at the specified coordinates
                    latitude = e['coords'][0]
                    longitude = e['coords'][1]
                    
                    # Add a marker to the map
                    # folium.Marker(location=[longitude,latitude], popup=e['title']).add_to(my_map)
                    if "fire" in e['title'] or "Fire" in e['title'] :
                      img = 'C:\\Users\\roub\\Desktop\\folder\\mapicons\\fire.png'
                    elif  "flood" in e['title'] or "Flood" in e['title']:
                       img = 'C:\\Users\\roub\\Desktop\\folder\\mapicons\\flood.png'
                    elif  "earthquake" in e['title'] or "Earthquake" in e['title']:
                       img = 'C:\\Users\\roub\\Desktop\\folder\\mapicons\\earthquake.png'     
                    elif  "industrial" in e['title'] or "Industrial" in e['title']:
                       img = 'C:\\Users\\roub\\Desktop\\folder\\mapicons\\industrial.png'
                    elif  "landslide" in e['title'] or "Landslide" in e['title']:
                       img = 'C:\\Users\\roub\\Desktop\\folder\\mapicons\\landslide.png'       
                    else:
                     print('den edwses')
                     folium.Marker([longitude,latitude], popup=e['title']).add_to(self.m)
                     img="false"
                    if "false" not in img:
                      # Define the icon for your custom pin (replace 'icon.png' with your image file)
                        custom_icon = folium.CustomIcon(icon_image=img, icon_size=(50, 50))
                        marker = folium.Marker(location=[longitude, latitude],popup=e['title'],  icon=custom_icon)
                      
                        marker.add_to(self.m)
                        
  def addFeedMap(self,events):
                for e in events:
            
                    # Create a folium map centered at the specified coordinates
                    latitude = e['coords'][0]
                    longitude = e['coords'][1]
                    
                    # Add a marker to the map
                    # folium.Marker(location=[longitude,latitude], popup=e['title']).add_to(my_map)
                    if "fire" in e['title'] or "Fire" in e['title'] :
                      img = 'C:\\Users\\roub\\Desktop\\folder\\mapicons\\fire.png'
                    elif  "flood" in e['title'] or "Flood" in e['title']:
                       img = 'C:\\Users\\roub\\Desktop\\folder\\mapicons\\flood.png'
                    elif  "earthquake" in e['title'] or "Earthquake" in e['title']:
                       img = 'C:\\Users\\roub\\Desktop\\folder\\mapicons\\earthquake.png'     
                    elif  "industrial" in e['title'] or "Industrial" in e['title']:
                       img = 'C:\\Users\\roub\\Desktop\\folder\\mapicons\\industrial.png'
                    elif  "landslide" in e['title'] or "Landslide" in e['title']:
                       img = 'C:\\Users\\roub\\Desktop\\folder\\mapicons\\landslide.png'       
                    else:
                     print('den edwses')
                     folium.Marker([longitude,latitude], popup=e['title']).add_to(self.m)
                     img="false"
                    if "false" not in img:
                      # Define the icon for your custom pin (replace 'icon.png' with your image file)
                        custom_icon = folium.CustomIcon(icon_image=img, icon_size=(50, 50))
                        marker = folium.Marker(location=[longitude, latitude],popup=e['title'],  icon=custom_icon)
                      
                        marker.add_to(self.m)
                
      #   # Define a GeoJSON feature collection with a polygon
      # geojson_data = {
      #       "type": "FeatureCollection",
      #       "features": [
      #           {
      #               "type": "Feature",
      #               "properties": {},
      #               "geometry": {
      #                   "type": "Polygon",
      #                   "coordinates": [
      #              [
      #                   [-0.1318, 51.5032],
      #                   [-0.1288, 51.5046],
      #                   [-0.1268, 51.5026],
      #                   [-0.1318, 51.5012],
      #                   [-0.1378, 51.5012],
      #                   [-0.1348, 51.5026],
      #                   [-0.1318, 51.5032]
      #               ]
      #                   ]
      #               }
      #           }
      #       ]
      #   }
        
      #   # Add the GeoJSON data to the map
      # folium.GeoJson(geojson_data).add_to(self.m)
      
      
      
  def add_image_layer(self, path):
         # Add the image overlay to the map
         print('call add image Layer!')
         response =self.make_req()
         if response.status_code == 200:
             
            img_overlay = folium.raster_layers.ImageOverlay(
                # image=response.content,
                image="C:\\Users\\roub\\Desktop\\gwis.png",
                bounds=[[23.0797, -44.2969], [73.7758, 76.9922]],
                opacity=0.5,
                name='WMS Image Overlay'
            ).add_to(self.m)
         else:
             print("To request htane malakia")

  def make_req(self):
    print('Make req!')
    req = "https://ows.globalfloods.eu/glofas-ows/ows.py?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap"
    add_BBOX = "&BBOX=23.07970000000000255,-44.29690000000000083,73.77580000000000382,76.99219999999999686 "
    add_CRS = "&CRS=EPSG:4326"
    add_WH = "&WIDTH=1439&HEIGHT= 602"
    add_TIME= ""#"&TIME=2023-01-01-00"
    add_LAYERS = "&LAYERS=MajorRiverBasins"
    add_STYLES = "&STYLES="
    add_FORMAT = "&FORMAT=image/png"
    add_DPI ="&DPI=96"
    add_MAP_RESOLUTION = "&MAP_RESOLUTION=96"
    add_FORMAT_OPTIONS = "&FORMAT_OPTIONS=dpi:96"
    add_TRANSPARENT = "&TRANSPARENT=TRUE"
    
    req = req+add_BBOX+add_CRS+add_WH+add_TIME+add_LAYERS+add_STYLES+add_FORMAT+add_FORMAT+add_MAP_RESOLUTION+add_FORMAT_OPTIONS+add_TRANSPARENT
    # Make the request
    response = requests.get(req)
    print(response.status_code)
    return response
      

    