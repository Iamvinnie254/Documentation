# A random number is one that can not be predicted logically


from numpy import random 

x= random.randint(1000)
x1 = random.randint(100, size=5)
x2 = random.randint(100, size=(3,5))
y = random.rand()
y2 = random.rand(5)
z = random.choice([1,2,3,4,5,6,7,8,9])
print(x)
print(x1)
print(x2)
print(y)
print(y2)
print(z)