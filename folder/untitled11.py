from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://rapidmapping.emergency.copernicus.eu/EMSR709/download'

# Set up the Selenium driver (replace 'path/to/chromedriver' with the actual path)
driver = webdriver.Firefox()

try:
    # Open the webpage
    driver.get(url)

    # Wait for the "Download AOIs" button to be clickable
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Download AOIs']"))
    )

    # Click the button
    button.click()

finally:
    # Close the browser window
    driver.quit()


import requests

url = 'https://rapidmapping.emergency.copernicus.eu/EMSR709/download'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the content of the response
    print(response.text)
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
import requests
from bs4 import BeautifulSoup

url = 'https://rapidmapping.emergency.copernicus.eu/EMSR709/download'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract and print each tag on a new line
    for tag in soup.find_all():
        print(tag)

else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
