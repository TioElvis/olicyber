import requests

# ----------REQUEST HEAD METHOD----------

URL = "http://web-07.challs.olicyber.it/"

response = requests.head(URL)

flag = response.headers["X-Flag"]

print(f"[FLAG]: {flag}")
