str = input("What word do you want to check? \n")

if str == str[::-1]:
    print("It a palindrome")
else:
    print("It is not a palindrome")

