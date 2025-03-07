import os

path = r"C:\Users\Hp\Desktop\PP2\Lab6\dir_and_files\2.py"

print(f"Existance: {os.access(path, os.F_OK)}") #exist
print(f"Readability: {os.access(path, os.R_OK)}") #readible
print(f"Writability: {os.access(path, os.W_OK)}") #writeable
print(f"Executability: {os.access(path, os.X_OK)}") #can be executed