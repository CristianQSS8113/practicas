import os 
os.system("cls")

numero = int(input("Número entero: "))
cantidad_divisores = 0
i = 1

while i <= abs(numero):
    if numero % i == 0:
        cantidad_divisores += 1
    i += 1

print(f"La cantidad de divisores de {numero} es: {cantidad_divisores}")