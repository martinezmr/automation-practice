import csv

# f = open("C:/Users/mmart/automation-practice/dnac-scripts/import_template.csv", "r")
# print(f.read())

samplefile = open('C:/Users/mmart/automation-practice/dnac-scripts/import_template.csv')
samplereader = csv.reader(samplefile)
sampledata = list(samplereader)
sampledata