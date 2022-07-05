import re

pattern = r"(.+) \1"
# \ matches the expression of the group of that number
match = re.match(pattern, "word word")
if match:
    print ("Match 1")

match = re.match(pattern, "?! ?!")
if match:
    print ("Match 2")    

match = re.match(pattern, "abc cde")
if match:
    print ("Match 3")


pattern = r"(\D+\d)"
# \d - match digits, \s - whitespace, \w - word characters
# Uppercase does the opposite of the lowercase, i.e. \D does not match digits
match = re.match(pattern, "Hi 999!")
if match:
    print("Match 1")

match = re.match(pattern, "1, 23, 456!")
if match:
    print("Match 2")

match = re.match(pattern, " ! $?")
if match:
    print("Match 3")


# print only hashtags
text = input()
#your code goes here
#use re.findall() with r"#\w+" as the regex
pattern = r"#\w+"
match = re.findall(pattern, text)

if match:
    print("\n".join(match))


pattern = r"\b(cat)\b"
# \A and \Z matche the beginning and end of a string
# \b matches the empty string between \w and \W characters (boundary between words basically)
# \B matches the empty string anywhere else
match = re.search(pattern, "The cat sat!")
if match:
    print ("Match 1")

match = re.search(pattern, "We s>cat<tered?")
if match:
    print ("Match 2")

match = re.search(pattern, "We scattered.")
if match:
    print ("Match 3")