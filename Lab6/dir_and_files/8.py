import os

path = r"C:\Users\Hp\Desktop\PP2\Lab6\dir_and_files\task6Dir\A.txt"

if os.access(path, os.F_OK): 
    if os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted succefully")
    else:
        print("Can not delete the file")
else:
    print("File does not exist")