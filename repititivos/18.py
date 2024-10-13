import os 
os.system("cls")

def ltrim(texto):
    return texto.lstrip()

def rtrim(texto):
    return texto.rstrip()

def alltrim(texto):
    return texto.strip()

def main():
    cadena = input("Ingrese una cadena de texto: ")
    print(f"Ltrim: '{ltrim(cadena)}'")
    print(f"Rtrim: '{rtrim(cadena)}'")
    print(f"Alltrim: '{alltrim(cadena)}'")

if __name__ == "__main__":
    main()