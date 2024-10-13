import os
os.system ("cls")

import math

radio= float(input("Radio del cilindro: "))
altura= float(input("Altura del cilindro: "))

area_base = math.pi * (radio **2)

area_lateral= 2 * math.pi * radio * altura

area_total = 2 * area_base + area_lateral

print(f"Area base del cilindro: {area_base:.2f} unidades cuadradas")
print(f"Lateral del clindro: {area_lateral:.2f} unidades cuadradas")
print(f"Total del cilindro: {area_total:.2f} unidades cuadradas")