import os
os.system("cls")

juan_aporte=float(input("Aporte de Juan en dólares: "))
rosa_aporte=float(input("Aporte en dólares: "))
daniel_aporte=float(input("Aporte de Daniel en soles: "))

dolar_a_soles= 3.00
daniel_aporte_dolares=daniel_aporte/dolar_a_soles

capital_total_dolares= juan_aporte + rosa_aporte + daniel_aporte_dolares

porcentaje_juan= (juan_aporte / capital_total_dolares) * 100
porcentaje_rosa= (rosa_aporte / capital_total_dolares) * 100
porcentaje_daniel= (daniel_aporte_dolares / capital_total_dolares) * 100

print(f"Capital en dolares : ${capital_total_dolares:.2f}")
print(f"Porcentaje de aporte de Juan : {porcentaje_juan:.2f}%")
print(f"Porcentaje de aporte de Rosa : {porcentaje_rosa:.2f}%")
print(f"Porcentaje de aporte de Daniel : {porcentaje_daniel:.2f}%")

