import os 
os.system("cls")

n = int(input("Ingrese la altura (n >= 4): "))

while n < 4:
    n = int(input("Error. Ingrese la altura (n >= 4): "))

for _ in range(n):
    print('*' * (2 * n))