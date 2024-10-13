import os
os.system ("cls")

angulo=float(input("Ángulo en grados: "))

if angulo ==0:
    clasificacion="Nulo"
elif 0 < angulo < 90:
    clasificacion= "Agudo"
elif angulo == 90:
    clasificacion= "Recto"
elif 90 < angulo < 180:
    clasificacion= "Obtuso"
elif angulo== 180:
    clasificacion= "Llano"
elif 180 < angulo < 360:
    clasificacion= "Cóncavo"
elif angulo == 360:
    clasificacion= "Completo"
else:
    clasificacion="Ángulo fuerda de rango"

print(f"La clasificacion del angulo es: {clasificacion}")