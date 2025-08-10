a=3
b=4
if b<a:
    print("Hello")

a = 35
b = 34
c = 200

if b>a:
    print("b is greater")

elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


# short hand if

if a> b: print("a is greater than b")

# short hand elif
print("A") if a>b else print("B")


# and
if a>b and b>c:
    print("Hello there!")
else:
    print("Error!")

# or

if a>b or a>c:
    print("Atleast one condition is true!")