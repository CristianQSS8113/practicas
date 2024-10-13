import os
os.system("cls")

monto_total=float(input("Monto total de la compra: "))

porcentaje_prestamo = 0.30 if monto_total > 5000 else 0.20
monto_prestamo = monto_total * porcentaje_prestamo
intereses = monto_prestamo * 0.10

dinero_propio=monto_total - monto_prestamo

print(f"Monto del prestamo: S/. {monto_prestamo:.2f}")
print(f"Intereses: S/. {intereses:.2f}")
print(f"Total a pagar al banco S/. {monto_prestamo + intereses:.2f}")
print(f"Dinero propio a pagar: S/. {dinero_propio:.2f}")

