#Python Sets

myset = {"apple", "banana", "cherry"} #automaticly
print(myset)

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

set1 = {"abc", 34, True, 40, "male"}
print(type(set1))

thisset = {"apple", "banana", "cherry"} #sets are unindexed
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

'''The union() and update() methods joins all items from both sets. 

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
'''
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2 #union, works only with sets and sets. Add union_update for other
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2 #intersection, works only with sets and sets. Add intersection_update for other
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2 #difference, works only with sets and sets. Add difference_update for other
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2 #symetric_difference, works only with sets and sets. Add symmetric_difference_update for other
print(set3)