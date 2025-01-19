#Python Variables

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a

#Legal variables names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

myVariableName = "John"   #Camel case - each word, except the first, starts with a capital letter
MyVariableName = "John"   #Pascal case - each word, except the first
my_variable_name = "John" #Snake case - each word is separated by an underscore character

x, y, z = "Orange", "Banana", "Cherry" #Many Values to Multiple Variables
print(x)
print(y)
print(z)

x = y = z = "Orange" #One Value to Multiple Variables
print(x)
print(y)
print(z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z) #Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".


x = "awesome" #Global variable

def myfunc():
  x = "fantastic" #Local variable
  print("Python is " + x)

myfunc()

print("Python is " + x)
