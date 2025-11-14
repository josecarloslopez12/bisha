# 11. Ejercicio.
# Crea una aplicación que dibuje una escalera de asteriscos. Nosotros le pasamos la altura de
# la escalera por teclado. Este es un ejemplo si insertaras un 5 de altura:
# *
# **
# ***
# ****
# *****

try:
    altura = int(input("Introduce la altura de la escalera: "))
    if altura <= 0:
        raise ValueError

except ValueError:
    print("Error: Solo son validos numeros enteros.")
else:
    print("\nForma nº1")
    for i in range(1, altura+1):
        for j in range(1, i+1):
            print(j, end="")
        print()

    print("\nForma nº2")
    escalera = "1"
    for i in range(2, altura+2):
        print(escalera)
        escalera = escalera+str(i)

    print("\nForma nº3")
    flag = 1
    while (flag <= altura):
        for i in range(1, flag+1):
            print(i, end="")
        print()
        flag += 1
