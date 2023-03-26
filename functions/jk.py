from decouple import config
import requests

url = config('API_URL')

def make_req():
    response = requests.get(url)
    print(f'Response = {response.json()}')
    return 'Hello from functions!'