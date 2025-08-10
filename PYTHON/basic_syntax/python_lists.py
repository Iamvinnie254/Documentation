# Python lists

# Used to store multiple items in a single variable

thislist = ['apple','cherry','mango','pineapple']
print(thislist)
print(len(thislist))
print(type(thislist))

# list constructor

mylist = list(("john","jane","mike"))
print(mylist)

# Access list items

print(mylist[1])

# append items

mylist.append("oranges")
print(mylist)

mylist.insert(1,"ken")

print(mylist)

# extendint lists
thislist.extend(mylist)
print(thislist)

# remove items

mylist.pop(1)
print(mylist)

# looping through a list

for x in mylist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])


# while loop


i = 0
while i <len(thislist):
    print(thislist[i])
    i = i + 1

# looping using list comprehension

[print(x) for x in mylist]


# 

fruits = ['kiwi','banana','mango']
newlist = []

for x in fruits:
   if "a" in x:
      newlist.append(x)
print(newlist)

# OR
newlist = [x for x in fruits if "a" in x]
print(newlist)