# fetch_schemes.py

import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv()

# Set base API details
BASE_URL = f"https://{os.getenv('DOMAIN')}.atlassian.net/rest/api/3"
EMAIL = os.getenv('EMAIL')
API_TOKEN = os.getenv('API_TOKEN')
auth = HTTPBasicAuth(EMAIL, API_TOKEN)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Fetch scheme IDs with error handling
def fetch_scheme_ids(endpoint, key):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url, headers=headers, auth=auth)
    if response.status_code == 200:
        data = response.json()
        if key in data and isinstance(data[key], list) and len(data[key]) > 0:
            return data[key][0]["id"]  # Return the first ID found
        else:
            print(f"Warning: No valid {key} found in the response.")
            return None
    else:
        print(f"Failed to fetch {endpoint}. Status Code: {response.status_code}")
        print(response.text)
        return None

# Fetch a list of users (for selecting the project lead)
def fetch_users():
    url = f"{BASE_URL}/users/search"
    response = requests.get(url, headers=headers, auth=auth)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch users. Status Code: {response.status_code}")
        print(response.text)
        return []
