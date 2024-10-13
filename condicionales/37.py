import os 
os.system("cls")

votos = {
    'Pamela': int(input("Votos para Pamela: ")),
    'Carol': int(input("Votos para Carol: ")),
    'Fanny': int(input("Votos para Fanny: "))
}

total_votos = sum(votos.values())
mayoria = total_votos / 2 + 1

ganador = [candidato for candidato, voto in votos.items() if voto >= mayoria]

if len(ganador) == 1:
    print(f"Gana: {ganador[0]}")
elif len(ganador) == 0:
    ordenados = sorted(votos.items(), key=lambda x: x[1], reverse=True)
    if ordenados[0][1] == ordenados[1][1]:
        print("Elección anulada (empate)")
    else:
        print(f"Segunda vuelta entre {ordenados[0][0]} y {ordenados[1][0]}")
else:
    print("Elección anulada (empate entre las tres)")