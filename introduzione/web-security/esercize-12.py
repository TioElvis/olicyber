import requests
from bs4 import BeautifulSoup

# ----------EXTRACT FLAG FROM HTML TAG----------

URL = "http://web-12.challs.olicyber.it/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

flag = soup.pre.string.strip()

print(f"[FLAG]: {flag}")
