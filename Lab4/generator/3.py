def divisibleBy3and4(num):
    start = 0
    while start <= num:
        if start % 3 == 0 and start % 4 == 0:
            yield start
        start += 1

N = int(input())

listOfNums = divisibleBy3and4(N)

for i in listOfNums:
    print(i)