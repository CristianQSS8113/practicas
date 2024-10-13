import os
os.system("cls")

docenas = int(input("Cantidad de docenas: "))
precio_docena=100

monto_compra= docenas* precio_docena
descuento= 0.15 * monto_compra if docenas >=6 else 0.10 * monto_compra
total_a_pagar= monto_compra - descuento

lapiceros_obsequio = (docenas //3) * 2 if docenas >=30 else 0

print(f"Monto de la compra: S/. {monto_compra:.2f}, Descuento: S/. {descuento:.2f}, Total a pagar: S/. {total_a_pagar:.2f}, Lapiceros de obsequio: {lapiceros_obsequio}")