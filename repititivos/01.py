import os 
os.system("cls")

dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))

cociente = 0
if divisor == 0:
        print("No se puede dividr entre cero.")
else: 
    while dividendo >= divisor :
         cociente += 1
         dividendo -= divisor

print(f"Cociente = {cociente}")
print(f"Residuo = {dividendo}")
