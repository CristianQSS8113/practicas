import os
os.system("cls")

mat_prom = (float(input("Mat. Práctica 1: ")) * 0.1 +
            float(input("Mat. Práctica 2: ")) * 0.2 +
            float(input("Mat. Práctica 3: ")) * 0.1 +
            float(input("Mat. Ex. Parcial: ")) * 0.3 +
            float(input("Mat. Ex. Final: ")) * 0.3)

fis_prom = (float(input("Fís. Práctica 1: ")) * 0.2 +
            float(input("Fís. Práctica 2: ")) * 0.2 +
            float(input("Fís. Práctica 3: ")) * 0.2 +
            float(input("Fís. Ex. Parcial: ")) * 0.2 +
            float(input("Fís. Ex. Final: ")) * 0.2)

qui_prom = (float(input("Quím. Práctica 1: ")) * 0.1 +
            float(input("Quím. Práctica 2: ")) * 0.3 +
            float(input("Quím. Práctica 3: ")) * 0.1 +
            float(input("Quím. Ex. Parcial: ")) * 0.25 +
            float(input("Quím. Ex. Final: ")) * 0.25)

for materia, prom in zip(["Matemática", "Física", "Química"], [mat_prom, fis_prom, qui_prom]):
    print(f"{materia}: {prom:.2f} - {'Aprobado' if prom >= 13 else 'Desaprobado'}")