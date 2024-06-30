animal_counts = {"squirrel": 2, "birds": 8, "cat": 1, "raccoon": 5}

#for loops
# too_many = []
# for animal, count in animal_counts.items():
#     if count > 4:
#         too_many.append(animal)

#comprehension below (same as for loop)
too_many = [
    animal
    for animal, count in animal_counts.items()
    if count > 4
]

print(too_many)


# numbers = [2,1,3,4,7,11,18]

# doubled_numbers = []
# for n in numbers:
#     doubled_numbers.append(n*2)
# # doubled_numbers = n*2 for n in numbers
# print(doubled_numbers)

numbers = []
for i in range (1,101):
    numbers.append(i)

##########################################
##list comprehension shortens the function
numbers = [i for i in range(1,101)]



#######################################################################


numbers = []
for i in range (1,101):
    if i % 3 != 0:
        numbers.append(i)
##########################################
##list comprehension shortens the function with an if statement 
numbers = [i for i in range(1,101) if i % 3 != 0]


#################accessing items in dictionarys
test_scores = {
    'Jeff': 'A',
    'Joe': 'B'
}

for person, grade in test_scores.items():
    print(person,'got',grade)

measurements = [0 for i in range(3)]
print(measurements)
