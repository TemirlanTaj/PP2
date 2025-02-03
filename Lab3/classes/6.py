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

a = list(map(int, input().split()))

primenums = list(filter(lambda x: isprime(x), a))

print(primenums)