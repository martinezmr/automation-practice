# assigning each item in the tuple to a variable
numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

x,y = [1,2]
x,y = y,x

print(x,y)

# variable prefaced with * takes all left over values
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)