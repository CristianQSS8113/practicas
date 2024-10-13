import os
os.system("cls")

numero = input("Número de 4 cifras: ")

if len(numero) ==4:
    cifras=[int(d) for d in numero]
    mayor = max(cifras)
    menor = min(cifras)
    
    
    mayor_numero= max(mayor*10+ menor, menor* 10+ mayor)
    
    print(f"Mayor numero de dos cifras: {mayor_numero}")
