import os
os.system("cls")

numero1=input("primer número de 3 cifras")
numero2=input("segundo número de 3 cifras")

invertido1= numero2[0] + numero1[1] + numero2[2]
invertido2= numero1[0] + numero2[1] + numero1[2]

print(f"Número invertido: {invertido1}")
print(f"Número invertido: {invertido2}")
