import requests
import json

url = "https://sandboxapicdc.cisco.com:443/api/aaaLogin.json"

payload = {
    "aaaUser": {
        "attributes": {
            "name": "admin",
            "pwd": "ciscopsdt"
        }
    }
}

headers = {
    'Content-Type': "application/json"
}

response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False).json()

token = response['imdata'][0]['aaaLogin']['attributes']['token']
cookie = {}
cookie['APIC-cookie'] = token

url = "https://sandboxapicdc.cisco.com:443/api/node/mo/uni/tu-Heroes/ap-Save_The_Planet.json"

headers = {
    'cache-control': "no-cache"
}

get_response = requests.get(
    url, headers=headers, cookies=cookie, verify=False).json()

print(json.dumps(get_response, indent=2, sort_keys=True))
