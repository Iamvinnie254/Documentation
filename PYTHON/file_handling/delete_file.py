
import os

os.remove("demofile.txt")


# check if the file exists

if os.path.exists("demo.txt"):
    os.remove("demo.txt")
else:
    print("The file does not exist!")