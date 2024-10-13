import os  
os.system("cls")

n = int(input("Ingrese un número n: "))
x = int(input("Ingrese el límite inferior x: "))
y = int(input("Ingrese el límite superior y: "))

print(f"Tabla de multiplicar de {n} desde {x} hasta {y}:")
i = x
while i <= y:
    print(f"{n} x {i} = {n * i}")
    i += 1