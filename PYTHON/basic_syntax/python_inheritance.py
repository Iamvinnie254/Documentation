# a class inherits all the methods and properties of another class

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
         print(self.firstname, self.lastname)


# use the person class to create an object, and then execute the printname method:

x = Person('john', 'doe')
x.printname()


# a child class Student

class Student(Person):
    pass

x = Student("ken","ken")
x.printname()

# or

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self,fname, lname)
x = Student("kenny","kennito")
x.printname()

# or
class Student(Person):
    def __init__(self, fname, lname):
       super().__init__(fname, lname)
x = Student("kennito","ken ken")
x.printname()