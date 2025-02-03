def GramsToOnces(gram):
    onces = gram / 28.3495231
    print(onces)

def OuncesToGrams(ounces): #v2
    grams = ounces * 28.3495231
    print(grams)

def FtoC(F):
    C = ( 5 / 9 ) * ( F - 32 )
    print(C)

def solve(numheads, numlegs):
    probableLegs = numlegs / 2
    rabbitHeads = probableLegs - numheads
    chickenHeads = numheads - rabbitHeads
    print(f"We have {int(chickenHeads)} chicken and {int(rabbitHeads)} rabbit")

def isprime(n):
    c = 0
    #print(int(n / 2))
    for i in range(2, int(n / 2) + 1 ):
        if n % i == 0:
            #print(f"devideable by {i}")
            c += 1
    #print(c)
    if c >= 1:
        return False
    else:
        return True        

def filter_prime(l):
    res = []
    for i in range(len(l)):
        if isprime(int(l[i])):
            # print(l[i])
            res.append(l[i])
    print(res)
    
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


def revOrd(s):
    temp = s.split()
    for i in range(1, len(temp) + 1):
        print(temp[-i], end=" ")

def has_33(l):
    for i in range(len(l)):
        if l[i] == '3' and l[i + 1] == '3':
            return True
    return False

def spy_game(l):
    for i in range(len(l)):
        if l[i] == '0' and l[i + 1] == '0' and l[i + 2] == '7':
            return True
    return False

def volOfSphere(r):
    Result = (4/3) * 3.14 * r**3
    return Result

def unique(l):
    res = []
    for i in l:
        if i not in res:
            res.append(i)
    return res
        

def palindrome_v2(s):
    temp = s[::-1]
    if s == temp:
        return True
    else:
        return False

def histogram(l):
    for i in l:
        print('*' * int(i))
