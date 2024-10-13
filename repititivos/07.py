import os 
os.system("cls")

n = int(input("Ingrese un número entero no negativo: "))
factorial = 1
i = 1

if n < 0:
    print("El factorial no está definido para números negativos.")
else:
    while i <= n:
        factorial *= i
        i += 1

print(f"El factorial de {n} es {factorial}.")