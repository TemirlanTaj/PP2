import re

text = "random,stuff.don,t know what,to.write"

res = re.sub(r'[ ,.]', ':', text)

print(res)