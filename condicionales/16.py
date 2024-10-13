import os
os.system("cls")

ingreso_mensual= float(input("Ingrese mensual: "))

costo_casa= float(input("Costo de la casa: "))

if ingreso_mensual < 1250:
    cuota_inicial = 0.15 * costo_casa
    cuotas_mensuales = (costo_casa - cuota_inicial) / 120
else:
    cuota_inicial= 0.30 * costo_casa
    cuotas_mensuales= (costo_casa - cuota_inicial) / 75

print(f"Cuota inicial: S/. {cuota_inicial:.2f}")    
print(f"Cuota mensual: S/. {cuotas_mensuales:.2f}")