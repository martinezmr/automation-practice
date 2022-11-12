# using IN and NOT IN to show boolean values

nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)


# use get function to index.  second value is printed if first value not found
pairs = {1: "apple",
  "orange": [2, 3, 4], 
  True: False, 
  12: "True",
}
print(pairs.get("orange", "dick"))
print(pairs.get(7, 42))
print(pairs.get(12345, "not found"))