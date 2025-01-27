#Python Booleans
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15)) #Almost any value is evaluated to True if it has some sort of content.
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) #Will return 0

def myFunction() : # Functions can return boolean value
  return True