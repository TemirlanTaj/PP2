import os

def pathCheck(path):
    if os.access(path, os.F_OK):
        if os.path.isfile(path):
            print("Name of the file:", os.path.basename(path))
        else: 
            print("This is not a file")
        print("Directory:", os.path.dirname(path))
    else:
        print("Path does not exist")


path1 = r"C:\Users\Hp\Desktop\PP2\Lab6\dir_and_files\3.py"
path2 = r"C:\Users\Hp\Desktop\PP2\Lab6\dir_and_files"
path3 = r"C:\Users\Hp\Desktop\PP2\Lab6\dir_and_files\randomstuff"

pathCheck(path1)
print("====================================================")
pathCheck(path2)
print("====================================================")
pathCheck(path3)