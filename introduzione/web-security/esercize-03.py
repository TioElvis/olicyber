import requests
from bs4 import BeautifulSoup

# ----------REQUEST MANUAL HEADER----------

URL = "http://web-03.challs.olicyber.it/flag"

headers = {"X-Password": "admin"}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

flag = soup.prettify().strip()

print(f"[FLAG]: {flag}")
