#Python For Loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

for x in range(6):
  print(x)

for x in range(2, 30, 3): #2 - start, 30 - end, 3 - step
  print(x) 

for x in [0, 1, 2]: #if we want to keep the loop with no content, put pass to avoid error
  pass