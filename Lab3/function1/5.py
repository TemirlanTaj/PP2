# Если можно через itertools)
# from itertools import permutations

# a = input("Enter string: ")

# listOfPermutations = [''.join(p) for p in permutations(a)]
# print(listOfPermutations)


def permutation(str):
    n = len(str)
    res = []
    if n == 1:
        return str
    else:
        for i in range(n):
            # print(f'start {str[i]} + permutation of {str[:i] + str[i+1:]}')
            for j in permutation(str[:i] + str[i+1:]):
                # print(f'added {str[i]} + {j}')
                res += [str[i] + j]
    return res

            

a = input("Enter string: ")

print(permutation(a))