import requests
from bs4 import BeautifulSoup

# ----------SIMPLE REQUEST WITH QUERY----------

URL = "http://web-02.challs.olicyber.it/server-records"

params = { "id": "flag" }

response = requests.get(URL, params)

soup = BeautifulSoup(response.text, "html.parser")

flag = soup.prettify().strip()

print(f"[FLAG]: {flag}")
