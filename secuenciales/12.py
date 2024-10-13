import os
os.system ("cls")

import math

a = float(input("Coeficiente a :"))
b = float(input("Coeficiente b :"))
c = float(input("Coeficiente c : "))

discriminante= b**2 - 4*a*c

raiz1 = (-b + math.sqrt(discriminante * (discriminante >= 0))) / (2 * a)
raiz2 = (-b - math.sqrt(discriminante * (discriminante >= 0))) / (2 * a)

print(f"Raiz 1: {raiz1 * (discriminante >=0)}")
print(f"Raiz 2: {raiz2 * (discriminante >=0)}")