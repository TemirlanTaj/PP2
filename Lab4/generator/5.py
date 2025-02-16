def reverse(num):
    while num > 0:
        yield num
        num -= 1

N = int(input())

listOfNums = reverse(N)

for i in listOfNums:
    print(i)