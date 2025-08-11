# this is a syntax for storing and exchanging data
# JSON is text, written with javascript object notation

import json

x = '{ "name":"john", "age": 30, "city":"Newyork"}'

y = json.loads(x)
print(y) # results to a python dictionary
print(y["age"])

z = json.dumps(x)
y = json.dumps(x,  indent=20, separators=(".","="), sort_keys=True)
print(z) # results to a json string
print(y)

# you can convert the following to json strings: dict,list,tuple,string,int,float,True,False,None
print(json.dumps({"name":"john","age":30}))
print(json.dumps(['apple','kiwi','mango']))
print(json.dumps(20))