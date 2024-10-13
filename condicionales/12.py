import os
os.system("cls")

dia_numero=int(input("Ingrese un número del 1 al 7: "))

if dia_numero == 1:
    dia_nombre = "Lunes"
if dia_numero == 2:
    dia_nombre = "Martes"
if dia_numero == 3:
    dia_nombre = "Miercoles"
if dia_numero == 4:
    dia_nombre = "Jueves"
if dia_numero == 5:
    dia_nombre = "Viernes"
if dia_numero == 6:
    dia_nombre = "Sabado"
if dia_numero == 7:
    dia_nombre = "Domingo"
    
print(f"El día conrespohndiente es : {dia_nombre}")