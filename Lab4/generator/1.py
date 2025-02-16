def square(num):
    # for i in range(num):
    #     yield i*i
    start = 1
    while start <= num:
        yield start*start
        start += 1



N = int(input())

squares = square(N)

for i in squares:
    print(i)