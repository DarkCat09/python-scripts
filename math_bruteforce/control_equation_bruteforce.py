# Math equation brutforce

print()
print("*** MATH EQUATION BRUTEFORCE ***")
print("********* by DarkCat09 *********")
print()

if input("Press ENTER or type y for start\nType n to exit\n") == 'n':
    quit()

print()
print("START!")

y = -1
result = 0
while result != (y + 10):
    y += 1
    result = y + y - 25
    print(str(y) + " + " + str(y) + " - 25 = " + str(result))
    if y > 1000:
        print("1000 iterations reached! Exiting!")
        break

print()
print(str(y))
print()
input("Press ENTER")
