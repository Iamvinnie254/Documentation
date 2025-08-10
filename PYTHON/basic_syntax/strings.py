# 

print("Hello world!")

# Assigning string to a variable
a = "This is programming"
print(a)

#multiline strings

a = """ this is
 a multiline
 string
"""

print(a)


# strings are arrays

a = "Hello, john"

print(a[1])


# looping through an array

for x in "banana":
    print(x)


# string length

a = "Hello, there!"
print(len(a))

#check string

txt = "I am a programmer"
print("programmer" in txt)

#check if not

txt = 'I am a programmer'
print("hello" not in txt)

# or

if "hello" not in txt:
    print("Not present")

# Slicing strings

b = "Hello there!"
print(b[2:5])
print(b[:6])
print(b[2:])
print(b[-5:-2]) # negative indexing

# Uppercase

a = "hello there"
print(a.upper())

# Lower case
a = "HELLO AGAIN"
print(a.lower())

# removing whitespaces

a = "  All this is awesome   "
print(a.strip())

# replace string

a = "Hello world!"
print(a.replace("H", "J"))

# split string

a = "Hello, there!"
print(a.split(","))

# string formatting
# F-Strings

age = 20
txt = f"My name is john, i am {age}"

print(txt.encode())

# escape character

# \

# String methods

""" 
capitalize()
casefold()
center()
count()
encode()
endswith()
expandtabs()
find()
format()
format_map()
index()
isalnum()
isalpha()
isascii()
isdecimal()
isdigit()








 """