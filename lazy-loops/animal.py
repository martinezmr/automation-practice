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