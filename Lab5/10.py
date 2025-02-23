import re

text = "hellowWorldTestExample"

res = re.sub(r'([A-Z])', r'_\1', text).lower()

print(res)