import os

path = r"C:\Users\Hp\Desktop\PP2\Lab6\dir_and_files\task6Dir\\"


for i in range(1,27):
    f = f'{path}{chr(i+64)}.txt'
    open(f, 'w')

print("Files created")