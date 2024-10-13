import os
os.system("cls")

numero_tarjeta=int(input("Número de la tarjeta: "))

monto_compra=float(input("Monto de la compra: "))

if numero_tarjeta % 2 == 0 and numero_tarjeta >= 100:
    descuento = 0.15 * monto_compra
else:
    descuento = 0.05 * monto_compra
    
total_a_pagar=monto_compra-descuento

print(f"Número de la tarjeta: {numero_tarjeta}")
print(f"Monto de la compra: S/.{monto_compra:.2f}")
print(f"Descuento: {descuento:.2f}")
print(f"Total a pagar: S/. {numero_tarjeta:.2f}")


