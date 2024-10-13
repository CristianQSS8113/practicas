import os 
os.system("cls")

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    n = int(input("Ingrese un número entero positivo: "))
    if es_primo(n):
        print(f"{n} es un número primo.")
    else:
        print(f"{n} no es un número primo.")

if __name__ == "__main__":
    main()