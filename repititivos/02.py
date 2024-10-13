import os 
os.system("cls")

num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

resultado = 0
contador = abs(num2)

while contador > 0:
    resultado += num1
    contador -= 1

if (num1 < 0) ^ (num2 < 0):
    resultado = -resultado

print(f"El resultado de la multiplicación es: {resultado}")