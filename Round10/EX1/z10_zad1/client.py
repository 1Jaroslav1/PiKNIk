import requests
import requests

url = 'http://127.0.0.1:8000/'

code = requests.post(url, data='Hackaton')
print(f'POST code: {code.status_code}')

data = requests.get(url)
print(f'Response: {data.text}')