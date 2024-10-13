import os 
os.system("cls")

n = int(input("Ingrese la base (n): "))
m = int(input("Ingrese el exponente (m): "))
resultado = 1
i = 0

while i < m:
    resultado *= n
    i += 1

print(f"{n} elevado a {m} es {resultado}.")