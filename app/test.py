import requests


BASE = "HTTP://127.0.0.1:5000/"

input()
response = requests.get(BASE + "video/0")
print(response.json())

input()
response = requests.patch(
    BASE + "video/0", json={"views": "99", "name": 'Sam'})

input()
response = requests.get(BASE + "video/0")
print(response.json())
