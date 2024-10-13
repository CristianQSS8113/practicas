import os 
os.system("cls")

while True:
    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))

    if divisor == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        cociente = 0
        while dividendo >= divisor:
            dividendo -= divisor
            cociente += 1

        resto = dividendo
        print(f"Cociente: {cociente}")
        print(f"Resto: {resto}")

    continuar = input("¿Desea realizar otra división? (s/n): ")
    if continuar != 's':
        break