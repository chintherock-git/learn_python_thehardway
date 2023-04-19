import requests

r = requests.get("https://pypi.org")
print(r.statuscode())
