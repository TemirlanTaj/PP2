import math

def degToRad(d):
    x = math.pi * d / 180
    return x

def radToDeg(r):
    x = r * 180 / math.pi

n = int(input("Input degree: "))
print("Output radian:", degToRad(n))





'''
180 - pi
deg - rad
rad = pi * deg / 180
deg = r * 180 / pi
'''