import os
os.system("cls")

examenes_aprobados= int(input("Catidad de examenes aprobados (0 a 3): "))

propina_base=20
propina_por_examen=5

propina_total=propina_base

if 1<=examenes_aprobados<=3:
    propina_total+= propina_por_examen* examenes_aprobados

print(f"Monto total de la propina es: S/. {propina_total}")