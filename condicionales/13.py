import os
os.system ("cls")

numero=int(input("Número entero positivo de tres cifras: "))

if 100 <= numero <= 999:
    cifras =[int(d) for d in str(numero)]
    if (cifras[0] + 1 == cifras[1] == cifras[2]- 1) or (cifras[0] - 1 == cifras[1] == cifras[2] +1):
        print("Las cifras son censecutivas.")
    else:
        print("Las cifras no son consecutivas.")
else:
    print("Ingrese número solo de tres cifras.")
