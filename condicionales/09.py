import os 
os.system("cls")

productos= {
    101: (17, 0.05,(1,10)),
    102: (25, 0.09, (11,20)),
    103: (16, 0.10, (21, 30)),
    104: (27, 0.13, (31, float('inf')))
}

codigo=int(input("Codigo del producto (101, 102, 103, 104): "))
unidades = int(input("Cantidad de unidades: "))

if codigo in productos:
    precio, descuento, rango =productos[codigo]
    importe = precio * unidades
    descuento_aplicado= importe * descuento if rango[0] <= unidades <= rango[1] else 0
    total = importe - descuento_aplicado
    
    print(f"Importe: S/. {importe:.2f} Descuento: S/. {descuento_aplicado:.2f} Total a pagar: S/. {total:.2f}")
    