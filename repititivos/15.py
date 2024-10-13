import os 
os.system("cls")

def convertir_texto(texto):
    return texto.upper(), texto.lower()

def main():
    cadena = input("Cadena de texto: ")
    mayusculas, minusculas = convertir_texto(cadena)
    print("Mayúsculas:", mayusculas)
    print("Minúsculas:", minusculas)

if __name__ == "__main__":
    main()