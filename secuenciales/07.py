import os
os.system ("cls")

base=float(input("Base del rectángulo: "))
altura=float(input("Altura del rectángulo"))

area= base * altura

perimetro = 2* (base + altura)

print(f"La area es {area:.2f} unidades cuadradas")
print(f"El perimetro es: {perimetro:.2f} unidades ")