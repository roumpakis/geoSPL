import feedparser
import requests
# Replace the URL with the actual RSS feed URL
"""copernicusNotify.

This module retrives the Copernicos activations notifications and the details for each event.

"""

import folium
import xml.etree.ElementTree as ET
class copernicusNotify():
    
    def add_geo_polygons(self,event_id): 
        """add_geo_polygons.
                    Retrives the Polygons coordinates from GeoJSON for the given event from Copernicus event feed.
           Parameters
           ----------
            event_id : string
                The id of Copernicus event 'EMSNxxx'
           Returns
           -------
            list
                A list of GeoJSON polygon coordinates if extists or None
        """
        
        
        geo_polygons = []
        url = "https://emergency.copernicus.eu/mapping/list-of-components/"+event_id+"/aemfeed"
        
        # Make a request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the feed using feedparser
            feed = feedparser.parse(response.content)
        
            # Check if the feed has entries
            if len(feed.entries) > 0:
                # Extract the georss:polygon from the first entry (assuming it's present)
                # print(feed.entries)
                for i in range(len(feed.entries)):
                    if 'coordinates' in feed.entries[i].where.keys():
                                
                                  georss_polygon = feed.entries[i].where['coordinates']
                                  geo_polygons.append(georss_polygon)      
                    else:
                        print("den htan ")
    
                if len(geo_polygons)>0:
                        # print(f"georss:polygon: {georss_polygon}")
                        return geo_polygons
                else:
                        # print("No georss:polygon found in the feed.")
                        return None
            else:
                # print("No entries found in the feed.")
                return None
        else:
            print(f"Failed to fetch the URL. Status code: {response.status_code}")  
            return None    
    def get_all_notifications(self):
        """get_all_notifications.
                    Retrives the Copernicus Emergency Activation and Recovery events feed. 
                    'http://emergency.copernicus.eu/mapping/activations-risk-and-recovery/feed'
           Parameters
           ----------

           Returns
           -------
                    events : list
                        List of Copernicus activation events 
                    feed : feedparser.util.FeedParserDict
                        The feed parser dictionary from 'http://emergency.copernicus.eu/mapping/activations-risk-and-recovery/feed'
        """
        # Replace the URL with the actual RSS feed URL
        rss_feed_url = 'http://emergency.copernicus.eu/mapping/activations-risk-and-recovery/feed'
        
        # Parse the RSS feed
        feed = feedparser.parse(rss_feed_url)
        
        # List to store event information
        events = [] #egw
        entries = feed.entries
        # Iterate through each entry in the feed
        # for entry in feed.entries:
        for entry in entries[:10]:
            # Dictionary to store information for each event
            event_info = {}
        
            # Extract information from the RSS entry
            event_info['title'] = entry.title
            event_info['link'] = entry.link
            event_info['published'] = entry.published
            event_info['coords'] = entry.where['coordinates']
            event_info['details'] = entry.summary
            event_info["id"] = entry.title.split('[')[1].split(']')[0]
            # print(event_info["id"] )
            # if "EMSR" in event_info["id"] :
            #     print("AAAAAAAAAA!@*%$&*!@$!%&@$&*$&&*$*!*&*$*!)!%@%!@")
            event_info['polygon'] = self.add_geo_polygons(event_info['id'])
            events.append(event_info)
        events = events[:10]    
        return events,feed
    
    
    def addPinPopup(self,long,lat,msg):
            folium.Marker([long,lat], popup=msg).add_to(self.m)
            
            
    def generate_feed_map(self,events,map_name):

        map_center = [0, 0]
        my_map = folium.Map(location=map_center, zoom_start=12)
        
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
             folium.Marker([longitude,latitude], popup=e['title']).add_to(my_map)
             img="false"
            if "false" not in img:
              # Define the icon for your custom pin (replace 'icon.png' with your image file)
                custom_icon = folium.CustomIcon(icon_image=img, icon_size=(50, 50))
                marker = folium.Marker(location=[longitude, latitude],popup=e['title'],  icon=custom_icon)
              
                marker.add_to(my_map)

        # Save the map as an HTML file
        my_map.save(map_name+'.html')
        return my_map
        
        
        
