import requests
from bs4 import BeautifulSoup

# Define the URL of the page to scrape
url = "https://poc-d8.lolandese.site/search-activations1"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the tbody element
    tbody = soup.find("table").find("tbody")
    all_events = []
    if tbody:
        # Find all rows (tr) within the tbody
        rows = tbody.find_all("tr")

        # Loop through the rows and print their content
        for row in rows:
            # Find all cells (td) within the row
            cells = row.find_all("td")
            per_event = []
            # Extract and print the text from each cell
            for cell in cells:
                print(cell.get_text(strip=True))
                per_event.append(cell.get_text(strip=True))
            all_events.append(per_event)                
    else:
        print("Tbody not found on the page.")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

for e in all_events:
    code = e[1]
    description = e[2]
    date = e[3]
    event = e[4]
    loc = e[5]
    
base = "https://emergency.copernicus.eu/mapping/list-of-components/"
 
link = base+code
# Send an HTTP GET request to the URL
response = requests.get(url)
