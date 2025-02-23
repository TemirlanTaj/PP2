import re

text = "hellowWorldTestExample"

res = re.sub(r'([A-Z])', r' \1', text)

print(res)