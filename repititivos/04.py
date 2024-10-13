import os 
os.system("cls")

n = int(input("Número : "))
m = int(input("Cantidad de múltiplos m: "))
i = 1

print(f"Los {m} múltiplos de {n} son:")
while i <= m:
    print(n * i)
    i += 1