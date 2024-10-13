import os
os.system("cls")

sexo= input("Sexo (F/M): ").strip().upper()
edad = int(input("Edad: "))

if sexo == 'F':
    categoria= 'FA' if edad <23 else 'FB'
elif sexo== 'M':
    categoria= 'MA' if edad <25 else 'MB'
    
print(f"Categoria del postulante: {categoria}")