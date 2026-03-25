import requests
from bs4 import BeautifulSoup

# ----------REQUEST OPTIONS METHOD----------

URL = "http://web-10.challs.olicyber.it/"

# View the code give from the challenge I see a condition that if I send a request different of GET/OPTIONS/HEAD the server response me with a header X-Flag
response = requests.post(URL)

flag = response.headers["X-Flag"]

print(f"[FLAG]: {flag}")
