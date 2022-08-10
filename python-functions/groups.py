import re

pattern = r"egg(spam)*"
# (spam) represents a group in the example pattern above
if re.match(pattern, "egg"):
    print("Match 1")

if re.match(pattern, "eggspamspamspamegg"):
    print("Match 2")

if re.match(pattern, "spam"):
    print("Match 3")


pattern = r"a(bc)(de)(f(g)h)i"
# group returns the whole match, the number presents an index
# groups returns all groups from the pattern
match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())


pattern = r"(?P<first>abc)(?:def)(ghi)"
# named groups where <name> is the name of the group
# and ... is the content (?P<name>...)
# non-capturing groups have the format (?:...)
# they are not accessible via the group method
match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())

pattern = r"gr(a|e)y"
# | or pype means 'or'
match = re.match(pattern, "gray")
if match:
    print ("Match 1")

match = re.match(pattern, "grey")
if match:
    print ("Match 2")    

match = re.match(pattern, "griy")
if match:
     print ("Match 3")