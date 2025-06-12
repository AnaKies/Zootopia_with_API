import requests


API_KEY = "rYuS4K7c0KnB9Hquc0wn1A==L07FObBxfsOduakm"

def search_for_animal_in_api(animal_name):
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        result = response.json()
        return result
    else:
        print("Error:", response.status_code, response.text)
        return None
