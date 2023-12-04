from sentinelhub import SHConfig, BBox, DataCollection, SentinelHubRequest, MimeType
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from copernicusNotify import copernicusNotify as CN
import os, io, tarfile, json, requests
from datetime import datetime, timedelta
from datetime import datetime as dt, timedelta
from shutil import move
import numpy as np
import datetime
import os
import matplotlib.pyplot as plt
import numpy as np
import shutil
from datetime import date
from datetime import datetime
import folium 
import pytz
from sentinelhub import (
    CRS,
    BBox,
    DataCollection,
    DownloadRequest,
    MimeType,
    MosaickingOrder,
    SentinelHubDownloadClient,
    SentinelHubRequest,
    bbox_to_dimensions,
)
import numpy as np
import matplotlib.pyplot as plt
from sentinelhub import Geometry, CRS, DataCollection, MimeType, SentinelHubRequest
client_id = '871600a3-ff0c-46a8-a75b-1ab14dea33b6'
client_secret = 'thkImuEFyW2rfROnd5AprDzh4hkEshUiqX7MWLOs'


from PIL import Image




# Configure your API credentials and instance ID
config = SHConfig()
config.sh_client_id = client_id
config.sh_client_secret = client_secret

today = datetime.utcnow().replace(tzinfo=pytz.utc)
# cn = CN()
# events,feed = cn.get_all_notifications()
# e = events[0]

