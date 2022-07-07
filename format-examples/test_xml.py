import xml.etree.ElementTree as ET

stream = open('C:/Users/mmart/automation-practice/format-examples/xml_example.xml' ,'r')

#Parse the data into an ElementTree Object
xml = ET.parse(stream)

#get the 'root' element object from the ElementTree
root = xml.getroot()

#Iterate through each child of the root Element
for e in root:
    #Print the stringified version of the element
    print(ET.tostring(e))
    print("")

    #Print the 'Id' attribute of the element object
    print(e.get("Id"))

