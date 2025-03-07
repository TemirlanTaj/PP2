import os

path = r"C:\Users\Hp\Desktop\PP2\Lab6\dir_and_files\4.txt"
fileContent = open(path)

# print(fileContent.readlines())

linesList = list(fileContent)
print('Length:', len(linesList))