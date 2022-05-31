import csv

with open("C:/Users/mmart/automation-practice/dnac-scripts/import_template.csv", mode="r") as infile:
    reader = csv.reader(infile)
    with open("C:/Users/mmart/automation-practice/dnac-scripts/import_template_new.csv", mode="w") as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1]} for rows in reader}


