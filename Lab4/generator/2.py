def even(num):
    start = 0
    while start <= num:
        if start % 2 == 0:
            yield start
        start += 1

N = int(input())

squares = even(N)

for i in squares:
    print(i)