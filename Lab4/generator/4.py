def squaresRange(a, b):
    for i in range(a, b):
        yield i*i

N1 = int(input())
N2 = int(input())

listOfNums = squaresRange(N1, N2)

for i in listOfNums:
    print(i)