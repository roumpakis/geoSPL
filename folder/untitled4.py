url = "https://rapidmapping.emergency.copernicus.eu/EMSR708/aem"


from owslib.wms import WebMapService

# GloFAS WMS URL
glofas_wms_url = 'https://ows.globalfloods.eu/glofas-ows/ows.py?'

# Connect to the WMS service
wms = WebMapService(glofas_wms_url, version='1.3.0')

# Print available layers
print("Available Layers:")
for layer in list(wms.contents):
    print(f"- {layer}")

# Print available styles for the first layer
first_layer = list(wms.contents.keys())[0]
styles = wms[first_layer].styles
print(f"\nAvailable Styles for Layer '{first_layer}':")
for style in styles:
    print(f"- {style}")

import folium
from owslib.wms import WebMapService

# GloFAS WMS URL
glofas_wms_url = 'https://ows.globalfloods.eu/glofas-ows/ows.py?'

# Connect to the WMS service
wms = WebMapService(glofas_wms_url, version='1.3.0')

# Create a Folium map and set its initial view
m = folium.Map(location=[51.505, -0.09], zoom_start=5)

# Add EFAS WMS layer to the map
efas_layer = folium.raster_layers.WmsTileLayer(
    url=glofas_wms_url,
    name='GloFAS Forecast Layer',
    format='image/png',
    layers='Flood Risk',
    attr='GloFAS - Global Flood Awareness System',
    transparent=True,
    overlay=True,
)

# Add another WMS layer (example: OpenStreetMap)
osm_layer = folium.raster_layers.WmsTileLayer(
    url='http://ows.mundialis.de/services/service?',
    name='OpenStreetMap',
    format='image/png',
    layers='OSM-WMS',
    transparent=True,
    overlay=True,
)

# Add layer control to the map
folium.LayerControl().add_to(m)

# Add the WMS layers to the map
efas_layer.add_to(m)
osm_layer.add_to(m)

# Save the map to an HTML file or display it
m.save('multilayer_map.html')
