# 15. Ejercicio.
# Dibuja un ordinograma de un programa que lee dos números y muestra el mayor.

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
else:
    print(f"{num2} es mayor que {num1}")
