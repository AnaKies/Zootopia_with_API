import os

import requests
from dotenv import load_dotenv

HTTP_CODE_OK = 200

# load variables (API-key) from the environment into the script
load_dotenv()


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
    },
    """
    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    api_key = os.getenv('API_KEY')
    response = requests.get(api_url, headers={'X-Api-Key': api_key}, timeout=10)
    if response.status_code == HTTP_CODE_OK:
        result = response.json()
        return result
    print("Error:", response.status_code, response.text)
    return None
