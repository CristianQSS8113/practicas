import os
os.system ("cls")

unidades=int(input("Cantidad de unidades: "))

precio_unitario = 27 if unidades <= 25 else 25 if unidades <=50 else 23

importe_compra= unidades* precio_unitario
descuento=importe_compra * (0.15 if unidades > 50 else 0.05)

total_a_pagar=importe_compra - descuento

print(f"Importe de la compra: S/. {importe_compra:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Total a pagar: S/. {total_a_pagar:.2f}")