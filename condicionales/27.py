import os
os.system("cls")

monto_vendido = float(input("Monto total vendido: "))

sueldo_bruto= 600 + 0.15 * monto_vendido
descuento = sueldo_bruto * (0.10 if sueldo_bruto > 1800 else 0.05)

sueldo_neto = sueldo_bruto - descuento
polos = 3 if monto_vendido > 1000 else 1

print(f"Sueldo bruto: S/. {sueldo_bruto:.2f}\nDescuento: S/. {descuento:.2f}\nSueldo neto: S/. {sueldo_neto:.2f}\nPolos obsequiados: {polos}")


