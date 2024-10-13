import os
os.system("cls")

cuadernos = int(input("Cuadernos adquiridos: "))

if cuadernos < 12:
    lucas = faber = pilot = 0
elif cuadernos < 24:
    lucas = cuadernos // 4
    faber = pilot = 0
elif cuadernos < 36:
    faber = (cuadernos // 4) * 2
    lucas = pilot = 0
else:
    pilot = (cuadernos // 4) * 2
    faber = (cuadernos // 6)
    lucas = (cuadernos // 12)

print(f"Lapiceros Lucas: {lucas}, Faber: {faber}, Pilot: {pilot}")