mujeres=int(input("Ingrese cantidad de mujeres: "))
varones=int(input("Ingrese cantidad de varones: "))

porcentaje_mujeres=(mujeres/(mujeres+varones))*100
porcentaje_varones=(varones/(mujeres+varones))*100

print(f"Porcentaje de varones: {porcentaje_varones: .2f}%")
print(f"Porcentaje de mujeres: {porcentaje_mujeres: .2f}%")

