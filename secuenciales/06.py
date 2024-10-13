import os
os.system("cls")

import math

radio= float(input("Radio del cilindro: "))
altura = float(input(" Altura del cilindro: "))

area_total= 2 * math.pi * radio * ( radio + altura)

volumen= math.pi * (radio **2) * altura

print(f"Área total del cilindro : {area_total: .2f} ")
print(f"Volumen del cilindro: {volumen:.2f} ")