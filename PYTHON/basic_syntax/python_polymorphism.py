# Polymorphism means many forms
#In programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

#Function polymorphism
x = "Hello, there!"
print(len(x))


# class polymorphism
# multiple classes with the same method name
# because of polymorphism we can execute the same method for all the three classes

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!!")
        
class Boat:
    def __init__(self,brand, model):
        self.brand = brand
        self.moddel = model

    def move(self):
        print("Sail!!")

class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Flyy!!!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing","747")


for x in (car1,boat1,plane1):
    x.move()







# Inheritance class polymorphism


class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Movee!!!")

class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("sail!!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing","747")


for x in (car1,boat1,plane1):
    print("Brand: ", x.brand)
    print("Model: ",x.model)
    x.move()




