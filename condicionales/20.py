import os
os.system("cls")

a=float(input("Primer número: "))
b=float(input("Segundo número: "))
c=float(input("Tercer número: "))

if a < b < c:
    orden="ascedente"
elif a > b > c:
    orden="descendete"
else:
    orden ="desordenado"
    
print(f"Los número están en orden {orden}. ")