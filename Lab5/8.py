import re

text = "hellowWorldTestExample"

res = re.findall(r'.[^A-Z]*', text)

print(res)