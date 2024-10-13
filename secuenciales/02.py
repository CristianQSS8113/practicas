import os
os.system("cls")

medida= int ( input ( " Ingrese metros : " ) )

centimetros = medida * 100
pulgadas = centimetros / 2.54
pie = pulgadas / 12
yarda = pie/ 3

print(f"{centimetros}centimetros")
print(f"{pulgadas} pulgadas")
print(f"{pie}pie")
print(f"{yarda}yarda")