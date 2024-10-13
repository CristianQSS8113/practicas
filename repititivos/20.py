import os 
os.system("cls")

def main():
    numeros = [float(input(f"Ingrese el número {i+1}: ")) for i in range(10)]
    print(f"Menor: {min(numeros)}")
    print(f"Mayor: {max(numeros)}")
    print(f"Promedio: {sum(numeros) / len(numeros):.2f}")

if __name__ == "__main__":
    main()