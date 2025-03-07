import time

num = int(input())
milisecs = int(input())
time.sleep(milisecs/1000)

c = pow(num, 0.5)

print(f"Square root of {num} after {milisecs} miliseconds is {c}")