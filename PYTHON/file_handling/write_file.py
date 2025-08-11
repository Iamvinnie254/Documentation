
with open("demofile.txt","a") as f:
    f.write("Now this is additional stuff!")


with open("demofile.txt") as f:
    print(f.read())