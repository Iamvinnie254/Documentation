# python dictionaries
# Stores data values in key:value pairs
# A dictionary is a collection which is ordered* , changeable and do not allow duplicates

dict = {
    'brand':'Ford',
    'model':'Mustang',
    'year':1964

}

print(dict)
print(dict["year"])
print(len(dict))
print(type(dict))

x = dict.keys()
print(x)

x = dict.get("model")
print(x)



# looping through the dictionary
for x in dict:
    print( "items in dict:",x)


# copying a dictionary
mydict = dict.copy()
print(mydict)
#dict constructor
""" 
cars = dict(name = "camaro", model = "isuzu", year= 2010, origin ="puetoricco" )
print(cars) """