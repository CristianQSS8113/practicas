import os
os.system ("cls")

horas_trabajadas=float(input("Horas trabajadas: "))
tarifa_horario=float(input("Tarifa horaria en dólares: "))

sueldo_basico=horas_trabajadas *  tarifa_horario

bonificacion= sueldo_basico * 0.20
sueldo_bruto = sueldo_basico + bonificacion

descuento= sueldo_bruto * 0.10
sueldo_neto= sueldo_bruto - descuento

print(f"Sueldo básico: ${sueldo_basico:.2f}")
print(f"Sueldo bruto: ${sueldo_bruto:.2f}")
print(f"Sueldo neto: ${sueldo_neto:.2f}")


