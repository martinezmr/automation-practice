import xmltodict

stream = open('C:/Users/mmart/automation-practice/format-examples/xml_example.xml' ,'r')

#Parse the data into an ElementTree Object
xml = xmltodict.parse(stream.read())

for e in xml["People"]["Person"]:
    print(e)

