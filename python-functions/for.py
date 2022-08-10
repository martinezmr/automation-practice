#for loops
for i in range(5):
    print(i)


#continue key word will make condition continue to run
for i in range(5):
    if i == 2:
        continue
        print("done")

ages = [4, 7, 26, 27]
total = 0
for age in ages:
    total += age
print(total)