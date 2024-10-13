import os 
os.system("cls")

count = 0

for num in range(1000, 10000):
    cifras = [int(d) for d in str(num)]
    suma_pares = 0
    suma_impares = 0
    
    for cif in cifras:
        if cif % 2 == 0:
            suma_pares += cif
        else:
            suma_impares += cif
            
    if suma_pares == suma_impares:
        print(num)
        count += 1

print(f"Números encontrados: {count}")