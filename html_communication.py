import requests

name = 'cheetah'
api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': 'rYuS4K7c0KnB9Hquc0wn1A==L07FObBxfsOduakm'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
