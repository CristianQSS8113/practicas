import os 
os.system("cls")

n = int(input("Ingrese un número: "))

print(f"Tabla de multiplicar de {n}:")
i = 1
while i <= 12:
    print(f"{n} x {i} = {n * i}")
    i += 1