
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

url = "https://rapidmapping.emergency.copernicus.eu/EMSR709/download"
download_folder = "C:\\Users\\roub\\Desktop\\AOIs"  # Change to the actual download folder path

# Set up the Selenium WebDriver using Firefox in headless mode
options = Options()
options.headless = True
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", download_folder)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/json")

driver = webdriver.Firefox(options=options)

try:
    # Open the webpage
    driver.get(url)

    # Click the button without waiting
    download_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Download AOIs')]")
    download_button.click()

    # Wait for the file to be downloaded
    file_path = os.path.join(download_folder, "example.json")
    WebDriverWait(driver, 60).until(
        lambda x: os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )

    print("File downloaded successfully!")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser window
    driver.quit()
