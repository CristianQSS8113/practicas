import os
os.system("cls")

peso = float(input("Peso en kg: "))
estatura = float(input("Estatura en metros: "))
imc = peso / (estatura ** 2)

if imc < 20:
    grado = "Delgado"
elif imc <= 25:
    grado = "Normal"
elif imc <= 27:
    grado = "Sobrepeso"
else:
    grado = "Obesidad"

print(f"IMC: {imc:.2f} - Grado de Obesidad: {grado}")