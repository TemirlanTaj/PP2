import re

text = "hello_world_test_example"

textSplit = text.split("_")
res = ""
for i in textSplit:
    res += i.capitalize()
res = res[0].lower() + res[1:]


print(res)