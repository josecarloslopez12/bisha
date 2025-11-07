
num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))
num3 = int(input("Introduce el último número: "))

if num1 > num2:
    if num1 > num3:
        print(num1, "es el mayor")
    else:
        print(num3, "es el mayor")
else:
    print(num2, "es el mayor")
