#Python Dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)
x = thisdict.keys() #or thisdict.vaules() to get values
print(x)

thisdict["color"] = "white"
print(thisdict)

thisdict.update({"year": 2020})
print(thisdict)

thisdict.pop("model")
print(thisdict)

for x in thisdict:
  print(thisdict[x])

mydict = thisdict.copy()
print(mydict)

myfamily = { #nested dictionaries
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}