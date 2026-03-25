import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# ----------SIMPLE REQUEST ACCEPT HEADER----------

URL = "http://web-04.challs.olicyber.it/users"

headers = {"Accept": "application/xml"}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, "xml")

flag = soup.find("user", comment=True)["comment"]

print(f"[FLAG]: {flag}") 

