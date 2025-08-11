
x = True


try:
    print(x)

except NameError:
    print(" Variable x is not defined!")

except:
    print("There is another error!")

else:
    print("nothing went wrong!")

finally:
    print("This code lock ends!")