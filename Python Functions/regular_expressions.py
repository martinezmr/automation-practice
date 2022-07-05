# used to verify strings that match a pattern
# used to perform substitutions in a string
# use import re for reg expressions

import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")

if re.search(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")

#re.finditer does same except returns the iterator
print(re.findall(pattern, "eggspamsausagespam"))


match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

#sub used to replace patterns in string
str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)