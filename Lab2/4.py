#Pyrhon Tuples

mytuple = ("apple", "banana", "cherry")

thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #the same as lists

x = ("apple", "banana", "cherry") #tuples are unchangeables so we create a list
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)


thistuple = ("apple", "banana", "cherry") #the same as lists
for x in thistuple:
  print(x)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
