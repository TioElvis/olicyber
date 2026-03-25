import requests
from bs4 import BeautifulSoup

# ----------SIMPLE REQUEST COOKIES----------

URL = "http://web-05.challs.olicyber.it/flag"

cookies = {"password": "admin"}

response = requests.get(URL, cookies=cookies)

soup = BeautifulSoup(response.text, "html.parser")

flag = soup.prettify().strip()

print(f"[FLAG]: {flag}")
