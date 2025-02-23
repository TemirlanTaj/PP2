import re

text = "abbbbbbbbbbbbbb"

res = re.match(r"ab*", text)

if res:
    print("True")
else:
    print("False")