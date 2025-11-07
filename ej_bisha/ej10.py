
num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))


print("Suma: ", num1+num2)
print("Resta: ", num1-num2)
print("Multiplicación: ", num1*num2)
if num1 == 0 or num2 == 0:
    print("Error, no se puede dividir entre 0")
else:
    print("División: ", num1/num2)
