import requests
from bs4 import BeautifulSoup

# ----------SIMPLE REQUEST----------

URL = "http://web-01.challs.olicyber.it/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

flag = soup.prettify().strip()

print(f"[FLAG]: {flag}")
