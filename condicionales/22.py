import os
os.system("cls")

unidades_a = int(input("Ingrese la cantidad de unidades del Producto A: "))
unidades_b = int(input("Ingrese la cantidad de unidades del Producto B: "))

precio_a, precio_b= 25,30

importe_a = unidades_a * precio_a
importe_b = unidades_b * precio_b
importe_bruto = importe_a + importe_b

descuento_a = 0.15 * importe_a if unidades_a > 50 else 0
descuento_b = 0.15 * importe_a if unidades_b > 60 else 0
total_a_pagar = importe_bruto - (descuento_a + descuento_b)

print(f"Importe bruto: S/. {importe_bruto:.2f}, Descuento total: S/. {descuento_a + descuento_b:.2f} , Total a pagar: S/. {total_a_pagar:.2f}")