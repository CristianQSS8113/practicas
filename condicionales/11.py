import os
os.system("cls")

numero=float(input("Ingrese un número: "))

if numero > 0:
    resultado = "El número es positivo"
elif numero < 0:
    resultado ="El número es negativo"
else:
    resultado ="El número es cero"

print(resultado)