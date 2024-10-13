import os
os.system("cls")

notas=[float(input(f"Ingrese la nota {i + 1}:  ")) for i in range(5)]

nota_mayor = max(notas)
nota_menor = min(notas)
notas.remove(nota_mayor)
notas.remove(nota_menor)

promedio= sum(notas) / len(notas)

print(f"Notas eliminadas: Mayor ={nota_mayor}, Menor= {nota_menor}")
print(f"Promedio de las notas restantes: {promedio:.2f}")