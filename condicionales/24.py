import os
os.system("cls")

monto_vendido = float(input("Monto total vendido: "))

comision= 0.10 * monto_vendido
sueldo_exceso = (monto_vendido-5000) // 500 * 25 if monto_vendido > 5000 else 0
sueldo_total =comision+ sueldo_exceso

print(f"Sueldo total del vendedor: S/. {sueldo_total:.2f}")
