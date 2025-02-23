import re

text = "abbbbb"

res = re.match(r"ab{2,3}", text)

if res:
    print("True")
else:
    print("False")