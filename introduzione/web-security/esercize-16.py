import requests
from bs4 import BeautifulSoup

# ----------EXTRACT FLAG FROM HREF PAGES----------

URL = "http://web-16.challs.olicyber.it"

visited = set()
to_visited = [URL]

flag = ""

for i in to_visited:    
    current = to_visited.pop()
    print(f"[VISITED]: {current}")

    if not current in visited:
        response = requests.get(current)
        soup = BeautifulSoup(response.text, "html.parser")

        if soup.h1 and "flag" in soup.h1.text:        
            flag = soup.h1.text
            break

        href_tags = soup.find_all("a")

        visited.add(current)
        for href in href_tags:        
            to_visited.append(f'{URL}/{href["href"]}')

print(f"[FLAG]: {flag}")