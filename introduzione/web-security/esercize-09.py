import requests
from bs4 import BeautifulSoup

# ----------REQUEST POST JSON----------

URL = "http://web-09.challs.olicyber.it/login"

json = {"username": "admin", "password": "admin"}

response = requests.post(URL, json=json)

flag = response.json()["token"]

print(f"[FLAG]: {flag}")
