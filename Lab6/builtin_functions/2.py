str = input("Enter your string: ")

cLower = len(list(filter(str.isupper, str)))
cUpper = len(list(filter(str.islower, str)))

print(f"Uppercase letters: {cLower}")
print(f"Lowercase letters: {cUpper}")