import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "turnlight", {"status": 0})
print(response.json())
input()
response = requests.put(BASE + "turnlight", {"status": 1})
print(response.json())
input()
response = requests.put(BASE + "turnlight", {"status": 1})
print(response.json())
input()
response = requests.get(BASE + "turnlight")
print(response.json())
