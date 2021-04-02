print("")
print("***MATH SIGNS BRUTEFORCE***")
print("*******light version*******")
print("")

sucess = False

#Entering values
a  = int(input("Enter first number: "))
b  = int(input("Enter second number: "))
eq = int(input("Enter result: "))
print("")

#Helper function
def checkResult(sign):
    if (not (sign == "+" or sign == "-" or sign == "*" or sign == "/")):
        return "Error!"
    else:
        #Calculator
        if (sign == "+"):
            return a+b
        elif (sign == "-"):
            return a-b
        elif (sign == "*"):
            return a*b
        elif (sign == "/"):
            return a/b
        else:
            return "Error."

#Bruteforce
for s in ["+", "-", "*", "/"]:
    if (checkResult(s) == eq):
        print("Sucess!")
        print("Correct sign for this expression:", s)
        sucess = True
        break

if (not sucess):
    print("Failed!")

print("")
input("Press enter to exit...")
