import os 
os.system("cls")

def suma_multiplos(n):
    total = 0
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 != 0:
            total += i
    return total

def main():
    n = int(input("Número entero positivo (n): "))
    resultado = suma_multiplos(n)
    print(f"La suma de los múltiplos de 3 que no son múltiplos de 5, menores o iguales a {n}, es: {resultado}")

if __name__ == "__main__":
    main()