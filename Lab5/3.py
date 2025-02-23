import re

text = "ajdknad_kandjdsn"

res = re.match(r".*[a-z]_[a-z]", text)

if res:
    print(res.group())
    print("True")
else:
    print("False")