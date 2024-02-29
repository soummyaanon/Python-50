import re

txt = "i pursue my higher education in the university of texas at Ohio university"
x = re.sub(r"\buniversity\b", "college", txt)
print(x)

