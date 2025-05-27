import requests

BASE_URL = 'http://127.0.0.1:3000/'

response = requests.post(BASE_URL + 'items/4', json={'name':'item11', 'color':'ffff'})
print(response.json())

response = requests.delete(BASE_URL + 'items/1')
print(response.json())

response = requests.put(BASE_URL + 'items/2', json={'name':'Sam', 'color':'white'})
print(response.json())

response = requests.patch(BASE_URL + 'items/3', json={'name':'apricot'})
print(response.json())

response = requests.get(BASE_URL + 'items/1')
print(response.json())