import os

path = r"C:\Users\Hp\Desktop\PP2\Lab6\dir_and_files\5.txt"
with open(path) as f:
    print(f.read())
print("=========================")
file = open(path, 'w')
file.write("abcabc")
file.close()
with open(path) as f:
    print(f.read())

