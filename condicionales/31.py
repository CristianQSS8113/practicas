import os
os.system("cls")

tarifas = {'A': 21.00, 'B': 19.50, 'C': 17.00, 'D': 15.50}

categoria = input("Categoría (A, B, C, D): ").upper()
horas_trabajadas = float(input("Horas trabajadas: "))

if categoria in tarifas:
    sueldo_bruto = horas_trabajadas * tarifas[categoria]
    descuento = sueldo_bruto * (0.20 if sueldo_bruto > 2500 else 0.15)
    sueldo_neto = sueldo_bruto - descuento
    
    print(f"Sueldo bruto: S/. {sueldo_bruto:.2f}")
    print(f"Descuento: S/. {descuento:.2f}")
    print(f"Sueldo neto: S/. {sueldo_neto:.2f}")
else:
    print("Categoría inválida.")