#

print("Enter name: ")
name = input()
print(f"Hello {name}")

# validate an input

y = True

while y == True:
    x = input("Enter a number: ")
    try:
        x = float(x)
        y = False
    except:
        print("Wrong input, please try again")



print("Thank!!!")