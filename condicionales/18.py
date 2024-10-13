import os
os.system("cls")

donacion=float(input("Monto de la donacion: "))

if donacion>=1000:
    centro_salud = 0.30 * donacion
    comedor_niños = 0.50 * donacion
else:
    centro_salud = 0.25 * donacion
    comedor_niños = 0.69 * donacion
    
inversion_bolsa= donacion -(centro_salud+comedor_niños)

print(f"Centro de Salud: S/. {centro_salud:.2f}")
print(f"Centro de Niños: S/. {comedor_niños:.2f}")
print(f"Centro en la Bolsa: S/. {inversion_bolsa:.2f}")