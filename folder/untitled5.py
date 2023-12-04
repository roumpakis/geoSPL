import requests
import xml.etree.ElementTree as ET

# Your XML data
xml_data = '''
<Layer queryable="1" opaque="0" cascaded="0">
    <Name>UpstreamArea</Name>
    <!-- Other elements -->
    <MetadataURL type="TC211">
        <Format>text/xml</Format>
        <OnlineResource xlink:type="simple" xlink:href="https://ows.globalfloods.eu/glofas-ows/ows.py?request=GetMetadata&layer=UpstreamArea"/>
    </MetadataURL>
    <!-- Other elements -->
</Layer>
'''

# Parse the XML
root = ET.fromstring(xml_data)

# Extract the metadata URL
metadata_url = root.find('.//MetadataURL/OnlineResource').get('{http://www.w3.org/1999/xlink}href')

# Make an API call to the metadata URL
response = requests.get(metadata_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content (assuming it's XML)
    print(response.text)
else:
    print(f"Error: {response.status_code}")

