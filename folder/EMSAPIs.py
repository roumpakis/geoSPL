# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:26:52 2023

@author: roub
"""
import requests

class EMSAPI():


    def GloFASAPI(self):#GloFASAPI Web Layers    
        GloFAS_layers_time = [
         "reportingPoints"   
        ]

        GloFAS_layers_without=["EGE_probRgt50",       #Probability [%] of exceeding 50 mm of accumulated precipitation over the first 10 days of the ECMWF ensemble forecast.  
                       "AccRainEGE",#Amount of accumulated precipitation (mm) over the the first 10 days of the forecast period as the mean of the ECMWF ensemble forecast.
        ]


        req = "https://ows.globalfloods.eu/glofas-ows/ows.py?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap"
        add_BBOX = "&BBOX=23.07970000000000255,-44.29690000000000083,73.77580000000000382,76.99219999999999686 "
        add_CRS = "&CRS=EPSG:4326"
        add_WH = "&WIDTH=1439&HEIGHT= 602"
        add_TIME="&TIME=2023-01-01-00"
        add_LAYERS = "&LAYERS=MajorRiverBasins"
        add_STYLES = "&STYLES="
        add_FORMAT = "&FORMAT=image/png"
        add_DPI ="&DPI=96"
        add_MAP_RESOLUTION = "&MAP_RESOLUTION=96"
        add_FORMAT_OPTIONS = "&FORMAT_OPTIONS=dpi:96"
        add_TRANSPARENT = "&TRANSPARENT=TRUE"
        
        req = req+add_BBOX+add_CRS+add_WH+add_TIME+add_LAYERS+add_STYLES+add_FORMAT+add_FORMAT+add_MAP_RESOLUTION+add_FORMAT_OPTIONS+add_TRANSPARENT
        
    def HumanSettlementAPI(self, bbox, time):  

        #Human Settlement Layer
        req = "https://ies-ows.jrc.ec.europa.eu/gwis?"
        layer = "LAYERS=ghsl"
        forma = "&FORMAT=image/png"
        transparent = "&TRANSPARENT=true"
        singletile = "&SINGLETILE=false"
        service = "&SERVICE=wms"
        version = "&VERSION=1.1.1"
        request = "&REQUEST=GetMap"
        style = "&STYLES="
        srs = "&SRS=EPSG:4326"
        bbox = "&BBOX=-18.0,27.0,42.0,72.0"
        wh = "&WIDTH=1600&HEIGHT=1200"
        time = "&TIME=2019-02-08"
        
        req = req+layer+forma+transparent+singletile+service+version+request+style+srs+bbox+wh+time
        return req
    
    
    
    def protectedAreaAPI(self):

        # Effis Emergency API
        req = "https://maps.effis.emergency.copernicus.eu/gwis?"
        service = "service=WMS"
        request = "&request=GetMap"
        layers = "&layers=wdpa.poly"
        styles = "&styles="
        forma = "&format=image%2Fpng"
        transparent = "&transparent=true"
        version = "&version=1.1.1"
        singletile = "&singletile=false"
        wh = "&width=2048&height=2048"
        srs = "&srs=EPSG%3A4326"
        bbox = "&bbox=-18.0,27.0,42.0,72.0"
    
        req = req + service + request + layers + styles + forma + transparent + version + singletile + wh + srs + bbox
        return req
    
    def corineLandcoverAPI(self):
        req = "https://maps.effis.emergency.copernicus.eu/gwis?"
        service = "service=WMS"
        request = "&request=GetMap"
        layers = "&layers=effis_clc_2020"
        styles = "&styles="
        forma = "&format=image%2Fpng"
        transparent = "&transparent=true"
        version = "&version=1.1.1"
        singletile = "&singletile=false"
        map_param = "&map=%2Fmnt%2Fefs%2Fmapfiles%2Feffis.clc.map"
        wh = "&width=2048&height=2048"
        srs = "&srs=EPSG%3A4326"
        bbox = "&bbox=-18.0,27.0,42.0,72.0"
    
        req = req + service + request + layers + styles + forma + transparent + version + singletile + map_param + wh + srs + bbox
        return req
                    # start_date =  "2023-11-13"
    def activeFiresAPI(self, start_date, end_date):
        # Effis Emergency Modis HS API
        req = "https://maps.effis.emergency.copernicus.eu/gwis?"
        layers = "LAYERS=modis.hs"
        forma = "&FORMAT=image/png"
        transparent = "&TRANSPARENT=true"
        singletile = "&SINGLETILE=false"
        service = "&SERVICE=wms"
        version = "&VERSION=1.1.1"
        request = "&REQUEST=GetMap"
        style = "&STYLES="
        srs = "&SRS=EPSG:4326"
        bbox = "&BBOX=-18.0,27.0,42.0,72.0"
        wh = "&WIDTH=1600&HEIGHT=1200"
        time = f"&TIME={start_date}/{end_date}"
    
        req = req + layers + forma + transparent + singletile + service + version + request + style + srs + bbox + wh + time
        return req
    


        # https://ies-ows.jrc.ec.europa.eu/effis?
        # LAYERS=ecmwf007.fwi
        # &FORMAT=image/png&
        # TRANSPARENT=true
        # &SINGLETILE=false
        # &SERVICE=wms
        # &VERSION=1.1.1
        # &REQUEST=GetMap
        # &STYLES=
        # &SRS=EPSG:4326
        # &BBOX=-18.0,27.0,42.0,72.0
        # &WIDTH=1600&HEIGHT=1200
        # &TIME=2021-02-08

    def burnedAreasAPI(self, start_date, end_date):
        # Effis Modis BA API
        req = "https://maps.effis.emergency.copernicus.eu/effis?"
        layers = "LAYERS=modis.ba"
        forma = "&FORMAT=image/png"
        transparent = "&TRANSPARENT=true"
        singletile = "&SINGLETILE=false"
        service = "&SERVICE=wms"
        version = "&VERSION=1.1.1"
        request = "&REQUEST=GetMap"
        style = "&STYLES="
        srs = "&SRS=EPSG:4326"
        bbox = "&BBOX=-18.0,27.0,42.0,72.0"
        wh = "&WIDTH=1600&HEIGHT=1200"
        time = f"&TIME={start_date}/{end_date}"
    
        req = req + layers + forma + transparent + singletile + service + version + request + style + srs + bbox + wh + time
        return req

    def EffisFuelMapAPI(self, start_date, end_date):
        # Effis Fuel Map API
        req = "https://ies-ows.jrc.ec.europa.eu/effis?"
        layers = "LAYERS=fuel_map"
        forma = "&FORMAT=image/png"
        transparent = "&TRANSPARENT=true"
        singletile = "&SINGLETILE=false"
        service = "&SERVICE=wms"
        version = "&VERSION=1.1.1"
        request = "&REQUEST=GetMap"
        style = "&STYLES="
        srs = "&SRS=EPSG:4326"
        bbox = "&BBOX=-18.0,27.0,42.0,72.0"
        wh = "&WIDTH=1600&HEIGHT=1200"
        time = f"&TIME={start_date}/{end_date}"
    
        req = req + layers + forma + transparent + singletile + service + version + request + style + srs + bbox + wh + time
        return req
    
  ####################### Forcasting methods ###########################      
    def fireWeatherIndexAPI(self, target_date):
        # Effis ECMWF007 FWI API
        req = "https://ies-ows.jrc.ec.europa.eu/effis?"
        layers = "LAYERS=ecmwf007.fwi"
        forma = "&FORMAT=image/png"
        transparent = "&TRANSPARENT=true"
        singletile = "&SINGLETILE=false"
        service = "&SERVICE=wms"
        version = "&VERSION=1.1.1"
        request = "&REQUEST=GetMap"
        style = "&STYLES="
        srs = "&SRS=EPSG:4326"
        bbox = "&BBOX=-18.0,27.0,42.0,72.0"
        wh = "&WIDTH=1600&HEIGHT=1200"
        time = f"&TIME={target_date}"
    
        req = req + layers + forma + transparent + singletile + service + version + request + style + srs + bbox + wh + time
        return req

    def initialSpreadIndexAPI(self, target_date):
        # Effis ECMWF007 ISI API
        req = "https://ies-ows.jrc.ec.europa.eu/effis?"
        layers = "LAYERS=ecmwf007.isi"
        forma = "&FORMAT=image/png"
        transparent = "&TRANSPARENT=true"
        singletile = "&SINGLETILE=false"
        service = "&SERVICE=wms"
        version = "&VERSION=1.1.1"
        request = "&REQUEST=GetMap"
        style = "&STYLES="
        srs = "&SRS=EPSG:4326"
        bbox = "&BBOX=-18.0,27.0,42.0,72.0"
        wh = "&WIDTH=1600&HEIGHT=1200"
        time = f"&TIME={target_date}"
    
        req = req + layers + forma + transparent + singletile + service + version + request + style + srs + bbox + wh + time
        return req


    def buildUpIndexAPI(self, target_date):
        # Effis ECMWF007 BUI API
        req = "https://ies-ows.jrc.ec.europa.eu/effis?"
        layers = "LAYERS=ecmwf007.bui"
        forma = "&FORMAT=image/png"
        transparent = "&TRANSPARENT=true"
        singletile = "&SINGLETILE=false"
        service = "&SERVICE=wms"
        version = "&VERSION=1.1.1"
        request = "&REQUEST=GetMap"
        style = "&STYLES="
        srs = "&SRS=EPSG:4326"
        bbox = "&BBOX=-18.0,27.0,42.0,72.0"
        wh = "&WIDTH=1600&HEIGHT=1200"
        time = f"&TIME={target_date}"
    
        req = req + layers + forma + transparent + singletile + service + version + request + style + srs + bbox + wh + time
        return req
    

    def  fineFuelMoistureCodeAPI (self, target_date):
        # Effis ECMWF007 FFMC API
        req = "https://ies-ows.jrc.ec.europa.eu/effis?"
        layers = "LAYERS=ecmwf007.ffmc"
        forma = "&FORMAT=image/png"
        transparent = "&TRANSPARENT=true"
        singletile = "&SINGLETILE=false"
        service = "&SERVICE=wms"
        version = "&VERSION=1.1.1"
        request = "&REQUEST=GetMap"
        style = "&STYLES="
        srs = "&SRS=EPSG:4326"
        bbox = "&BBOX=-18.0,27.0,42.0,72.0"
        wh = "&WIDTH=1600&HEIGHT=1200"
        time = f"&TIME={target_date}"
    
        req = req + layers + forma + transparent + singletile + service + version + request + style + srs + bbox + wh + time
        return req
# The Duff Moisture Code (DMC) is a numeric rating of the average moisture content of loosely compacted organic layers of moderate depth. This code gives an indication of fuel consumption in moderate duff layers and medium-size woody material. 
    def DuffMoistureCodeAPI(self, target_date):
        # Effis ECMWF007 DMC API
        req = "https://ies-ows.jrc.ec.europa.eu/effis?"
        layers = "LAYERS=ecmwf007.dmc"
        forma = "&FORMAT=image/png"
        transparent = "&TRANSPARENT=true"
        singletile = "&SINGLETILE=false"
        service = "&SERVICE=wms"
        version = "&VERSION=1.1.1"
        request = "&REQUEST=GetMap"
        style = "&STYLES="
        srs = "&SRS=EPSG:4326"
        bbox = "&BBOX=-18.0,27.0,42.0,72.0"
        wh = "&WIDTH=1600&HEIGHT=1200"
        time = f"&TIME={target_date}"
    
        req = req + layers + forma + transparent + singletile + service + version + request + style + srs + bbox + wh + time
        return req

    def DroughCodeAPI(self, target_date):
        # Effis ECMWF007 DC API
        req = "https://ies-ows.jrc.ec.europa.eu/effis?"
        layers = "LAYERS=ecmwf007.dc"
        forma = "&FORMAT=image/png"
        transparent = "&TRANSPARENT=true"
        singletile = "&SINGLETILE=false"
        service = "&SERVICE=wms"
        version = "&VERSION=1.1.1"
        request = "&REQUEST=GetMap"
        style = "&STYLES="
        srs = "&SRS=EPSG:4326"
        bbox = "&BBOX=-18.0,27.0,42.0,72.0"
        wh = "&WIDTH=1600&HEIGHT=1200"
        time = f"&TIME={target_date}"
    
        req = req + layers + forma + transparent + singletile + service + version + request + style + srs + bbox + wh + time
        return req


    def anomalyFWIAPI(self, target_date):
        # Effis ECMWF007 Anomaly API
        req = "https://ies-ows.jrc.ec.europa.eu/effis?"
        layers = "LAYERS=ecmwf007.anomaly"
        forma = "&FORMAT=image/png"
        transparent = "&TRANSPARENT=true"
        singletile = "&SINGLETILE=false"
        service = "&SERVICE=wms"
        version = "&VERSION=1.1.1"
        request = "&REQUEST=GetMap"
        style = "&STYLES="
        srs = "&SRS=EPSG:4326"
        bbox = "&BBOX=-18.0,27.0,42.0,72.0"
        wh = "&WIDTH=1600&HEIGHT=1200"
        time = f"&TIME={target_date}"
    
        req = req + layers + forma + transparent + singletile + service + version + request + style + srs + bbox + wh + time
        return req

    def rankingFWIAPI(self, target_date):
        # Effis ECMWF007 Ranking API
        req = "https://ies-ows.jrc.ec.europa.eu/effis?"
        layers = "LAYERS=ecmwf007.ranking"
        forma = "&FORMAT=image/png"
        transparent = "&TRANSPARENT=true"
        singletile = "&SINGLETILE=false"
        service = "&SERVICE=wms"
        version = "&VERSION=1.1.1"
        request = "&REQUEST=GetMap"
        style = "&STYLES="
        srs = "&SRS=EPSG:4326"
        bbox = "&BBOX=-18.0,27.0,42.0,72.0"
        wh = "&WIDTH=1600&HEIGHT=1200"
        time = f"&TIME={target_date}"
    
        req = req + layers + forma + transparent + singletile + service + version + request + style + srs + bbox + wh + time
        return req

        
    def callAPI(self,req):

        # Make the request
        response = requests.get(req)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save the image content to a file
            with open('output_image.png', 'wb') as file:
                file.write(response.content)
            print('Image saved successfully.')
        else:
            print(f"Error: {response.status_code}")
