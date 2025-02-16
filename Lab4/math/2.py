def areaOfTrapez(h, b1, b2):
    x = h * (b1 + b2) / 2
    return x


height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

print("The area of the trapezoid is:", areaOfTrapez(height, base1, base2))