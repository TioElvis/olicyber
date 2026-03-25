import requests
from bs4 import BeautifulSoup

# ----------SIMPLE REQUEST----------

URL = "http://web-15.challs.olicyber.it"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

flag = ""

link_tags = soup.find_all("link")
for i in link_tags:
    response = requests.get(f"{URL}/{i["href"]}")
    _soup = BeautifulSoup(response.text, "html.parser")

    _soup_pretty = _soup.prettify().strip()
    if "flag" in _soup_pretty:
        flag = _soup_pretty
        break

script_tags = soup.find_all("script")
for i in script_tags:
    response = requests.get(f"{URL}/{i["src"]}")
    _soup = BeautifulSoup(response.text, "html.parser")

    _soup_pretty = _soup.prettify().strip()
    if "flag" in _soup_pretty:
        # I preview the flag into a comment so I make this to show the flag in a better way
        flag = _soup_pretty.split(" ")[8].strip()
        break

print(f"[FLAG]: {flag}")
