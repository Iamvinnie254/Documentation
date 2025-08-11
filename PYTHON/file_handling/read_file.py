# The key function for working with files in python is the open() function
# It takes two parameters : filename and mode

# There are 4 methods(modes) for opening a file: "r"- read, "a"- append, "w"- write, "x"- create
# You can also specify if you want the file to be handled as binary or text mode: "t"- text or "b"-binary e.g.images

f = open("demofile.txt", "r")
print(f.read())
print(f.readline())
f.close()

##

with open("demofile.txt") as f:
    print(f.read())
    print(f.read(5))


with open("demofile.txt") as f:
    print(f.readline())


with open("demofile.txt") as t:

    for a in t:
        print(a)