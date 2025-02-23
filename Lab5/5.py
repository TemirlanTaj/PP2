import re

text = "aoaefhopb"

res = re.match(r".*a.+b$", text)

if res:
    print(res.group())
    print("True")
else:
    print("False")