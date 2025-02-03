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
    

a = list(input("Enter your number: ").split())
print(a)
filter_prime(a)