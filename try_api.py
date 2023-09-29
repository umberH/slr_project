import requests

api_url = 'http://www.bbcurdu.com/'

response = requests.get(api_url)


#response.json()
print(response.status_code)
print(response.headers["Content-Type"])
print(response.text)

print(response.cookies)

print(response.encoding)

print(response.url)

print(response.history)

print(response.is_redirect)


api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
response.json()

print(response.status_code)


todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
response.json()