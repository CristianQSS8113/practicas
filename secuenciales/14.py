import os
os.system("cls")

import math

num1= float(input("Primer número: "))
num2= float(input("Segundo número: "))
num3= float(input("Tercer número: "))
num4= float(input("Cuarto número: "))
num5= float(input("Quinto número: "))

numeros=[num1, num2, num3, num4, num5]

numeros.sort()

mayor1 = numeros[2]
mayor2 = numeros[3]
mayor3 = numeros[4]

promedio=(mayor1+mayor2+mayor3)/3

print(f"Promedio de los tres números mayores es: {promedio}")
