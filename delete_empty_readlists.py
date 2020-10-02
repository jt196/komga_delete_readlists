import requests
import json
import getpass
import sys

from requests.auth import HTTPBasicAuth

print('Please enter the base URL of your Komga installation (e.g. http://komga.mysite.com):')
url = input()
print('Please enter your Komga username:')
user = input()
password = getpass.getpass('Please enter your Komga password:')

r = requests.get(f'{url}/api/v1/readlists?unpaged=true', auth=HTTPBasicAuth(f'{user}', f'{password}'))

readlists_json = r.json()

def empty_list_count():

    empty_lists = 0

    for item in readlists_json['content']:
        id = item['id']
        name = item['name']
        if len(item['bookIds']) == 0:
            print("List '" + item['name'] + "' is empty.")
            empty_lists += 1
            readlist_url = (f'{url}/api/v1/readlists/{id}')
            print(readlist_url)

    if empty_lists == 0:
        print('You have no empty lists, aborting program')
        sys.exit()
    elif empty_lists == 1:
        print('You have 1 empty list')
    else:
        print(f'You have a total of {empty_lists} empty list(s)')

empty_list_count()

answer = input("Do you wish to continue pruning your readlists (y/n): ") 
if answer == "y": 
    print("Deleting empty readlists...")
    for item in readlists_json['content']:
        id = item['id']
        name = item['name']
        if len(item['bookIds']) == 0:
            readlist_url = (f'{url}/api/v1/readlists/{id}')
            x = requests.delete(readlist_url, auth = (user, password))
            # print(x.status_code)
            print(f"Readlist {name} deleted")
elif answer == "n": 
    print("OK, exiting program")
    sys.exit()
else: 
    print("Please enter yes or no.") 

empty_list_count()