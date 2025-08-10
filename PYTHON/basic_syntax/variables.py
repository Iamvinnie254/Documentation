#creating variables

x = 5
y = "John"

print(x)
print(y)


#Casting

x=str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

#Getting the type

x = 5
y = "john"
print(type(x))
print(type(y))

#Many values to multiple variables

x,y,z = "maize", "beans","oranges"

print(x)
print(y)
print(z)

# One value to multiple variables

x=y=z = "Cherry"
print(x)
print(y)
print(z)

# Unpacking a collection

fruits = ['banana', 'mango','kiwi']

x, y , z = fruits
print(x)
print(y)
print(z)


# Global variables - variables that are created outside of a function

x = 'Awesome'

def myFunc():
    print("Python is "+x)

myFunc()


# The global keyword

def func():
    global x
    x = "fantastic"

func()
print('Python is '+x)