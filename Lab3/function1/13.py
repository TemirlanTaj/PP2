import random 
name = input("What is ypur name? \n")
print(f"Well, {name}, I'm thinking of a number between 1 to 20")
goal = random.randint(1, 20)
guess = ""
c = 0
while guess != goal:
    c += 1
    guess = int(input("Take a guess: "))
    if guess < goal:
        print("too low")
    elif guess > goal:
        print("too high")
print(f"Congratulation, {name}, you guessed the number in {c} tries")