import os
os.system("cls")

longitud_km = int ( input ( " Ingrese el primer tramo en KM : " ))
longitud_pies = int ( input ( " Ingrese el segundo tramo en pies :" ))
longitud_millas = int ( input ( "Ingrese el tercer tramo en millas : " ))

metro_por_km = 1000
metro_por_pie = 3.2808
metro_por_milla= 1609

metros_km = longitud_km * metro_por_km
metros_pie = longitud_pies * metro_por_pie
metros_milla= longitud_millas * metro_por_milla

longitud_total_metros=metros_km+ metros_pie + metros_milla
longitud_total_yardas= longitud_total_metros / 0.9144

print(f"Longitud total recorrida: {longitud_total_metros: .2f} metros")
print(f"Longitud total recorrida: {longitud_total_yardas: .2f} yardas")