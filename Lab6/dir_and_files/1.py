import os

path = r"C:\Users\Hp\Desktop\PP2\Lab6"

everything = os.scandir(path)
files = []
dirs = []

for i in everything:
    if i.is_file():
        files.append(i.name)
    elif i.is_dir():
        dirs.append(i.name)

print(f"Files: {files}")
print(f"Dirs: {dirs}")
print(f"All: {dirs + files}")
