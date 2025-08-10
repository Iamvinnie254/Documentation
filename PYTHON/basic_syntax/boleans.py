# Python booleans

# Booleans can either be True or False

print(10>9)
print(20==30)
print(7<4)
print(bool(8))
print(bool("hello"))


#######

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

#######

def func():
    return True

print(func())

########

x = 200
print(isinstance(x, int))