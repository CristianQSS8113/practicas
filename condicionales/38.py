import os 
os.system ("cls")

mes = int(input("Número del mes (1-12): "))
año = int(input("Año: "))

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

días_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    días_por_mes[1] = 29  

if 1 <= mes <= 12:
    print(f"Mes: {meses[mes - 1]}, Días: {días_por_mes[mes - 1]}")
