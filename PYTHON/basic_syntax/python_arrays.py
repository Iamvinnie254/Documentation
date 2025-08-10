# An array is a special variable, which can hold more than one value at a time

cars = ['volvo','mazda','toyota','suzuki']
print(cars)
print(len(cars))
print(type(cars))
cars.append('honda')
print(cars)


for a in cars:
    print(a)


cars.pop(1)
print(cars)

cars.remove("volvo")
print(cars)