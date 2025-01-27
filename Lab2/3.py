#Python Lists

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
list1 = ["abc", 34, True, 40, "male"]
#List is a collection which is ordered and changeable. Allows duplicate members.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist[1] = "blackcurrant" #how to change elements
print(thislist)
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"] #how to add elements
thislist.insert(2, "watermelon")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
thislist = ["apple", "banana", "cherry"] #extend
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"] #how to remove items
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
thislist.pop() #remove last item
thislist.clear() #removes all items

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = [100, 50, 65, 82, 23]
thislist.sort() # reverse = true for reverse
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)