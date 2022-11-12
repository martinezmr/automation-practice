# else statements can be used with for and while loops as well

for i in range(10):
    if i == 999:
        break
else:
    print("Unbroken 1")

for i in range(10):
    if i == 5:
        break
else:
    print("Unbroken 2")

# example 2
ages = []
i = 0
while i<3:
   age = int(input())
   ages.append(age)
   i+=1
   if age < 16:
      print("Too young!")
      break
else:
   print("Get ready!")

# else statement prints if try statement succeeds
try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)