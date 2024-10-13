import os
os.system("cls")

nota_matematicas = float(input("Ingrese la nota de Matemáticas: "))
nota_fisica = float(input("Ingrese la nota de Física: "))

propina_matematicas=3 if nota_matematicas > 17 else nota_matematicas
propina_fisica = 2 if nota_fisica > 15 else 0.5

total_propina = propina_matematicas+ propina_fisica
promedio = (nota_matematicas + nota_fisica) / 2

print(f"Total de la propina: S/. {total_propina:.2f}")
if promedio>16:
    print("¡Te obesquiará un reloj!")