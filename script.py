import requests
import sys

r = requests.get('https://mark1.co.za')
print(r.status_code)
