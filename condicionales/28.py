import os
os.system("cls")

hora_24 = input("Hora en formato 24 horas (HH:MM): ")

horas, minutos = hora_24.split(':')
horas = int(horas)
minutos = int(minutos)


if 0 <= horas < 24 and 0 <= minutos < 60:
    periodo = "AM" if horas < 12 else "PM"
    horas_12 = horas % 12 or 12
    print(f"{horas_12}:{minutos:02d} {periodo}")
else:
    print("Hora inválida.")