class sentinelAPI:
    
    def get_event_map(self,e):
        long = e['coords'][1]
        lat =  e['coords'][0]
        event_date = dt.strptime(e['published'], '%a, %d %b %Y %H:%M:%S %z')

        square_size = 0.1/4

        # Define a GeoJSON geometry
        long_lat = {
            "type": "Polygon",
            "coordinates": [
                [
          [long - square_size / 2, lat + square_size / 2] ,  # Top-left
            [long + square_size / 2, lat + square_size / 2, ],  # Top-right
            [ long + square_size / 2,lat - square_size / 2],  # Bottom-right
            [long - square_size / 2, lat - square_size / 2 ],  # Bottom-left
        
                ]
            ]
        }
        lat_long= {
            "type": "Polygon",
            "coordinates": [
                [
          [lat + square_size / 2, long - square_size / 2 ] ,  # Top-left
            [lat + square_size / 2 , long + square_size / 2  ],  # Top-right
            [ lat - square_size / 2, long + square_size / 2],  # Bottom-right
            [lat - square_size / 2 , long - square_size / 2  ],  # Bottom-left
        
                ]
            ]
        }
        
        
        
        polygon_coordinates = long_lat["coordinates"][0]
        map_center = [long,lat]
        mymap = folium.Map(location=map_center, zoom_start=12)
        folium.Polygon(locations=polygon_coordinates, color='blue', fill=True, fill_color='blue').add_to(mymap)
        
        # Add a pin marker at the specified latitude and longitude
        folium.Marker(location=[long, lat], popup=e['title']).add_to(mymap)
        
        # Save the map as an HTML file or display it in the Jupyter Notebook
         
        return mymap

    def get_event_images_before(self,e):
        long = e['coords'][1]
        lat =  e['coords'][0]
        event_date = dt.strptime(e['published'], '%a, %d %b %Y %H:%M:%S %z')

        date_before_start = event_date- timedelta(days=20)
        date_before_end = event_date - timedelta(days=1)
        time_interval_before = (date_before_start,date_before_end)

        square_size = 0.1/4

        # Define a GeoJSON geometry
        long_lat = {
            "type": "Polygon",
            "coordinates": [
                [
          [long - square_size / 2, lat + square_size / 2] ,  # Top-left
            [long + square_size / 2, lat + square_size / 2, ],  # Top-right
            [ long + square_size / 2,lat - square_size / 2],  # Bottom-right
            [long - square_size / 2, lat - square_size / 2 ],  # Bottom-left
        
                ]
            ]
        }
        lat_long= {
            "type": "Polygon",
            "coordinates": [
                [
          [lat + square_size / 2, long - square_size / 2 ] ,  # Top-left
            [lat + square_size / 2 , long + square_size / 2  ],  # Top-right
            [ lat - square_size / 2, long + square_size / 2],  # Bottom-right
            [lat - square_size / 2 , long - square_size / 2  ],  # Bottom-left
        
                ]
            ]
        }
        bbox_values = [long - square_size / 2, lat - square_size / 2, long + square_size / 2, lat + square_size / 2]
        bbox_str = "&BBOX=" + ",".join(map(str, bbox_values))
        bbox = "&BBOX=" + ",".join(map(str, bbox_values))
        
        
        
        # Convert the GeoJSON to a geometry object
        self.geometry = Geometry(lat_long, CRS('EPSG:4326'))
        
        data = self.get_sentinel_data(self,self.geometry,config,time_interval_before,"1212")
        im = Image.fromarray(data)
        im.save("C:\\Users\\roub\\Desktop\\images\\before.jpeg")
        return data
    def get_event_images_after(self,e):
        long = e['coords'][1]
        lat =  e['coords'][0]
        event_date = dt.strptime(e['published'], '%a, %d %b %Y %H:%M:%S %z')

        date_before_start = event_date- timedelta(days=20)
        date_before_end = event_date - timedelta(days=1)
        time_interval_before = (date_before_start,date_before_end)

        square_size = 0.1/4

        # Define a GeoJSON geometry
        long_lat = {
            "type": "Polygon",
            "coordinates": [
                [
          [long - square_size / 2, lat + square_size / 2] ,  # Top-left
            [long + square_size / 2, lat + square_size / 2, ],  # Top-right
            [ long + square_size / 2,lat - square_size / 2],  # Bottom-right
            [long - square_size / 2, lat - square_size / 2 ],  # Bottom-left
        
                ]
            ]
        }
        lat_long= {
            "type": "Polygon",
            "coordinates": [
                [
          [lat + square_size / 2, long - square_size / 2 ] ,  # Top-left
            [lat + square_size / 2 , long + square_size / 2  ],  # Top-right
            [ lat - square_size / 2, long + square_size / 2],  # Bottom-right
            [lat - square_size / 2 , long - square_size / 2  ],  # Bottom-left
        
                ]
            ]
        }
        

        # Convert the GeoJSON to a geometry object
        self.geometry = Geometry(lat_long, CRS('EPSG:4326'))
        
        data = self.get_data_after(self,e,self.geometry,config)
        print(" days after ", np.sum(data))  
        im = Image.fromarray(data)
        im.save("C:\\Users\\roub\\Desktop\\images\\after.jpeg")
        return data
    
    

    def get_data_after(self,e,geometry,config):
        i=1
        event_date = dt.strptime(e['published'], '%a, %d %b %Y %H:%M:%S %z')
        date_after_end =  event_date+ timedelta(days=1)
        time_interval_after = (event_date,date_after_end)
        data = self.get_sentinel_data(self,self.geometry,config,time_interval_after,str(i))
        filename = "after"+str(i)
        while np.sum(data) == 0 and date_after_end <= today :
            date_after_end =  date_after_end+ timedelta(days=1)
            time_interval_after = (event_date,date_after_end)
            
            data = self.get_sentinel_data(self,self.geometry,config,time_interval_after,filename)
            i=i+1
            filename = "after"+str(i)
        print(str(i)+" days after ", np.sum(data))            
        return data
        
        
    def get_sentinel_data(self,geometry,config,time_interval,filename):     
        print(filename)
               ############################## AFTER 
        request = SentinelHubRequest(
            data_folder='C:\\Users\\roub\\Desktop\\folder_sentinel\\folder\\sentinel_images\\',
            evalscript="""
        //VERSION=3
        
        let minVal = 0.0;
        let maxVal = 0.4;
        
        let viz = new HighlightCompressVisualizer(minVal, maxVal);
        
        function evaluatePixel(samples) {
            let val = [samples.B04, samples.B03, samples.B02];
            val = viz.processList(val);
            val.push(samples.dataMask);
            return val;
        }
        
        function setup() {
          return {
            input: [{
              bands: [
                "B02",
                "B03",
                "B04",
                "dataMask"
              ]
            }],
            output: {
              bands: 4
            }
          }
        }
        
        
            """,
            input_data=[
                SentinelHubRequest.input_data(
                    data_collection=DataCollection.SENTINEL2_L1C,
                                 mosaicking_order=MosaickingOrder.LEAST_CC,
                    time_interval=time_interval,
        
                ),
            ],
 responses=[
        SentinelHubRequest.output_response("default", MimeType.JPG),
    ],
            geometry=self.geometry,
            size=(512, 512),
            config=config
        )
        filename='C:\\Users\\roub\\Desktop\\folder_sentinel\\folder\\sentinel_images\\'+filename
        # Define the file path and name for saving the data
        # file_path = "C:\\Users\\roub\\Desktop\\folder_sentinel\\folder"+e['id']+date_before.strftime('%Y-%m-%d')+".jpg"
        request.save_data()

        data = request.get_data()[0]
        # slice_data=data[:,:,0]
        # plt.imshow(slice_data, cmap='viridis')  # You can choose a different colormap
        # plt.colorbar()  # Add a colorbar to the plot
        # plt.title('Slice of ndarray as Image')
        # plt.show()
        # print((request.data_folder))
        # for folder, _, filenames in os.walk(request.data_folder):
        #         for fname in filenames:
        #             print(os.path.join(folder, fname))
        # Assuming the data_folder contains only folders
        all_folders = [folder for folder in os.listdir(request.data_folder) if os.path.isdir(os.path.join(request.data_folder, folder))]
        if np.sum(data) ==0:
            # Find the most recent folder based on creation time
            most_recent_folder = max(all_folders, key=lambda folder: os.path.getctime(os.path.join(request.data_folder, folder)))
        
            # Construct the full path of the most recent folder
            full_path_most_recent_folder = os.path.join(request.data_folder, most_recent_folder)
        
            # Delete the most recent folder
            shutil.rmtree(full_path_most_recent_folder)
        return data
    
