# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:18:15 2023

@author: roub
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://rapidmapping.emergency.copernicus.eu/EMSR709/download"

# Set up the Selenium WebDriver using Firefox
driver = webdriver.Firefox()

try:
    # Open the webpage
    driver.get(url)

    # Wait for the button to be present in the DOM
    download_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Download AOIs')]"))
    )

    # Wait for the button to be clickable
    download_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Download AOIs')]"))
    )

    # Click the button
    download_button.click()

    # Wait for the download to complete
    time.sleep(5)

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser window
    driver.quit()
