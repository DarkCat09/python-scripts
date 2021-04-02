import time

print('***КАЛЬКУЛЯТОР***')
print()

firstn = float(input("Введите первое число: "))
secondn = float(input("Введите второе число: "))
mathact = input('Выберите математическое действие(+,-,*,/): ')
equals = float(0)

if (mathact == "+"):
    equals = firstn + secondn
    print(firstn, '+', secondn, '=', equals)
elif (mathact == "-"):
    equals = firstn - secondn
    print(firstn, '-', secondn, '=', equals)
elif (mathact == "*"):
    equals = firstn * secondn
    print(firstn, '*', secondn, '=', equals)
elif (mathact == "/"):
    if (secondn != float(0)):
        equals = firstn / secondn
        print(firstn, '/', secondn, '=', equals)
    else:
        print("Делить на 0 нельзя!")
else:
    print("Неверный математический знак!")

print('Завершено.')
input("Нажмите любую клавишу для закрытия программы...")
