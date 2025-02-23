import re

text = "anaASSDAadasn"

res = re.match(r".*[A-Z][a-z]", text)

if res:
    print(res.group())
    print("True")
else:
    print("False")