import requests
from bs4 import BeautifulSoup

# ----------SIMPLE REQUEST POST METHOD----------

URL = "http://web-08.challs.olicyber.it/login"

data = {"username": "admin", "password": "admin"}

response = requests.post(URL, data=data)

soup = BeautifulSoup(response.text, "html.parser")

flag = soup.prettify().strip()

print(f"[FLAG]: {flag}")
