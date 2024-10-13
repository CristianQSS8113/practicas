import os 
os.system("cls")

def mostrar_numeros():
    for i in range(1, 101):
        print(f"{i:2}", end=' ')
        if i % 10 == 0:
            print()  

def main():
    mostrar_numeros()

if __name__ == "__main__":
    main()