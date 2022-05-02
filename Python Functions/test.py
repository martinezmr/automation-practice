names = ["John", "Oscar", "Jacob"]

file = open("names.txt", "w+")
#write down the names into the file
for i in names:
    file.write(i+ "\n")
file.close()

file= open("names.txt", "r")
#output the content of file in console
print(file.read())

file.close()