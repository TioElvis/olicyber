import requests
from bs4 import BeautifulSoup

# ----------SIMPLE REQUEST COOKIES 2----------

URL = "http://web-06.challs.olicyber.it"

session = requests.Session()

# GET THE COOKIE FOR THE SESSION
response = session.get(f"{URL}/token")

# GET THE FLAG
response = session.get(f"{URL}/flag")

flag = response.text.strip()

print(f"[FLAG]: {flag}")
