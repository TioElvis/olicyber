import requests

# ----------CSRF REQUEST----------

URL = "http://web-11.challs.olicyber.it"

session = requests.Session()
json = { "username": "admin", "password": "admin" }

flag = ""

for i in range(0, 4):
    # GET THE CSRF TOKEN
    response = session.post(f"{URL}/login", json=json)
    CSRF = response.json()["csrf"]

    params = { "index": i, "csrf": CSRF }
    response = session.get(f"{URL}/flag_piece", params=params)

    data = response.json()
    if "flag_piece" in data:
        flag_piece = data["flag_piece"]
        flag += flag_piece
        print(f"[FLAG PIECE {i + 1}]: {flag_piece}")

print(f"[FLAG]: {flag}")
