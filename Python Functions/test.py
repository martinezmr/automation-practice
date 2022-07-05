import re
text = input()
#your code goes here
#use re.findall() with r"#\w+" as the regex
pattern = r"#\w+"

match = re.findall(pattern, text)

if match:
    print("\n".join(match))