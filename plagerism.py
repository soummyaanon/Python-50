import re

txt = "i study in the university of texas at arlington"
x = re.search(r"\buniversity\b", txt)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
    