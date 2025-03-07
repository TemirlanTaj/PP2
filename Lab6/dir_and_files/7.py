import os

path1 = r"C:\Users\Hp\Desktop\PP2\Lab6\dir_and_files\4.txt"
path2 = r"C:\Users\Hp\Desktop\PP2\Lab6\dir_and_files\7.txt"

with open(path1) as f:
    content = f.read()

with open(path2, "w") as f:
    f.write(content)

print("4.txt was copied to 7.txt")