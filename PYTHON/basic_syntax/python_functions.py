# python functions

# A function is a block of code that only runs when it is called

def func():
    print("hello, there!")
func()

# passing arguments

def func(fname):
    print(fname + " Njoroge")

func("Emil")
func("Ken")

# arbitrary arguments, *args

def func(*kids):
    print("The youngest kid is "+ kids[2])

func("Emil","Tobius","ken")

# arbitrary keyword arguments, **kwargs

def func(**kid):
    print("His last name is, "+kid["lname"])
func(fname = 'tobias', lname='njoroge')