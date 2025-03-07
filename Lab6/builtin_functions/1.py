import functools

list = [1,2,3,4,6,10,40]

res = functools.reduce(lambda a, b: a*b, list)

print(res)