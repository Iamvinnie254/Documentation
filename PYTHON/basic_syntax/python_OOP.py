# Object oriented programming

# Python is object oriented, allowing you to structure your code using classes and objects for better organization and reusability

# Classes and Objects
# a classdefines what an object should look like, and an object is created based on that class.

# a class is like the object constructor or a "blueprint" for creating objects

class Myclass:
    x = 5


    # creating an object
p1 = Myclass()
print(p1)



# the __init__() method

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("john", 20)

print(p1.name)
print(p1.age)
print(p1)

# the __str__() method

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"
        
p1 = Person('John', 20)
print(p1)