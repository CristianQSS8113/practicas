import os 
os.system("cls")

def main():
    cadena = input("Ingrese la cadena principal: ")
    subcadena = input("Ingrese la subcadena a buscar: ")
    indice = cadena.find(subcadena)
    print(f"Índice: {indice}" if indice != -1 else "No se encontró.")

if __name__ == "__main__":
    main()