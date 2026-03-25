import requests
from bs4 import BeautifulSoup, Comment

# ----------EXTRACT FLAG FROM HTML COMMENT----------

URL = "http://web-14.challs.olicyber.it/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

comments = soup.find_all(string=lambda text: isinstance(text, Comment))

flag = ""
for c in comments:
    if "flag" in c:
        flag = c.split(" ")[4]
    c.extract()

print(f"[FLAG]: {flag}")
