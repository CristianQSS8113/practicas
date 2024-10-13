import os
os.system("cls")

monto_vendido=float(input("Monto total vendido: "))

sueldo_base = 250

if monto_vendido <= 5000:
    comision = 0.05 * monto_vendido
elif monto_vendido <= 10000:
    comision = 0.08 * monto_vendido
elif monto_vendido <20000:
    comision=0.10 * monto_vendido
else:
    comision = 0.15 * monto_vendido

sueldo_bruto= sueldo_base + comision
descuento = 0.15 * sueldo_bruto if sueldo_bruto > 3500 else 0.08 * sueldo_bruto

sueldo_neto= sueldo_bruto - descuento

print(f"Sueldo bruto: S/. {sueldo_bruto:.2f}, Comisión: S/. {comision:.2f}, Descuento: S/. {descuento:.2f}, Sueldo neto: S/. {sueldo_neto:.2f}")