import os
os.system("cls")

ausencia = float(input("Horas de ausencia: "))
defectuosos = int(input("Tornillos defectuosos: "))
no_defectuosos = int(input("Tornillos no defectuosos: "))

if ausencia > 1.5 and defectuosos >= 300 and no_defectuosos <= 10000:
    grado = 5
elif ausencia <= 1.5 and defectuosos < 300 and no_defectuosos > 10000:
    grado = 20
elif ausencia <= 1.5 and defectuosos < 300:
    grado = 12
elif ausencia <= 1.5 and no_defectuosos > 10000:
    grado = 13
elif defectuosos < 300 and no_defectuosos > 10000:
    grado = 15
elif ausencia <= 1.5:
    grado = 7
elif defectuosos < 300:
    grado = 8
elif no_defectuosos > 10000:
    grado = 9
else:
    grado = 5

print(f"Grado de eficiencia: {grado}")