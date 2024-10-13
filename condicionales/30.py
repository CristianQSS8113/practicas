import os
os.system("cls")

cuota=float(input("Monto de la cuota: "))
dias_pago=float(input("Dia de pago (1-30): "))

if dias_pago <=10:
    total_a_pagar= cuota - max(5, 0.02* cuota)
elif dias_pago <=20:
    total_a_pagar = cuota
else:
    total_a_pagar = cuota+max(10,0.03 * cuota)
    
print(f"Total a pagar: S/. {total_a_pagar:.2f}")
