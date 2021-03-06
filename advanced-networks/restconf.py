# GET - get data
# POST - writes data
# PUT - updates data
# PATCH - replaces data
# DELETE - deletes data

import requests
import json
from pprint import pprint

# set up connection parameters in a dictionary
router = {"ip": "ios-xe-mgmt.cisco.com", "port": "9443",
        "user": "root", "password": "D_Vay!_10&"}

# set REST API Headers
headers = {"Accept": "application/yang-data+json",
            "Content-Type": "application/yang-data+json"}

url = f"https://{router['ip']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"

response = requests.get(url, headers=headers, auth=(
    router['user'], router['password']), verify=False)

api_data = response.json()
print("/" * 50)
pprint(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["description"])
print("/" * 50)
if api_data["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] == 'if-state-up':
    print("Interface is up")