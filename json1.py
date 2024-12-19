
import json, requests
from http.client import responses

api_url = "https://reqres.in/api/users?page=1"
api_url2 = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_url)
response2 = requests.get(api_url2)
data = response.json()
data2 = response2.json()

print(data['data'][0]['first_name'])
counter = 0
for i in data2:
    if i['userId'] == 1:
        counter += 1
        print(counter)
