import requests
import json

from requests.auth import HTTPBasicAuth

r = requests.get("https://<yoursite>/api/v1/readlists?unpaged=true", auth=HTTPBasicAuth("<user>", "<password>"))

readlists_json = r.json()

for item in readlists_json['content']:
    id = item['id']
    name = item['name']
    if len(item['bookIds']) == 0:
        readlist_url = (f'https://<yoursite>/api/v1/readlists/{id}')
        x = requests.delete(readlist_url, auth = ("<user>", "<password>"))
        print(x.status_code)
        print(f"Readlist {name} deleted")