import os
os.system("cls")

numero= int(input("Numero asignado (cuatro cifras): "))

if 1000<= numero<=9999:
    estado_civil=numero // 1000
    edad = (numero //10) % 100
    sexo = numero % 10
    
    
    estados= {1:"Soltero", 2: "Casado", 3: "Divorciado", 4:"Viudo"}
    sexo_str="Masculino" if sexo==1 else "Femenino" if sexo ==2 else "Desconocido"
    
    print(f"Estado civil: {estados.get(estado_civil, 'Desconocido')}, Edad: {edad}. Sexo: {sexo_str}")
    