# An iterator is an object that contins a countable number of values.

mytuple = ('hen','cow','milk','sheep')
print(mytuple)

myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# creating an iterator

class Numbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 30:
            x =  self.a
            self.a +=1
            return x
        else:
            raise StopIteration
    
myclass  = Numbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
