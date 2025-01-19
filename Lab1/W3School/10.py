#Python Strings
print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt) #bool inside

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

#Slicing
b = "Hello, World!"
print(b[2:5]) #Get the characters from position 2 to position 5 (not included)
b = "Hello, World!"
print(b[:5]) #Get the characters from the start to position 5 (not included)
b = "Hello, World!"
print(b[2:]) #Get the characters from position 2, and all the way to the end
b = "Hello, World!"
print(b[-5:-2]) #Use negative indexes to start the slice from the end of the string

#Modify strings
a = "Hello, World!"
print(a.upper())
a = "Hello, World!"
print(a.lower())
a = " Hello, World! " #The strip() method removes any whitespace from the beginning or the end:
print(a.strip()) # returns "Hello, World!"
a = "Hello, World!" #The replace() method replaces a string with another string:
print(a.replace("H", "J"))
a = "Hello, World!" #The split() method splits the string into substrings if it finds instances of the separator:
print(a.split(",")) # returns ['Hello', ' World!']

#Format Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)
price = 59
txt = f"The price is {price:.2f} dollars" #Display the price with 2 decimals:
print(txt)

#Escape characters
txt = "We are the so-called \"Vikings\" from the north."
'''
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value

'''