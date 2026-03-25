import requests
from bs4 import BeautifulSoup

# ----------EXTRACT FLAG FROM DIFFERENTS HTML SPAN TAGS----------

URL = "http://web-13.challs.olicyber.it/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

span_tags = soup.find_all("span", class_="red")
parser = "".join([span.get_text() for span in span_tags])

flag = "flag{" + parser + "}"
print(f"[FLAG]: {flag}")
