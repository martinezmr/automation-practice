contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

name = input()

for i in contacts:
    if name in i:
        print(str(i[0]) + " is " + str(i[1]))
        break
else:
    print("Not Found")

# example below shows using functions and tuples to calculate area/perimeter
def calc(x):
    return(x*4,x*x)
side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))