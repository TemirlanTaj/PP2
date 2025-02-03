# def palindrome_v1(s):
#     if type(s) == str:
#         temp = s[::-1]
#         if s == temp:
#             return False
#         else: 
#             return True
#     elif type(s) == list:
#         temp = []
#         for i in range(1, len(s) - 1):
#             temp += s[-i]
#         if s == temp:
#             return False
#         else: 
#             return True
        
def palindrome_v2(s):
    temp = s[::-1]
    if s == temp:
        return True
    else:
        return False

a = input()

print(palindrome_v2(a))
