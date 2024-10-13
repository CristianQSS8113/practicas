import os
os.system("cls")

tardanza = int(input("Minutos de tardanza: "))
observaciones = int(input("Cantidad de observaciones: "))

puntaje_puntualidad = max(10 - tardanza // 10, 1)
puntaje_rendimiento = max(10 - observaciones, 1)
puntaje_total = puntaje_puntualidad + puntaje_rendimiento

bonificacion = 0
if puntaje_total >= 18:
    bonificacion = 1000
elif puntaje_total >= 15:
    bonificacion = 500
elif puntaje_total >= 10:
    bonificacion = 200

print(f"Puntaje por puntualidad: {puntaje_puntualidad}")
print(f"Puntaje por rendimiento: {puntaje_rendimiento}")
print(f"Puntaje total: {puntaje_total}")
print(f"Bonificación anual: S/. {bonificacion:.2f}")