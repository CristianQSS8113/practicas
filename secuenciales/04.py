import os
os.system("Cls")

print("Estatura")
pies=int(input("Pies: "))
pulgadas=int(input("Pulgadas: "))

metros = (pies * 0.3048) + (pulgadas* 0.0254)

print(f"Tu estatura en metros es: {metros}, m")