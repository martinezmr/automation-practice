import json

stream = open('C:/Users/mmart/automation-practice/format-examples/json-example.json')

jsonobj = json.load(stream)

print(type(jsonobj['People']))