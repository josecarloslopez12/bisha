# 17. Ejercicio.
# Dibuja un ordinograma de un programa que lea dos números y lo visualiza en orden
# ascendente.

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))

if num1 > num2:
    print(num1, num2)
else:
    print(num2, num1)
