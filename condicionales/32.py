import os
os.system ("cls")

pensiones = {'A': (550, 0, 13.99, 0), 'B': (500, 14, 15.99, 0.10), 'C': (450, 16, 17.99, 0.12), 'D': (400, 18, 20, 0.15)}

categoria = input("Categoría (A, B, C, D): ").upper()
promedio = float(input("Promedio: "))

if categoria in pensiones:
    pension, min_prom, max_prom, descuento = pensiones[categoria]
    descuento_aplicado = pension * descuento if min_prom <= promedio <= max_prom else 0
    nueva_pension = pension - descuento_aplicado
    
    print(f"Pensión: S/. {pension:.2f}, Descuento: S/. {descuento_aplicado:.2f}, Nueva: S/. {nueva_pension:.2f}")
else:
    print("Categoría inválida.")