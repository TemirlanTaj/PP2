def solve(numheads, numlegs):
    probableLegs = numlegs / 2
    rabbitHeads = probableLegs - numheads
    chickenHeads = numheads - rabbitHeads
    print(f"We have {int(chickenHeads)} chicken and {int(rabbitHeads)} rabbit")

a = int(input("How many heads do we have? \n"))
b = int(input("How many legs do we have? \n"))

solve(a, b)