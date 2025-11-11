# 5. Ejercicio.
# Dibuja un ordinograma que toma como dato de entrada un número que corresponde a la
# longitud de un radio (La longitud del radio es la mitad de la del diámetro) y nos escribe la longitud
# de la circunferencia (La longitud de una circunferencia es igual a pi por el diámetro), el área del
# círculo (El área de un círculo es pi multiplicado por el radio al cuadrado) y el volumen de la
# esfera que corresponde con dicho radio.

import math

radio = int(input("Introduce el radio: "))

print("Longitud circunferencia: ", math.pi * (radio*2))
print("Área del círculo: ", math.pi * (radio ** 2))
print("Volumen esfera: ", 4/3 * math.pi*(radio**3))
