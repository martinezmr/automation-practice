import re

pattern = r"gr.y"
#pattern match for anything that is gr#y
if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "blue"):
    print("Match 3")


pattern = r"^gr.y$"
# ^ and $ match start and end of string, i.e. must start with gr and end in y
if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "stingray"):
    print("Match 3")