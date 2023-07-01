import requests
import json
import base64

# Define the API endpoint URL
url = 'http://127.0.0.1:5000/generate-image'

# Set up the request payload
payload = {
    'prompt': 'a donut',
}

# Send the POST request to generate the image
response = requests.post(url, json=payload)

# Check the response status code
if response.status_code == 200:
    # Get the generated images from the response
    data = response.json()
    print(data)
else:
    print('Request failed with status code')
