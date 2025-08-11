    ###Modules###


import platform

x = platform.system()
y = dir(platform)
print("I am running: ",x)
print(y)


## Datetime

import datetime

x=datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%a"))
print(x.strftime("This is week: %W"))

# creating/constructing a date

x = datetime.datetime(2025,8,11)
print(x)
print(x.strftime("%B"))