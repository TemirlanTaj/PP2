import math


def area(side, len):
    x = round(side * len**2 / (4 * math.tan(math.pi/side)))
    return x

a = int(input("Number of sides: "))
b = float(input("Length of sides: "))

print(f"The area of the polygon is:", area(a,b))