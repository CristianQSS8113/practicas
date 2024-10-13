import os
os.system("cls")

numero=int(input("Numero de 4 cifras: "))

c1 = numero // 1000
numero %= 1000 
c2 = numero // 100
numero %=100
c3 = numero //10
c4 = numero % 10

suma=c1 + c2 +c3 + c4

print(f"Suma = {suma}") 