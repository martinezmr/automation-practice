#yield statement used to define a generator
def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)

#infinite sevens
def infinite_sevens():
  while True:
    yield 7

for i in infinite_sevens():
  print(i)

#creates a list out of loop output
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))