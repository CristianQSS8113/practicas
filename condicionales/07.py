import os
os.system("cls")

numero1 = int(input("Primer número: "))
numero2 = int(input("Segundo número: "))
numero3 = int(input("Tercer número: "))

numero_intermedio=numero1

if (numero1 > numero2 and numero1 < numero3) or (numero1 < numero2 and numero1 > numero3):
    numero_intermedio = numero1
elif (numero2 > numero1 and numero2 < numero3) or (numero2 < numero1 and numero2 > numero3):
    numero_intermedio=numero2
else:
    numero_intermedio=numero3
    
print(f"Número intermedio es: {numero_intermedio}")