import requests
from bs4 import BeautifulSoup

url = 'https://rapidmapping.emergency.copernicus.eu/EMSR709/aem'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract information based on HTML structure
    # Example: Print the title of the webpage
    title = soup.title.text.strip()
    print(f'Title: {title}')

    # You can inspect the HTML structure of the page using developer tools
    # in your web browser to identify the elements you want to extract.

    # Example: Extract and print text from a specific element with a particular class
    # element_text = soup.find('div', class_='your-class-name').text.strip()
    # print(f'Element Text: {element_text}')

else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
