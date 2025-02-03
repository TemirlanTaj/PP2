string = input("Enter your string: ")

def revOrd(s):
    temp = s.split()
    for i in range(1, len(temp) + 1):
        print(temp[-i], end=" ")
        

revOrd(string)