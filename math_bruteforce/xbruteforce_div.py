from fractions import Fraction
import time

print("***X BRUTEFORCE - DIVISION***")
print()

imit = int(input("Включить имитацию брутфорс-взлома хэша (небольшая задержка при подборе)?\nответ: 0-выкл., 1-вкл., 2-в.скорость, 3-оч.в.скорость: "))
print()

accuracy = Fraction(input("Укажите точность числа с плавающей запятой (float).\nответ: 1-только целочисл. знач., 0.1=0.1, 0.01=0.01, ... : "))
print(accuracy)
print()

x = input("Первое число (x, если неизвестно): ")
y = input("Второе число (x, если неизвестно): ")
z = input("Результат (x, если не известен): ")
res = 0
a = Fraction(0)

#Checking - what number is X
#and Bruteforcing
if ((x == "x") and (not (y == "x")) and (not (z == "x"))):
    while (not (Fraction(a) == (Fraction(z)*Fraction(y)))):
        print(str(float(Fraction(a))) + "/" + str(float(Fraction(y))) + "=" + str(float((Fraction(a)/Fraction(y)))))
        a = Fraction(a) + accuracy
        if (imit == 1):
            time.sleep(0.07)
        if (imit == 2):
            time.sleep(0.007)
        if (imit == 3):
            time.sleep(0.001)
    print(str(float(Fraction(a))) + "/" + str(float(Fraction(y))) + "=" + str(float((Fraction(a)/Fraction(y)))))
    print ("OK!")
    print("x is", float(Fraction(a)))
elif ((y == "x") and (not (z == "x")) and (not (x == "x"))):
    a = Fraction(a) + accuracy
    while (not (Fraction(a) == (Fraction(x)/Fraction(z)))):
        print(str(float(Fraction(x))) + "/" + str(float(Fraction(a))) + "=" + str(float((Fraction(x)/Fraction(a)))))
        a = Fraction(a) + accuracy
        if (imit == 1):
            time.sleep(0.07)
        if (imit == 2):
            time.sleep(0.007)
        if (imit == 3):
            time.sleep(0.001)
    print(str(float(Fraction(x))) + "/" + str(float(Fraction(a))) + "=" + str(float((Fraction(x)/Fraction(a)))))
    print ("OK!")
    print("x is", float(Fraction(a)))
elif ((z == "x") and (not (y == "x")) and (not (x == "x"))):
    attempt = 0
    while (not (Fraction(a) == (Fraction(x)/Fraction(y)))):
        print(str(float(Fraction(x))) + "/" + str(float(Fraction(y))) + "=" + str(float(Fraction(a))))
        #for debug
        #print(Fraction(a), accuracy)
        
        if (attempt > 3000):
            #Protection
            print()
            stopAndCalc = int(input("Попыток взлома уже больше 3000. Использовать обычный калькулятор?\nответ: 1-да, 0-нет: "))
            if (stopAndCalc):
                a = Fraction(x)/Fraction(y)
                break
            else:
                print("Что ж, это Ваше дело.\nВ любой момент можно остановить программу нажатием клавиш Ctrl+C")
                print()

        a = Fraction(a) + accuracy
        if (imit == 1):
            time.sleep(0.07)
        if (imit == 2):
            time.sleep(0.007)
        if (imit == 3):
            time.sleep(0.001)
        attempt = attempt + 1
    print(str(float(Fraction(x))) + "/" + str(float(Fraction(y))) + "=" + str(float(Fraction(a))))
    print("OK!")
    print()
    print("x is", float(Fraction(a)))
else:
    print("Ошибка!")

print()
input("Чтобы выйти, нажмите ENTER")
