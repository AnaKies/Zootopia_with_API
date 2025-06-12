import requests
import os
from dotenv import load_dotenv

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
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    API_KEY = os.getenv('API_KEY')
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
      result = response.json()
      return result
    else:
      print("Error:", response.status_code, response.text)
      return None