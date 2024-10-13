import os
os.system("cls")

practica1=float(input("Nota de primera practica: "))
practica2=float(input("Nota de segunda practica: "))
practica3=float(input("Nota de tercera practica: "))

if practica3>= 10:
    practica3 +=2
    
promedio_final=( practica1 + practica2 + practica3 ) / 3

print(f"Promedio final: {promedio_final:.2f}")