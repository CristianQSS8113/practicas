import os
os.system ("cls")

sueldo_bruto = float(input("Sueldo bruto del empleado: "))
numero_hijos = int(input("Número de hijos: "))

if numero_hijos > 1:
    bonificacion = (0.125 * sueldo_bruto) + (40 * numero_hijos)
else:
    bonificacion = 0.10 * sueldo_bruto
    
sueldo_neto=sueldo_bruto+bonificacion

print(f"Bonificacion: S/. {bonificacion:.2f}")
print(f"Sueldo neto a pagar: S/. {sueldo_neto:.2f}")