import requests

# API endpoint URL
url = "https://api.example.com/backend/dashboard-api/public-activations/"

# Parameters for the request (replace with actual values as needed)
params = {
    "code": "EMSR568",
}

try:
    # Make the GET request
    response = requests.get(url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Access the list of activations
        activations = data.get("results", [])

        # Print information about each activation
        for activation in activations:
            print(f"Activation Code: {activation.get('code')}")
            print(f"Name: {activation.get('name')}")
            print(f"Activator: {activation.get('activator')}")
            print(f"Activation Time: {activation.get('activationTime')}")
            print("-------------")

    else:
        print(f"Error: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
