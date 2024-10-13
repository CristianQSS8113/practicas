import os
os.system("cls")

tardanza = int(input("Minutos de tardanza: "))
observaciones = int(input("Cantidad de observaciones: "))

puntaje_puntualidad = 10 if tardanza == 0 else 8 if tardanza <= 2 else 6 if tardanza <= 5 else 4 if tardanza <= 9 else 0
puntaje_rendimiento = 10 if observaciones == 0 else 8 if observaciones == 1 else 5 if observaciones == 2 else 1 if observaciones == 3 else 0

puntaje_total = puntaje_puntualidad + puntaje_rendimiento
bonificacion = 12.5 * puntaje_total if puntaje_total >= 20 else 10.0 * puntaje_total if puntaje_total >= 17 else 7.5 * puntaje_total if puntaje_total >= 14 else 5.0 * puntaje_total if puntaje_total >= 11 else 2.5 * puntaje_total

print(f"Puntaje por puntualidad: {puntaje_puntualidad}\nPuntaje por rendimiento: {puntaje_rendimiento}\nPuntaje total: {puntaje_total}\nBonificación anual: S/. {bonificacion:.2f}")