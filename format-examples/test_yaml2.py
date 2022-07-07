import yaml
from yaml import load, load_all

stream = open('C:/Users/mmart/automation-practice/format-examples/yamlaintmarkuplanguage.yaml', 'r')
documents = load_all(stream, Loader=yaml.FullLoader)

print(type(documents))

for doc in documents:
    print(type(doc))

    print(doc['people'])

    print(doc['people'][1]['LastName'])