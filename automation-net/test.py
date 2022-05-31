import csv

list = [1,2,3,4,5,6,7,8]
with open('C:/Users/mmart/automation-practice/automation-net/test.csv', 'w', newline='') as f:
    write = csv.writer(f)
    for l in list:
        print('Number', l)
        write.writerow('Number', l)