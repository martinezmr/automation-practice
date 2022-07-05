#matches any character within the pattern
import re

pattern = r"[aeiou]"

if re.search(pattern, "grey"):
    print("Match 1")

if re.search(pattern, "qwertyuiop"):
    print("Match 2")

if re.search(pattern, "rhythm myths"):
    print("Match 3")


#matches any character in the first bracket, followed by the second bracket, and third
pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
    print("Match 1")

if re.search(pattern, "E3"):
    print("Match 2")

if re.search(pattern, "1ab"):
    print("Match 3")

#does not match any characters within bracket because of '^'
pattern = r"[^A-Z]"

if re.search(pattern, "this is all quiet"):
    print("Match 1")

if re.search(pattern, "AbCdEfG123"):
    print("Match 2")

if re.search(pattern, "THISISALLSHOUTING"):
    print("Match 3")


#use $ at end to set the ending for the pattern string
Id = input()

pattern = r"[A-Z][A-Z][0-9][0-9]$"

if re.search(pattern, Id):
    print("Searching")
else:
    print("Wrong format")