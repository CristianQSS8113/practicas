import os
os.system ("cls")

horas_trabajadas=float(input("Horas trabajadas: "))
tarifa_hora=float(input("Tarifa por hora: "))

if horas_trabajadas <= 48:
    sueldo_bruto= horas_trabajadas * tarifa_hora
else:
    horas_extras=horas_trabajadas-48
    sueldo_bruto=(48*tarifa_hora) + (horas_extras * tarifa_hora * 1.2)
    
descuento= 0
if sueldo_bruto > 1500:
    descuento = sueldo_bruto * 0.11

total_a_pagar=sueldo_bruto-descuento

print(f"Horas trabajadas: {horas_trabajadas}")
print(f"Pago por hora: S/.{tarifa_hora:.2f}")
print(f"Sueldo bruto: S/.{sueldo_bruto:.2f}")
print(f"Descuento: S/.{descuento:.2f}")
print(f"Total a pagar: S/. {total_a_pagar:.2f}")